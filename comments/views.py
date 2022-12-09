from rest_framework import generics, permissions
from rest_framework.response import Response
from testhub_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentsList(generics.ListCreateAPIView):
    """
    View for list of comments
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        post_id = request.GET.get('post', None)
        print(post_id)
        queryset = self.get_queryset()
        if post_id is not None:
            queryset = self.get_queryset().filter(post=post_id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

class CommentDetails(generics.RetrieveDestroyAPIView):
    """
    View for retrieving and deleting comment
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
