from django.test import TestCase
from .models import List, Card
from django.contrib.auth.models import User
from django.urls import reverse

class CreateFieldsForTest:
    def user_create(self, id = 123, username = "user"):
        return User.objects.create(id = "123", username = "user")

    def list_create(self, id = "123", name = "test list", user_id = "123"):
        return List.objects.create(id = id, name = name, user_id = user_id)

    def card_create(self, id = "123", name = "card test", list_id = "123"):
        return Card.objects.create(id = id, name = name, list_id = list_id)

class ListTest(TestCase):
    def test_list_creation(self):
        CreateFieldsForTest.user_create(self)
        list = CreateFieldsForTest.list_create(self)
        self.assertTrue(isinstance(list, List))
        self.assertEqual(list.__str__(), list.name)

class CardTest(TestCase):
    def test_card_creation(self):
        CreateFieldsForTest.user_create(self)
        list = CreateFieldsForTest.list_create(self)
        card = CreateFieldsForTest.card_create(self)
        self.assertTrue(isinstance(card, Card))
        self.assertEqual(card.__str__(), card.name)
