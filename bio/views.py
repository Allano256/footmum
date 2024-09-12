from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Bio
from .serializers import BioSerializer


class BioList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    posts_count-number of posts a profile owner has created.
    followers_count-number of users folowing a profile.
    following_count-number of profiles a profile owner is following
    annotate allows to get extra query fields
    The double underscore helps to show the relationships
    dinstinct is set to true so that we dont get duplicates
    """
    queryset = Bio.objects.annotate(
       broadcast_count= Count('owner__broadcast', dinstinct=True),
       followers_count =Count('owner__followed', dinstinct=True),
       following_count=Count('owner__following',dinstinct=True)
    ).order_by('-created_at')
    serializer_class = BioSerializer

    filter_backends =[
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    
    # We have to set the filter set fiels to filter profiles that are following a profile given its id

    filterset_fields=[
       'owner__following__followed__bio',
       'owner__followed__owner__bio',
    ]



    ordering_fields=[
        'broadcast_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at'
    ]


class BioDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Bio.objects.annotate(
       broadcast_count= Count('owner__broadcast', dinstinct=True),
       followers_count =Count('owner__followed', dinstinct=True),
       following_count=Count('owner__following',dinstinct=True)
    ).order_by('-created_at')
    serializer_class = BioSerializer








# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status 
# from rest_framework.exceptions import NotFound
# from .serializers import BioSerializer
# from drf_api.permissions import IsOwnerOrReadOnly

# from .models import Bio


# # Create your views here.

# class BioList(APIView):
#     """
#     This function  will return all the profiles.
#     """
#     serializer_class= BioSerializer


#     def get(self, request):
#         bio = Bio.objects.all()
#         serializer=BioSerializer(bio, many=True, context={'request':request})
#         return Response(serializer.data)
    
# class BioDetail(APIView):
#     """
#     This will return just a single profile.
#     """
    
#     permission_classes = [IsOwnerOrReadOnly]

    
#     def get_object(self, pk):

#         try:
#             bio=Bio.objects.get(pk=pk)
#             self.check_object_permissions(self.request, Bio)
#             return bio
#         except Bio.DoesNotExist:
#             raise NotFound('Bio does not exist')
           

#     def get(self,request, pk):
#         bio = self.get_object(pk)
#         serializer = BioSerializer(bio, context={'request':request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
#     def put(self, request,pk):
#         """
#         This will update a user profile.
#         """
#         bio =self.get_object(pk)
#         serializer= BioSerializer(bio, data=request.data, context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


