from rest_framework import serializers
from .models import Comment


class CommentSeializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model, adds three extra fields when returning a list of Comment instances.
    """
    owner= serializers.ReadOnlyField(source='owner.username')


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model= Comment
        fields= [
           'id', 'owner','broadcast','created_at','updated_at','content'
        ]

class CommentDetailSerializer(CommentSeializer):
     """
     Serializer for the comment model used in Detail view 
     broadcast is a read only field so that we dont have to set it on each update
     When editing a Comment, it should always be associated with the same broadcast.
     Therefore, we should create an additional serializer which automatically references the broadcast Id which the comment is associated with.
     """
     broadcast = serializers.ReadOnlyField(source='broadcast.id')

      
