
from rest_framework import status, permissions
from rest_framework.exceptions import NotFound
from .serializers import BroadcastSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Broadcast



# Create your views here.
class BroadcastList(APIView):
    """
    This function will list all the posts available.
    Permissions are added to ensure only authenticated users  have access to the posts.
    """

    serializer_class =BroadcastSerializer
    permission_classes=[
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self,request):
        broadcast= Broadcast.objects.all()
        serializer = BroadcastSerializer(broadcast, many=True, context={'request':request})
        return Response (serializer.data)
    
    def post(self, request):
        serializer=BroadcastSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
     

class BroadcastDetail(APIView):
    """
    This function will update and delete a broadcast.
    """
    def get_object(self, pk):
        try:
            broadcast = Broadcast.objects.get(pk=pk)
            self.check_object_permissions(self.request, broadcast)
            return broadcast
        except Broadcast.DoesNotExist:
            return NotFound('The post does not exist...')
        
    def get(self, request,pk):
        """
        Retrieve a broadcast by ID.
        """
        broadcast = self.get_object(pk)
        serializer= BroadcastSerializer(broadcast, context={'request':request})
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        """
        This will update a broadcast by ID
        """
        broadcast= self.get_object(pk)
        serializer= BroadcastSerializer(broadcast, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        broadcast=self.get_object(pk)
        broadcast.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

        
