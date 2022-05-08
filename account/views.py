from django import forms
from django.shortcuts import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Photo
from .form import RegistrationForm, UserEditForm, ProfileEditForm
from django.contrib import messages
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user_profile = Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html')
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def profile(request, slug, pk):
    user = get_object_or_404(User,pk=pk)
    context = {'user':user}
    return render(request, 'account/profile/profile.html', context)

def profile_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('account:profile_edit')
        else:
            messages.error(request, 'Error while updating your profile!')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request,'account/profile/form/edit.html', context)