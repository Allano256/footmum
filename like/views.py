from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from like.models import Likes
from like.serializer import LikesSerializer

# Create your views here.

class LikeList(generics.ListCreateAPIView):
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]
    serializer_class= LikesSerializer
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        """
        This will ensure that the like is made by only the signed in user only.
        """
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveAPIView):
    """
    Only the user that liked the post can unlike it.
    """
    permission_classes=[IsOwnerOrReadOnly]
    serializer_class= LikesSerializer
    queryset = Likes.objects.all()
