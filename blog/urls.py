from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

from rest_framework import routers
from .views import UserViewSet, EntryViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)
