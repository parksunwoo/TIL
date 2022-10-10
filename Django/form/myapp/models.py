from Django.db import models
from Django.urls import reverse
from Django.core.validators import MinLengthValidator

min_length_3_validator = MinLengthValidator(3)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator], help_text='글 제목입니다. 100자 이내로 입력해주세요')
    content = models.TextField(help_text='글 내용')
    user_agent = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])

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
