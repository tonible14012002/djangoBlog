from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404
import json
from django.http.response import JsonResponse
from blogSite.models import Post
from .models import Like
# Create your views here.


@login_required
def post_like(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            post_id = data['post_id']
            post = get_object_or_404(Post,pk=post_id)
            newLike, created = Like.objects.get_or_create(post=post,user=request.user)
            if not created:
                newLike.delete()
            total = Like.objects.filter(post=post).count()
        return JsonResponse({'liked':created, 'total':total},status=200)
    except:
        return HttpResponseNotFound("<h1>Page not Found</h1>")
