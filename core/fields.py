from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import CharField


class PasswordField(CharField):
    """Passwotd Fields"""
    def __init__(self, **kwargs):
        # Show password in closed type in admim
        kwargs['style'] = {'input_type': 'password'}
        kwargs.setdefault('write_only', True)

        super().__init__(**kwargs)
        # add django password validator
        self.validators.append(validate_password)
