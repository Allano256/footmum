from rest_framework import serializers
from .models import Bio


class BioSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # is_owner = serializers.SerializerMethodField()
    # following_id =serializers.SerializerMethodField()

    # posts_count = serializers.ReadOnlyField()
    # followers_count = serializers.ReadOnlyField()
    # following_count = serializers.ReadOnlyField()


    def get_owner(self, obj):
        request =self.context['request']
        return request.user == obj.owner
    
    # def get_following_id(self,obj):
    #     """
    #     This will show who the person is following.
    #     """
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         following= 

    class Meta:
        model=Bio
        fields =[
            'id','owner','created_at','updated_at','user_name','content','image',
        ]