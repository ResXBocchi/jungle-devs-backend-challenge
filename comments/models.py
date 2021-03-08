from django.db import models
from posts.models import Post
from helpers.models import Base
from settings import settings


# Create your models here.

class Comment(Base):
    content = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        default=0

    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )