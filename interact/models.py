from django.db import models
from blogSite.models import Post, User
from django.conf import settings

# Create your models here.
class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='emotion')
    create = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-create']
