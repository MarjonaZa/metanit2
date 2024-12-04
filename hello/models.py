from django.db import models

# Create your models here.
#комиты

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    def __str__(self):
        return self.name