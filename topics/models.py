from django.db import models
from helpers.models import Base
from settings import settings
# Create your models here.

class Topic(Base):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=0

    )
    description = models.TextField(max_length=500)
    urlname = models.SlugField(max_length=60)