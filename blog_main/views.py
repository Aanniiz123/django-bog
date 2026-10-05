from pyexpat import features
from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    features_posts = Blog.objects.filter(is_featured=True, status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status = 'Published')
    
    context = {
        'features_posts': features_posts,
        'posts' : posts,
    }
    return render(request, "home.html", context)
