from rest_framework import generics, permissions
from testhub_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    View for listing followers
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    View to retrieve and delete a follower
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
