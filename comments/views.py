from rest_framework import generics, permissions
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

class CommentDetails(generics.RetrieveDestroyAPIView):
    """
    View for retrieving and deleting comment
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
