from rest_framework import serializers 
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Profile serializer meta class
        """
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'username',
            'profile_img'
        ]