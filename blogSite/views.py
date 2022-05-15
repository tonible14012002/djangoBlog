import json
from django.contrib.auth.models import User

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, Page, \
    PageNotAnInteger, EmptyPage, InvalidPage
from blog.settings import EMAIL_HOST_USER
from .models import Emotion, Post, Comment
from django.views.generic.list import ListView
from .form import CommentForm, PostCreationForm, ShareForm
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
        if 'comment' in request.POST:
            commentForm = CommentForm(request.POST)
            if commentForm.is_valid():
                cmt = commentForm.save(commit=False)
                cmt.post = post
                cmt.save()
                return redirect(post.get_absolute_url())
        else:
            commentForm = CommentForm()
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
        commentForm = CommentForm()
        emailForm = ShareForm()

    context = {'post':post, 'commentForm':commentForm,\
         'emailForm':emailForm, 'sent':sent}
    return render(request,'blogSite/post/post_detail.html',context)

@login_required
def post_like(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data['post_id']
        post = get_object_or_404(Post,pk=post_id)
        newEmotion, created = Emotion.objects.get_or_create(post=post,user=request.user)
        if not created:
            newEmotion.delete()
        total = Emotion.objects.filter(post=post).count()
    return JsonResponse({'liked':created, 'total':total},status=200)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.author = request.user
            newPost.save()
            return redirect(newPost.get_absolute_url())
    else:
        form = PostCreationForm()
    context = {'form':form}
    return render(request,'blogSite/post/post_create.html', context)