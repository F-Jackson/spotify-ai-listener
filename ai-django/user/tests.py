from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase, runner
from .serializers import UserSerializer


class UserSerializerValidation(TestCase):
    def setUp(self) -> None:
        valid_data = {'username': 'jacks', 'password': '123', 'email': 'testevalid@email.com'}
        User.objects.create_user(valid_data)

    def test_username_is_valid(self) -> None:
        valid_data = {'username': 'exist', 'password': '123', 'email': 'testevalid@email.com'}
        user_valid = UserSerializer(data=valid_data)
        self.assertEqual(user_valid.is_valid(), True)

    def test_username_not_valid(self) -> None:
        invalid_data = {'username': 'jacks', 'password': '123', 'email': 'testevalid@email.com'}
        user_invalid = UserSerializer(data=invalid_data)
        self.assertEqual(user_invalid.is_valid(), False)
