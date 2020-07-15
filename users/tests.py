from django.test import TestCase
from django.contrib.auth.models import User

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'admin',
            'password': 'admin'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/users/login/', self.credentials, follow=True)
        print(response.context)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
