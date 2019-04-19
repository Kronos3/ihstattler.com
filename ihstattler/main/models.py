from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    term_id = models.IntegerField()
    nice_name = models.CharField(max_length=32)
    cat_parent = models.CharField(max_length=32)
    cat_name = models.CharField(max_length=32)

    @staticmethod
    def parse(element):
        category = Category(element.find("./term_id").text, element.find("./category_nicename").text, element.find("category_parent").text, element.find("./cat_name)").text)
        category.save()
        return category

class Tag(models.Model):
    term_id = models.IntegerField()
    slug = models.CharField(max_length=32)
    name = models.CharField(max_length=32)

    @staticmethod
    def parse(element):
        tag = Tag(element.find("./term_id").text, element.find("./tag_slug").text, element.find("./tag_name"))
        tag.save()
        return tag

class Term(models.Model):
    term_id = models.IntegerField()
    taxonomy = models.CharField(max_length=32)
    slug = models.CharField(max_length=32)
    parent = models.CharField(max_length=32)
    name = models.CharField(max_length=32)

    @staticmethod
    def parse(element):
        term = Term(element.find("./term_id").text, element.find("./term_taxonomy").text, element.find("./term_slug").text, element.find("./term_parent").text, element.find("./term_name").text)
        term.save()
        return term

class ImageItem(models.Model):
    title = models.CharField(max_length=32)
    link = models.CharField(max_length=32)
    pub_date = datetime.strftime(models.charField(max_length=32), '%m/%d/%Y') #did you want me to turn this from a string into a datefield?
    post_id = models.IntegerField()
    post_date = models.DateField()
    attachment_url = models.URLField()

    @staticmethod
    def parse(element):
        item = ImageItem(element.find("./title").text, element.find("./link").text, element.find("./pubDate").text, element.find("./post_id").text, element.find("./post_date").text, element.find("./attachment_url").text)
        item.save()
        return item

class PostItem(models.Model):
    """ text = models.TextField()
    headline = models.CharField(max_length=128)
    authors = models.ManyToManyField(User)

    #published_on = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)"""

    title = models.CharField(max_length=32)
    link = models.CharField(max_length=32)
    pub_date = datetime.strftime(models.charField(max_length=32), '%m/%d/%Y')
    encoded_content = models.CharField(max_length=5000) #what length do I set this to because it is an article
    post_id = models.IntegerField()
    post_date = models.DateField()
    #<category domain="byline" nicename="john-peterson"><![CDATA[JOHN PETERSON]]></category>
	#<category domain="category" nicename="sports"><![CDATA[Sports]]></category>
	#<category domain="post_tag" nicename="student-feature"><![CDATA[Student Feature]]></category>
    #How do I parse something like this

    @staticmethod
    def parse(element):
        item = PostItem(element.find("./title").text, element.find("./link").text, element.find("./pubDate").text, element.find("./content:encoded").text, element.find("./post_id").text, element.find("./post_date").text)
        item.save()
        return item




