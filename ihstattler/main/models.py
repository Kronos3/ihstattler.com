from django.db import models
from django.utils.dateparse import parse_datetime

class Category(models.Model):
    term_id = models.CharField(max_length=128)
    nice_name = models.CharField(max_length=64)
    cat_parent = models.CharField(max_length=64)
    cat_name = models.CharField(max_length=64)

    @staticmethod
    def parse(element):
        category = Category(element.find("./term_id").text,
                            element.find("./category_nicename").text,
                            element.find("category_parent").text,
                            element.find("./cat_name)").text)
        category.save()
        return category


class Tag(models.Model):
    term_id = models.CharField(max_length=128)
    slug = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

    @staticmethod
    def parse(element):
        tag = Tag(element.find("./term_id").text,
                  element.find("./tag_slug").text,
                  element.find("./tag_name"))
        tag.save()
        return tag


class Term(models.Model):
    term_id = models.CharField(max_length=128)
    taxonomy = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    parent = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

    @staticmethod
    def parse(element):
        term = Term(element.find("./term_id").text,
                    element.find("./term_taxonomy").text,
                    element.find("./term_slug").text,
                    element.find("./term_parent").text,
                    element.find("./term_name").text)
        term.save()
        return term


class Profile(models.Model):
    nice_name = models.CharField(max_length=64)
    human_name = models.CharField(max_length=64)


class Item(models.Model):
    title = models.TextField()
    link = models.CharField(max_length=256)
    pub_date = models.DateField()
    encoded_content = models.TextField()
    post_id = models.IntegerField()
    post_date = models.DateTimeField()
    attachment_url = models.CharField(max_length=256, null=True)

    category = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="category_tag", null=True)
    post_tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="article_tag", null=True)
    byline = models.ManyToManyField(Profile)

    @staticmethod
    def parse(element):
        tag = None
        post_tag = None
        byline = []
        print(element.findall("./content_encoded"))
        encoded_content = element.find("./content_encoded").text
        attachment_url = None
        for cat in element.findall("./category"):
            if cat.attrib["domain"] == "category":
                try:
                    tag = Tag.objects.get(nice_name=cat.attrib["nicename"])
                except Tag.objects.model.DoesNotExist:
                    print("Tag %s not found" % cat.attrib["nicename"])
                    tag = None
            if cat.attrib["domain"] == "byline":
                try:
                    current_byline = Profile.objects.get(nice_name=cat.attrib["nicename"])
                except Profile.objects.model.DoesNotExist:
                    current_byline = Profile(nice_name=cat.attrib["nicename"], human_name=cat.text)
                    current_byline.save()
                byline.append(current_byline)
            if cat.attrib["domain"] == "post_tag":
                try:
                    post_tag = Tag.objects.get(nice_name=cat.attrib["nicename"])
                except Tag.objects.model.DoesNotExist:
                    print("Post Tag %s not found" % cat.attrib["nicename"])
                    post_tag = None

        for meta in element.findall("postmeta"):
            meta_key = meta.find("meta_key").text
            if meta_key.startswith("_oembed_") and not meta_key.startswith("_oembed_time_"):
                encoded_content = meta.find("meta_value").text
            elif meta_key == "_wp_attached_file":
                attachment_url = meta.find("meta_value").text

        item = Item(title=element.find("./title").text,
                    link=element.find("./link").text,
                    pub_date=parse_datetime(element.find("./pubDate").text),
                    encoded_content=encoded_content,
                    post_id=element.find("./post_id").text,
                    post_date=parse_datetime(element.find("./post_date").text),
                    category=tag,
                    post_tag=post_tag,
                    attachment_url=attachment_url
                    )
        item.save()
        item.byline.set(byline)
        return item


def parse(to_parse):
    import xml.etree.ElementTree as ET
    tree = ET.parse('TattlerWordpressRecent.xml')
    root = tree.getroot()
    content = root[0]

    if to_parse == "tags":
        for tag in content.findall("./tag"):
            Tag.parse(tag)
    elif to_parse == "category":
        for cat in content.findall("./category"):
            Category.parse(cat)
    elif to_parse == "term":
        for term in content.findall("./term"):
            Term.parse(term)
    elif to_parse == "item":
        for item in content.findall("./item"):
            Item.parse(item)
