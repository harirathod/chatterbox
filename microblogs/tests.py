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

        self.user2 = User.objects.create_user(
            '@personTwo',
            first_name='human',
            last_name='two',
            email='personTwo@example.org',
            password='PasswordPersonTwo',
            bio="Person Two's Bio."
        )

    def test_valid_user(self):
        self._assert_user_is_valid(self.user)
        self._assert_user_is_valid(self.user2)

    # --- Username testing ---

    def test_username_not_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid(self.user)

    def test_password_not_blank(self):
        self.user.password = ""
        self._assert_user_is_invalid(self.user)

    def test_username_can_be_30_chars(self):
        """We don't want usernames to have a length longer than 30 characters, as there are not very recognisable / rememberable.."""
        self.user.username = "@" + "a" * 29
        self._assert_user_is_valid(self.user)

    def test_username_cannot_be_over_30_chars(self):
        """We don't want usernames to have a length longer than 30 characters, as there are not very recognisable / rememberable.."""
        self.user.username = "@" + "a" * 30
        self._assert_user_is_invalid(self.user)

    def test_username_must_be_unique(self):
        self.user2.username = "@personTwo"
        self.user.username = "@personTwo"
        self._assert_user_is_invalid(self.user)

    def test_username_must_start_with_at_symbol(self):
        """We want our usernames to be like '@johnsmith'"""
        self.user.username = "personOne"
        self._assert_user_is_invalid(self.user)

        self.user.username = "@personOne"
        self._assert_user_is_valid(self.user)

    def test_username_must_contain_only_one_at_symbol(self):
        self.user.username = "@@personOne"
        self._assert_user_is_invalid(self.user)

    def test_username_may_contain_numbers(self):
        self.user.username = "@person1"
        self._assert_user_is_valid(self.user)
    
    def test_username_must_only_have_alphanumerics(self):
        self.user.username = "@p!e+r(son)O'n\"e"
        self._assert_user_is_invalid(self.user)

    # --- First Name testing ---

    def test_first_name_must_not_be_blank(self):
        self.user.first_name = ""
        self._assert_user_is_invalid(self.user)
    
    def test_first_name_may_be_a_duplicate(self):
        self.user.first_name = 'human'
        self._assert_user_is_valid(self.user)

    def test_first_name_must_not_be_over_50_chars(self):
        self.user.first_name = "a" * 50
        self._assert_user_is_valid(self.user)

        self.user.first_name = "a" * 51
        self._assert_user_is_invalid(self.user)   

    # --- Last Name testing ---

    def test_last_name_must_not_be_blank(self):
        self.user.last_name = ""
        self._assert_user_is_invalid(self.user)
    
    def test_last_name_may_be_a_duplicate(self):
        self.user.last_name = 'two'
        self._assert_user_is_valid(self.user)

    def test_last_name_must_not_be_over_50_chars(self):
        self.user.last_name = "a" * 50
        self._assert_user_is_valid(self.user)

        self.user.last_name = "a" * 51 
        self._assert_user_is_invalid(self.user)   

    # --- Email testing ----

    def test_email_must_not_be_blank(self):
        self.user.email = ""
        self._assert_user_is_invalid(self.user)

    def test_email_must_be_unique(self):
        self.user2.email = "personOne@example.org"
        self._assert_user_is_invalid(self.user2)

    def test_email_must_have_username(self):
        self.user.email = "@x.com"
        self._assert_user_is_invalid(self.user)

    def test_email_must_have_one_at_symbol(self):
        self.user.email = "x@x@.com"
        self._assert_user_is_invalid(self.user)

        self.user.email = "xx.com"
        self._assert_user_is_invalid(self.user)

    def test_email_must_have_a_domain(self):
        self.user.email = "example@.com"
        self._assert_user_is_invalid(self.user)

        self.user.email = "example@example."
        self._assert_user_is_invalid(self.user)

        self.user.email = "example@example"
        self._assert_user_is_invalid(self.user)

    def test_email_can_have_multiple_dots(self):
        self.user.email = "example@ed.ac.uk"
        self._assert_user_is_valid(self.user)

    # --- Bio testing ---

    def test_bio_may_be_blank(self):
        self.user.bio = ""
        self._assert_user_is_valid(self.user)

    def test_bio_may_be_a_duplicate(self):
        self.user2.bio = "Hi."
        self.user.bio = "Hi."
        self._assert_user_is_valid(self.user)

    def test_bio_can_be_520_chars(self):
        self.user.bio = "a" * 520
        self._assert_user_is_valid(self.user)

    def test_bio_must_not_be_over_520_chars(self):
        self.user.bio = "a" * 521
        self._assert_user_is_invalid(self.user)

    # Helper methods

    def _assert_user_is_valid(self, user: User):
        try:
            user.full_clean()
        except ValidationError as e:
            self.fail("The user used in the 'test_valid_user' test case is supposed to be valid. This error message indicates that the user was invalid.")

    def _assert_user_is_invalid(self, user: User):
        with self.assertRaises(ValidationError):
            user.full_clean()