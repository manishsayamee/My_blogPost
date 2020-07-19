from django.shortcuts import render,get_object_or_404, redirect
from .models import Post


def home(request):
  return render(request, 'blogs/home.html',)

def PostList(request):
  qeuryset = Post.objects.filter(status=1).order_by('-created_on')
  context={
    'data':qeuryset
  }
  return render(request, 'blogs/index.html', context=context)


def PostDetail(request, user):
  user_obj=  Post.objects.get(id=user)
  return render(request, 'blogs/post_detail.html', context= { 
    'data':user_obj
   })
