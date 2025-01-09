from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostCreate(generics.CreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  lookup_field = 'pk'

class PostDetail(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  lookup_field = 'pk'

class PostUpdate(generics.UpdateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  lookup_field = 'pk'

class PostDelete(generics.DestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  lookup_field = 'pk'