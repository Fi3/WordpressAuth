import importlib
from django.conf import settings
from django.contrib.auth.models import User
from .WordpressAPI import WordpressAPI
import WordpressAuth.AuthenticationMethods as AuthenticationMethods
from django.conf import settings

class AuthBackEnd:
    """
    """

    def authenticate(self, username=None, password=None):
        """
        Check the username and password and return an user
        """
        authMethod = getattr(AuthenticationMethods, settings.WORDPRESS_AUTHENTICATION_METHOD)
        wpApi = WordpressAPI(settings.WORDPRESS_URL, username, password,
                             settings.WORDPRESS_ADMNIN_USER,
                             settings.WORDPRESS_ADMIN_PASSWORD,
                             settings.WORDPRESS_SESSION_MANAGER,
                             authMethod)
        if wpApi.isAuthenticated():
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                password = User.objects.make_random_password()
                user = User(username=username)
                user.is_staff = False
                user.is_superuser = False
                user.set_password(password)
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
