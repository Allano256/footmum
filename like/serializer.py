
from rest_framework import serializers
from .models import Likes
from django.db import IntegrityError


class LikesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model=Likes
        fields =[
            'id', 'owner','created_at','broadcast'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'description':'possible duplicate'
            })
