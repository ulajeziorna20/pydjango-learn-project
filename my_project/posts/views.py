from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.

# protector
from django.contrib.auth.decorators import login_required

def posts_list(request):

# tutaj pobierasz wszystkie posty
  posts = Post.objects.all().order_by('-date')

  return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):

    post = Post.objects.get(slug=slug)

    return render(request, 'posts/post_page.html', {'post': post})

  # return HttpResponse(slug)


@login_required(login_url="/users/login/")
def posts_new(request):
  return render(request, 'posts/post_new.html')