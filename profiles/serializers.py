from rest_framework import serializers 
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    follow_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Function to check profile ownership
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_follow_id(self, obj):
        """
        Function for getting followers
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        """
        Profile serializer meta class
        """
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'username',
            'profile_img', 'is_owner', 'follow_id', 'posts_count',
            'followers_count', 'following_count'
        ]