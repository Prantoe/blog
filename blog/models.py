from django.db import models

from author.models import User


class Tag(models.Model):
      title = models.CharField(max_length=100)
      
      class Meta:
            # verbose_name="tag"
            # verbose_name_plural="tags"
            ordering=['title']

      def __str__(self):
          return self.title

class Post(models.Model):
      title = models.CharField(max_length=50)
      tags = models.ManyToManyField('Tag')
      publish_date = models.DateTimeField(auto_now_add=True)
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      content = models.TextField()
      slug_blog = models.SlugField(max_length=100, unique=True)

      def __str__(self):
            return self.title + ' | ' + str(self.author)

      
