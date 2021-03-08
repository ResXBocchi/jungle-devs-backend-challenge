from django.db import models
from helpers.models import Base
from topics.models import Topic
from settings import settings

# Create your models here.

class Post(Base):
    content = models.TextField(max_length=40000)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=0
    )