from django.urls import path
from . import views

app_name='interact'
urlpatterns = [
    path('like/', views.post_like, name='post_like'),
]