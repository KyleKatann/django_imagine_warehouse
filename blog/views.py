from django.shortcuts import render
from django.utils import timezone
from .models import Post,Caliculator

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    cals  = Caliculator.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'cals': cals})
# Create your views here.
