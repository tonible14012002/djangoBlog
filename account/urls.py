
from django.shortcuts import redirect
from django.urls import path,reverse_lazy, reverse
from . import views
from django.contrib.auth import views as auth_views

def Home(requets):
    return redirect('account:login')

app_name = 'account'
urlpatterns = [
    path('',Home),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/',views.user_register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),
    path('password_rese/done',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')), name= 'password_reset_confirm'),
    path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('profile/<slug:slug>/<int:pk>',views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('post_create/', views.post_create, name='post_create'),
    
]