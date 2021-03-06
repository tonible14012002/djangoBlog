from django import template
from ..models import Post
# from interact.models import Comment
from django.db.models import Q, Count

register = template.Library()

# @register.simple_tag
# def comment_count(post):
#     return Comment.objects.filter(post=post).count()

# @register.inclusion_tag('blogSite/post/feed.html')
# def mostCommentPost(num = 5, user=None):
#     if user:
#         posts = Post.published\
#             .filter(author=user)\
#             .annotate(comment_count=Count('comments'))\
#             .order_by('-comment_count')[:num]
#     else:
#         posts = Post.published\
#             .annotate(comment_count=Count('comments'))\
#             .order_by('-comment_count')[:num]

#     return {'posts':posts, 'post_list':'most_comment'}

@register.inclusion_tag('blogSite/post/feed.html')
def  latestPost(num=5, user=None):
    if user:
        posts = Post.published\
            .filter(author=user)\
            .order_by('-update','-publish', '-create')[:num]
    else:
        posts = Post.published\
            .order_by('-update','-publish', '-create')[:num]
    return {'posts':posts, 'post_list':'latest_post'}

@register.simple_tag
def totalPost(user=None):
    if user:
        return Post.published.filter(user=user).count()
    return Post.published.count()
