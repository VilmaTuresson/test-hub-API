from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        """
        Function to check comments ownership
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Comment serializer meta class
        """
        model = Comment
        fields = [
            'id', 'owner', 'created_at', 'content', 'post',
            'content', 'is_owner', 'profile_id'
        ]