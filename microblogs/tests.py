from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError
# Unit tests go here.

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user =  User.objects.create_user(
            '@personOne',
            first_name='person',
            last_name='one',
            email='personOne@example.org',
            password='PasswordPersonOne',
            bio="Person One's Bio."
        )

    def test_valid_user(self):
        self._assert_user_is_valid(self.user)

    def test_username_not_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid(self.user)

    def test_password_not_blank(self):
        self.user.password = ""
        self._assert_user_is_invalid(self.user)

    def test_username_can_be_30_chars(self):
        """We don't want usernames to have a length longer than 30 characters, as there are not very recognisable / rememberable.."""
        self.user.username = "a" * 30
        self._assert_user_is_valid(self.user)

    def test_username_cannot_be_over_30_chars(self):
        """We don't want usernames to have a length longer than 30 characters, as there are not very recognisable / rememberable.."""
        self.user.username = "a" * 31
        self._assert_user_is_invalid(self.user)

    def _assert_user_is_valid(self, user: User):
        try:
            user.full_clean()
        except ValidationError as e:
            self.fail("The user used in the 'test_valid_user' test case is supposed to be valid. This error message indicates that the user was invalid.")

    def _assert_user_is_invalid(self, user: User):
        with self.assertRaises(ValidationError):
            user.full_clean()