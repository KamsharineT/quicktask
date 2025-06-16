# tasks/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_task(self):
        data = {
            "title": "Test Task",
            "description": "This is a test",
            "due_date": "2025-06-30"
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, "Test Task")
