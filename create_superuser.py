import os

# TODO: Позже прикрутить данный скрипт

from django.contrib.auth.management.commands.createsuperuser import \
    Command as createsuperuser
from django.core.management import call_command
from dotenv import load_dotenv

load_dotenv(override=True)

# Параметры для создания super пользователя
username = os.environ.get("SUPERUSER_NAME")
email = os.environ.get("SUPERUSER_EMAIL")
password = os.environ.get("SUPERUSER_PASSWORD")

# Вызов команды createsuperuser с параметрами
call_command('createsuperuser', interactive=False,
             username=username, email=email)

# Обновление пароля созданного пользователя
user = createsuperuser.UserModel.objects.get(username=username)
user.set_password(password)
user.save()
