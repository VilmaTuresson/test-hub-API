from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Class for likes serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Like serializer meta class
        """
        model = Like
        fields = ['id', 'owner', 'post']
