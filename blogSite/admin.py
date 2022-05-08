import imp
from django.contrib import admin
from .models import Emotion, Post, Comment
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug', 'status', 'update', 'create']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'create']

@admin.register(Emotion)
class EmotionAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'create']