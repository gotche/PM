from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # This is the only required field
    user = models.ForeignKey(User, unique=True)

    # The rest is completely up to you...
    permisos= models.CharField(max_length=100, blank=True)
