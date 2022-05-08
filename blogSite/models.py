from django.utils import timezone
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=200,blank=False, null=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posts')
    slug = models.SlugField(max_length=10, unique_for_date='publish')
    body = models.TextField(blank=False, null=False)

    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='draft')
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    object = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-update','-publish']
    
    def get_absolute_url(self):
        return reverse(
            'blogsite:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
                ]  
        )

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=250)
    edited = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['update', 'create']

class Emotion(models.Model):
    STATIC_CHOICE = (
        ('like', 'Like'),
        ('unlike', 'Unlike'),
        ('love', 'Love'),
        ('Haha', 'haha')
    )
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='emotions')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='emotion')
    create = models.DateTimeField(auto_now_add=True)
    emotion = models.CharField(choices=STATIC_CHOICE,default='like',max_length=10)
    class Meta:
        ordering = ['-create']
