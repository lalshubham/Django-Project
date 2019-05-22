from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Article,Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . import forms

# Create your views here.

def  index(request):
    return HttpResponse('Hello World')

def templateindex(request):
    articles = Blog.objects.all().order_by('title')
    return render(request,"NOR/index.html",{'articles':articles})

def blog_details(request, slug):
    blogs = Blog.objects.get(slug=slug)
    return render(request,"NOR/BlogView.html",{'blogs':blogs})

@login_required(login_url="/accounts/login")
def blog_create(request):
    if request.method == 'POST':
        form = forms.CreateBlog(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:list')
    else:
        form = forms.CreateBlog()
    return render(request,'NOR/blog_create.html',{'form':form})
