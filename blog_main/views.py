from pyexpat import features
from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    features_posts = Blog.objects.filter(is_featured=True).order_by('updated_at')
    context = {
        'categories': categories,
        'features_posts': features_posts,
    }
    return render(request, "home.html", context)
