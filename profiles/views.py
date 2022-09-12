from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(APIView):
    """
    Profile view
    """
    def get(self, request):
        """
        Profile view get for profiles
        """
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    Profile details view
    """
    serializer_class = ProfileSerializer

    def get_object(self, pk):
        """
        Function to get profile details or 404 and serialize data
        """
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Serialize data
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)