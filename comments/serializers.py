from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_img = serializers.ReadOnlyField(source='owner.profile.profile_img.url')

    def get_is_owner(self, obj):
        """
        Function to check comments ownership
        """
        request = self.context.get('request', None)
        if request is not None:
            return request.user == obj.owner
        return False

    class Meta:
        """
        Comment serializer meta class
        """
        model = Comment
        fields = [
            'id', 'owner', 'created_at', 'content', 'post',
            'content', 'is_owner', 'profile_id', 'profile_img'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for comment details
    """
    post = serializers.ReadOnlyField(source='post.id')