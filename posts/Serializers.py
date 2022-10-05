from rest_framework import serializers 
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_img.url'
    )

    def get_is_owner(self, obj):
        """
        Function to check posts ownership
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Post serializer meta class
        """
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'content',
            'link', 'image', 'is_owner', 'profile_id', 'profile_image'
        ]