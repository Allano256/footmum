from rest_framework import serializers
from .models import Broadcast
from like.models import Likes


class BroadcastSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id =serializers.ReadOnlyField(source='owner.bio.id')
    profile_image = serializers.ReadOnlyField(source='owner.broadcast.image.url')
    like_id = serializers.SerializerMethodField()

    comments_count= serializers.ReadOnlyField()
    likes_count=serializers.ReadOnlyField()

    """
    Set the size of the image.
    """
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Size of image  should not be larger that 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'The size of image is larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height is larger than 4096px'
            )
        
    def get_is_owner(self,obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_like_id(self,obj):
        """
        Get current user from context and check if the user is authenticated.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like= Likes.objects.filter(
                owner=user, broadcast=obj
            ).first()
            return like.id if like else None
        return None
    
    class Meta:
        model= Broadcast
        fields = [
             'id','owner','created_at','updated_at','title','is_owner','content', 'image','image_filter','profile_image','like_id','comments_count','likes_count','profile_id'
        ]
    
