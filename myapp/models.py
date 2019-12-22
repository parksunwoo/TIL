from django.db import models
from django.core.validators import MinLengthValidator

min_length_3_validator = MinLengthValidator(3)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)