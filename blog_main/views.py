from pyexpat import features
from tkinter import N
from django.shortcuts import render
from blogs.models import Category, Blog
from blogs.models import About

def home(request):
    features_posts = Blog.objects.filter(is_featured=True, status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status = 'Published')
    
    
    ## Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
        
    context = {
        'features_posts': features_posts,
        'posts' : posts,
        'about' : about
    }
    return render(request, "home.html", context)
