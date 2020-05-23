from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120, help_text="This is title for u issue")
    message = models.TextField(help_text="What's on your mind...")

    def __str__(self):
        return self.title
