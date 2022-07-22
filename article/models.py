from django.db import models
from helpers.models import BaseModel
from common.models import User


# Create your models here.

# TAG:
class Tag(BaseModel):
    slug = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# ARTICLE:
class Article(BaseModel):
    slug = models.CharField(max_length=128, unique=True)

    title = models.CharField(max_length=128, verbose_name='Title')
    sub_title = models.CharField(max_length=128, verbose_name='Sub_title')
    content = models.TextField()
    published_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to="articles/", null=True, blank=True)
    image_caption = models.CharField(max_length=128, null=True, blank=True)
    read_time = models.IntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)

    tags = models.ManyToManyField(Tag, related_name='articles', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles', blank=True)

    is_main = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_for_you = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# COMMENT:
class Comment(BaseModel):
    text = models.TextField(null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


# BOOKMARK:
class Bookmark(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
