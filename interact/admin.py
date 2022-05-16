from django.contrib import admin
from .models import Like, Comment

# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'create']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =['user', 'create', 'edited']