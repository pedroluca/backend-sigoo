from django.contrib.auth.backends import ModelBackend
from .models import Usuario

class UsuarioBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        try:
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            try:
                user = Usuario.objects.get(email=username)
            except Usuario.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None