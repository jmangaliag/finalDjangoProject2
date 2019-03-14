from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import PostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Post
# Create your views here.

def index(request):
    context = {}
    if request.user.is_authenticated:
        posts = Post.objects.filter(is_active=True).order_by('-date_posted')
        context = {
            'posts': posts
        }
    return render(request, 'index.html', context)

@login_required
def delete(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    post.is_active = False
    post.save()
    return redirect('/')

@login_required
def post(request):
    context = {}
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context['form'] = form
            return render(request, 'post.html', context)
    else:
        context['form'] = PostModelForm(initial={'posted_by':request.user})
        return render(request, 'post.html', context)

@login_required
def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context['form'] = form
            return render(request, 'details.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
        return render(request, 'details.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registerPage.html', {'form': form})
