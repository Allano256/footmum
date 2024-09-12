from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    bio_id = serializers.ReadOnlyField(source='bio.id')
    bio_image = serializers.ReadOnlyField(source='bio.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'bio_id', 'bio_image'
        )