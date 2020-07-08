from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
	posts = Post.objects.all()
	return render(request,"django_app/home.html",{'posts':posts})

def contact(request):
	return render(request,"django_app/contact.html")

def about(request):
	return render(request,"django_app/about.html")