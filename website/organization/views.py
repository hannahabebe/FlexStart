from django.shortcuts import get_object_or_404, render
from .models import Category, Post

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def blog(request):
    news = Post.objects.all()
    return render(request, 'blog.html', {'news':news})

def contact(request):
    return render(request, 'contact.html')


def blogSingle(request, id):
    news = get_object_or_404(Post,id = id)
    return render(request, 'blog-single.html', {'news':news})
