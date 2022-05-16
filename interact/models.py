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

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,
                            related_name='comments')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=250)
    edited = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.profile.get_name()
    
    class Meta:
        ordering = ['update', 'create']
