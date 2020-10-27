from users.models import Profile
from django.test import TestCase
from rest_framework.test import APIClient,APITestCase
from .serializers import ProfileSerializer
from rest_framework.views import status
from django.urls import reverse

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_profile(
                    user="",
                    bio="",
                    image="",
                   ):
        if user != "" and bio != "" and image != "" :
            Profile.objects.create.objects(user=user,bio=bio,image=image)

    def setUp(self):
        self.submit_site('Mabel', 'Keep life simple',
                           'cloudlink.field',
                        )


class GetProjectTest(BaseViewTest):
    def test_get_project(self):
        """
        This test ensure that all songs added in the setUp method
        exist when we make a GET request to the project/endpoint
        """
        response = self.client.get(
            reverse('Projects', kwargs={'version': 'v1'}))

        # fetch the data from db
        expected = Profile.objects.all()
        serialized = ProfileSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
