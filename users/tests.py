from django.test import TestCase
from django.contrib.auth.models import User

class Registration(TestCase):
    def setUp(self):
        self.user = User()

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'user',
            'password': 'password'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        response = self.client.post('/users/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
