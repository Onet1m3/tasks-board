from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from apps.tasks.models import TaskCardModel


class TasksModelViewSetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = TaskCardModel.objects.create(title='Test Task', description='Test Description')

    def test_get_queryset(self):
        url = reverse('taskcardmodel-list')
        self.client.force_authenticate(user=self.task.user)

        response = self.client.get(url, {'ordering': 'desc'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['created_at'], 'created_at')

    def test_create_task(self):
        url = reverse('taskcardmodel-list')
        self.client.force_authenticate(user=self.user)
        data = {"title": "New Task", "description": "New Description"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Task")
        self.assertEqual(response.data['description'], "New Description")

    def test_retrieve_task(self):
        url = reverse('taskcardmodel-detail', args=[self.task.id])
        self.client.force_authenticate(user=self.task.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        url = reverse('taskcardmodel-detail', args=[self.task.id])
        self.client.force_authenticate(user=self.task.user)
        data = {"title": "Updated Task", "description": "Updated Description"}

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Task")
        self.assertEqual(response.data['description'], "Updated Description")

    def test_add_comment(self):
        url = reverse('taskcardmodel-add-comment', args=[self.task.id])
        self.client.force_authenticate(user=self.user)
        data = {"description": "New Comment"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_change_task_executor(self):
        url = reverse('taskcardmodel-change-task-executor', args=[self.task.id])
        self.client.force_authenticate(user=self.user)
        data = {"user_id": 1}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
