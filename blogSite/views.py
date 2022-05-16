import json
from django.contrib.auth.models import User

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, Page, \
    PageNotAnInteger, EmptyPage, InvalidPage
from blog.settings import EMAIL_HOST_USER
from .models import Post
from django.views.generic.list import ListView
from .form import PostCreationForm, ShareForm
from blogSite import form
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

class page_list(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'blogSite/post/postlist.html'
    paginate_by = 3

@login_required
def post_detail(request,year,month,day,pk,slug):
    user = get_object_or_404(User,pk=pk)
    post = get_object_or_404(
        Post,
        slug=slug,
        publish__year = year,
        publish__month = month,
        author = user,
        publish__day = day
    )
    sent = False
    if request.method == 'POST':
        if 'redirect' in request.POST:
            return redirect(post.get_absolute_url())

        if 'share' in request.POST:
            emailForm = ShareForm(request.POST)
            if emailForm.is_valid():
                data = emailForm.cleaned_data
                # send email
                subject = 'Django email'
                body = \
                    f"{data['name']} recommended you to read {post} at: \n{post.get_absolute_url()}\n{data['name']} comments: {data['body']}"
                send_mail(subject,body,EMAIL_HOST_USER, [data['to']],fail_silently=False)
                sent = True
        else:
            emailForm = ShareForm()
    else:
        emailForm = ShareForm()

    context = {'post':post,\
         'emailForm':emailForm, 'sent':sent}
    return render(request,'blogSite/post/post_detail.html',context)

