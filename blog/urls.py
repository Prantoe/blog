from django.urls import path
from blog.views import HomeView, DetailView, AuthorView


urlpatterns=[
  path('', HomeView.as_view(), name="home"),
  path('article/<slug:slug_blog>/', DetailView.as_view(), name='detail'),
  path('blog/author/<slug:name>/', AuthorView.as_view(), name='auth')
  ]