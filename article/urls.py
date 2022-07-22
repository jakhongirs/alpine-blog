from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.AllArticlesView.as_view(), name="all_article"),
    path('articles/main/', views.IsMainNewsView.as_view(), name="is_main"),
    path('articles/popular/', views.IsPopularArticlesView.as_view(), name="is_popular"),
    path('articles/foryou/', views.IsForYouArticlesView.as_view(), name="is_foryou"),
    path('article/<int:id>/', views.ArticleDetailView.as_view()),
]
