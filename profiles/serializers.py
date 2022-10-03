from rest_framework import serializers 
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Function to check profile ownership
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Profile serializer meta class
        """
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'username',
            'profile_img', 'is_owner'
        ]