from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .Serializers import PostSerializer


class PostList(APIView):
    """
    View for list of posts
    """
    def get(self, request):
        """
        function 
        """
        posts = Post.object.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)