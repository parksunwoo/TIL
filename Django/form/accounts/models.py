from Django.db import models
from Django.core.validators import RegexValidator
from Django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, validators=[RegexValidator(r'^010[1-9]\d{7}$')])

