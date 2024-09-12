from rest_framework import serializers
from .models import Bio
from follower.models import Follower


class BioSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    broadcast_count=serializers.ReadOnlyField()
    followers_count =serializers.ReadOnlyField()
    following_count= serializers.ReadOnlyField()

  

    def get_is_owner(self, obj):
        request =self.context['request']
        return request.user == obj.owner
    
    def get_following_id(self,obj):
        """
        This will show who the person is following.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following= Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None
    
     

    class Meta:
        model=Bio
        fields =[
            'id','owner','created_at','updated_at','user_name','content','image','is_owner','following_id','broadcast_count','followers_count','following_count',
        ]