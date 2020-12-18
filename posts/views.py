from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    
    posts = Post.objects.filter(user=request.user).order_by('-published_at')    
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            new_post.user = request.user
            new_post.save()

    context = {
        'posts':posts,
        'form':form,
        'title':'Home Page'
    }

    return render(request,'posts/home.html',context)

@login_required
def UpdatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Your task has been updated successfully')
        return redirect('/')

    context = {
        'form':form
    }

    return render(request,'posts/update.html',context)

@login_required
def DeletePost(request,pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        messages.warning(request,'Your task has been deleted successfully')
        return redirect('/')

    context = {
        'post':post
    }

    return render(request,'posts/delete.html',context)

