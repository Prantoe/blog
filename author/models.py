from django.db import models


# Create your models here.
class User(models.Model):
      name = models.CharField(max_length=50)
      phone = models.FloatField(max_length=20)
      create_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.name