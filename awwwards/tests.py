from django.http import response
from django.test import TestCase
from .models  import Project,Review
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
from rest_framework.views import status
from .serializers import ProjectSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()
    
    @staticmethod
    def submit_site(title="",description="",date_posted="",author="",project_image="",link="",country=""):
        if title != "" and description != "" and date_posted != "" and author != "" and project_image != "" and link != "" and country !="":
            Project.objects.create(title=title, description=description,date_posted=date_posted,author=author,project_image=project_image,link=link,country=country)
    
    
    def setUp(self):
        self.submit_site('portfolio','This a portfolio website','25 october 2020','mabel','http://123ncsjcb.jpg','http://hwnjbcc123.com','mexico')

class GetProjectTest(BaseViewTest):
    
    def test_get_project(self):
        """
        This test ensure that all songs added in the setUp method
        exist when we make a GET request to the project/endpoint
        """
        response = self.client.get(
            reverse('Projects',kwargs={'version':'v1'})
        )
        
        # fetch the data from db 
        expected = Project.objects.all()
        serialized = ProjectSerializer(expected,many=True)
        self.assertEqual(response.data,serialized.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)