from ast import Delete
from email.policy import default
from multiprocessing import reduction
from pydoc import stripid
from pyexpat import model
import string
from django.forms import SlugField
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(max_length=20)
    avatar = models.ImageField(upload_to='user/%y/%m/%d')

    def __str__(self):
        fullname = self.user.first_name.strip() + ' ' + self.user.last_name.strip()
        if fullname:
            return fullname
        else:
            return self.user.username

    def save(self, *args, **kwargs):
        if not self.slug:
            fullname = self.user.first_name.strip() + ' ' + self.user.last_name.strip()
            self.slug = slugify(fullname)
        super(Profile, self).save(*args,**kwargs)

    def get_name(self):
        return self.user.first_name.strip() + ' ' + self.user.last_name.strip()

    def get_absolute_url(self):
        return reverse(
            'account:profile',
            args=[self.slug,
                self.user.id
                ]
            )

class Photo(models.Model):
    title = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='user/%y/%m/%d/')
    create = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='photos')
    