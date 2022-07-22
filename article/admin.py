from django.contrib import admin
from .models import Article, Tag, Comment, Bookmark


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(Bookmark)
