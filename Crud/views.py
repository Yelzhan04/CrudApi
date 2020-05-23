from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializers


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
