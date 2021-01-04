from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Post

def allPosts(request):
    all_posts=Post.objects.all()
    context={'all_posts':all_posts}
    return render(request,'all_posts.html',context)

def post(request,id):
    # post=Post.objects.get(id=id)
    post=get_object_or_404(Post,id=id)
    context={'post':post}
    return render(request,'detail.html', context)