from django.shortcuts import render
from .serializers import CommentSeializer, CommentDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions



# Create your views here.
class CommentList(generics.ListCreateAPIView):
    serializer_class= CommentSeializer
    permissions_class= [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()


    def  perform_create(self, serializer):
        broadcast_id =self.request.data.get('broadcast_id')
        serializer.save(broadcast_id=broadcast_id)

    filter_backends=[
        DjangoFilterBackend
    ]

    filterset_fields = [
        'broadcast'
    ]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This will ensure that only the owners of the comments cxan retrieve, edit or destroy a comment
    """
    permission_class = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()


