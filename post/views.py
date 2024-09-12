from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Broadcast
from .serializers import BroadcastSerializer


class BroadcastList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = BroadcastSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Broadcast.objects.annotate(
        comments_count =Count('comment',distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')

    filter_backends=[
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
     
     
    #  This will be the field section to chose from
    filterset_fields=[
        'owner__followed__owner__bio',
        'likes__owner__bio',
        'owner__bio',
    ]
    

    # This adds text search functionality to the application
    search_fields=[
        'owner__username',
        'title',
    ]


    ordering_fields=[
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]



    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BroadcastDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = BroadcastSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Broadcast.objects.annotate(
        comments_count =Count('comment',distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')











# from rest_framework import status, permissions
# from rest_framework.exceptions import NotFound
# from .serializers import BroadcastSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Broadcast



# # Create your views here.
# class BroadcastList(APIView):
#     """
#     This function will list all the posts available.
#     Permissions are added to ensure only authenticated users  have access to the posts.
#     """

#     serializer_class =BroadcastSerializer
#     permission_classes=[
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def get(self,request):
#         broadcast= Broadcast.objects.all()
#         serializer = BroadcastSerializer(broadcast, many=True, context={'request':request})
#         return Response (serializer.data)
    
#     def post(self, request):
#         serializer=BroadcastSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )
     

# class BroadcastDetail(APIView):
#     """
#     This function will update and delete a broadcast.
#     """
#     def get_object(self, pk):
#         try:
#             broadcast = Broadcast.objects.get(pk=pk)
#             self.check_object_permissions(self.request, broadcast)
#             return broadcast
#         except Broadcast.DoesNotExist:
#             return NotFound('The post does not exist...')
        
#     def get(self, request,pk):
#         """
#         Retrieve a broadcast by ID.
#         """
#         broadcast = self.get_object(pk)
#         serializer= BroadcastSerializer(broadcast, context={'request':request})
#         return Response(serializer.data)
    
    
#     def put(self, request, pk):
#         """
#         This will update a broadcast by ID
#         """
#         broadcast= self.get_object(pk)
#         serializer= BroadcastSerializer(broadcast, data=request.data, context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         broadcast=self.get_object(pk)
#         broadcast.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )

        
