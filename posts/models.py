from django.db import models
from helpers.models import Base
from topics.models import Topic
# Create your models here.

class Post(Base):
    content = models.TextField(max_length=40000)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE
    )