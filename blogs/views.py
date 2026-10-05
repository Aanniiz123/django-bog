from .models import Blog, Category
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def posts_by_category(request, category_id):
    ## Fetch the post that belongs to the category with the id categoryid
    
    posts = Blog.objects.filter(status = 'Published', category = category_id)
    
    try:
        category = Category.objects.get(pk = category_id)
    except:
        return redirect('home')
    
    context = {
        'posts' : posts,
        'category' : category,
    
    }
    return render(request, 'post_by_category.html', context)