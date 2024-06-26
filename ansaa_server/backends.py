from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

class EmailBackend(ModelBackend):
    """Log in to Django without providing a password.
    """
    def authenticate(self, request, email):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None