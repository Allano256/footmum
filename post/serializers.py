from rest_framework import serializers
from .models import Broadcast


class BroadcastSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # is_owner = serializers.SerializerMethodField()
    # profile_id =serializers.ReadOnlyField(source='owner.profile.id')
    # profile_image = serializers.ReadOnlyField(source='owner.post.image.url')

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
        
    def get_object(self,obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model= Broadcast
        fields = [
             'id','owner','created_at','updated_at','title','content', 'image','image_filter',
        ]
    
