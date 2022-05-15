from django import template
from..models import Like
from blogSite.models import Post
from django.db.models import Q, Count


register = template.Library()

@register.simple_tag
def likeIcon(user, post):
    if Like.objects.filter(user=user,post=post).count():
        return 'unlike'
    else:
        return 'like'

@register.simple_tag
def totalLikes(post):
    return post.likes.count()

@register.inclusion_tag('blogSite/post/feed.html')
def mostLikePost(num, user=None):
    if user:
        posts = Post.published\
            .filter(author=user)\
            .annotate(
                like_count = Count('likes')
            ).order_by('-like_count')[:num]
    else:
        posts = Post.published\
            .annotate(
                like_count = Count('likes')
            ).order_by('-like_count')[:num]
    return {'posts':posts, 'post_list':'most_like'}

