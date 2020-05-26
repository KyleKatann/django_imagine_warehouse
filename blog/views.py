from django.shortcuts import render
from django.utils import timezone
from .models import Post,Caliculator

#import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    cals  = Caliculator.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'cals': cals})
# Create your views here.
