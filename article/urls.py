from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.AllArticlesView.as_view(), name="all_article"),
]
