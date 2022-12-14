from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from testhub_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    """
    Profile view
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
    ]

    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

    search_fields = ['owner__username']


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Profile details view
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')