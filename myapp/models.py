from django.db import models
from django.core.validators import MinLengthValidator

min_length_3_validator = MinLengthValidator(3)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    ip = models.CharField(max_length=15)

class GameUser(models.Model):
    server = models.CharField(max_length=10)
    username = models.CharField(max_length=20, validators=[MinLengthValidator])

    class Meta:
        unique_together = [
            ('server', 'username'),
        ]
