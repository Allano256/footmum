from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSeializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model, adds three extra fields when returning a list of Comment instances.
    """
    owner= serializers.ReadOnlyField(source='owner.username')
    is_owner =serializers.SerializerMethodField()
    profile_id =serializers.ReadOnlyField(source='owner.bio.id')
    profile_image=serializers.ReadOnlyField(source='owner.bio.image.url')
    created_at =serializers.SerializerMethodField()
    updated_at =serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
       
    

    
    class Meta:
        model= Comment
        fields= [
           'id', 'owner','broadcast','created_at','updated_at','content','is_owner','profile_id','profile_image','created_at','updated_at',
        ]

class CommentDetailSerializer(CommentSeializer):
     """
     Serializer for the comment model used in Detail view 
     broadcast is a read only field so that we dont have to set it on each update
     When editing a Comment, it should always be associated with the same broadcast.
     Therefore, we should create an additional serializer which automatically references the broadcast Id which the comment is associated with.
     """
     broadcast = serializers.ReadOnlyField(source='broadcast.id')

      
