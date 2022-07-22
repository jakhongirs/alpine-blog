from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer
from rest_framework import generics
from helpers.pagination import CustomPagination, PageFive, PageThree


# Create your views here.

# ALL ARTICLES:
class AllArticlesView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPagination


# IS_MAIN:
class IsMainNewsView(generics.ListAPIView):
    queryset = Article.objects.filter(is_main=True)
    serializer_class = ArticleSerializer
    pagination_class = PageFive


# IS_POPULAR:
class IsPopularArticlesView(generics.ListAPIView):
    queryset = Article.objects.filter(is_popular=True)
    serializer_class = ArticleSerializer
    pagination_class = PageThree


# IS_FORYOU:
class IsForYouArticlesView(generics.ListAPIView):
    queryset = Article.objects.filter(is_popular=True)
    serializer_class = ArticleSerializer
    pagination_class = PageThree


# ARTICLE DETAIL
class ArticleDetailView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset
