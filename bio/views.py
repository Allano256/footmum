from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.exceptions import NotFound
from .serializers import BioSerializer
from drf_api.permissions import IsOwnerOrReadOnly

from .models import Bio


# Create your views here.

class BioList(APIView):
    """
    This function  will return all the profiles.
    """
    serializer_class= BioSerializer


    def get(self, request):
        bio = Bio.objects.all()
        serializer=BioSerializer(bio, many=True, context={'request':request})
        return Response(serializer.data)
    
class BioDetail(APIView):
    """
    This will return just a single profile.
    """
    
    permission_classes = [IsOwnerOrReadOnly]

    
    def get_object(self, pk):

        try:
            bio=Bio.objects.get(pk=pk)
            self.check_object_permissions(self.request, Bio)
            return bio
        except Bio.DoesNotExist:
            raise NotFound('Bio does not exist')
           

    def get(self,request, pk):
        bio = self.get_object(pk)
        serializer = BioSerializer(bio, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request,pk):
        """
        This will update a user profile.
        """
        bio =self.get_object(pk)
        serializer= BioSerializer(bio, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


