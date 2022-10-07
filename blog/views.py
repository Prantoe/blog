from blog.models import Post
from author.models import User

from django.views.generic import ListView, DetailView


class HomeView(ListView):
  queryset = Post.objects.order_by('-publish_date')
  model = Post
  template_name = 'home.html'

class DetailView(DetailView):
  model = Post
  template_name = 'detail.html'
  slug_field = 'slug_blog'
  slug_url_kwarg = 'slug_blog'


class AuthorView(DetailView):
  # queryset = Post.objects.filter(author=1)


  model = User
  template_name = 'auth.html'
  slug_field = 'name'
  slug_url_kwarg = 'name'

  # print(queryset)
