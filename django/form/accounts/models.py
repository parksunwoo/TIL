from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, validators=[RegexValidator(r'^010[1-9]\d{7}$')])

