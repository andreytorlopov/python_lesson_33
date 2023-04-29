#!/bin/bash

# Если миграции есть, то накатываем, если нет - то ничего не делаем
python manage.py migrate --check
status=$?
if [[ $status != 0 ]]; then
    python manage.py migrate
fi
exec "$@"