from rest_framework import serializers
from .models import Article, Tag
from common.serializer import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"
