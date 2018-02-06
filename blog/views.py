from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
# Retrieves a web request and returns a web response. Inside view goes all the the logic to return desired response. First create application view, define url pattern for each view, and then templates = Returns http response.

def post_list(request):
	posts = Post.published.all()
	return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


