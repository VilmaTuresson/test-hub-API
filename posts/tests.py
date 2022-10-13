from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTest(APITestCase):
    """
    Class for testing post list view
    """
    def setUp(self):
        User.objects.create_user(username='testAdmin', password='pass')
        
    def test_can_list_posts(self):
        """
        Test for listing posts
        """
        testAdmin = User.objects.get(username='testAdmin')
        Post.objects.create(owner=testAdmin, title='something')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

