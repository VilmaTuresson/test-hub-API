from rest_framework import serializers 
from .models import Post
from likes.models import Like


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
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Function to check posts ownership
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Function to for getting likes
        """
        user = self.context['request'].user
        if user.is_authenticated:
            liked = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return liked.id if liked else None
        return None

    class Meta:
        """
        Post serializer meta class
        """
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'content',
            'image', 'is_owner', 'profile_id', 'profile_image',
            'like_id', 'comments_count', 'likes_count'
        ]