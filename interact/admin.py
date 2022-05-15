from django.contrib import admin
from .models import Like

# Register your models here.
@admin.register(Like)
class EmotionAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'create']