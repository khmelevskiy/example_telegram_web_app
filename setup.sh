#!/bin/bash

./requirements/install_requirements.sh

#django-admin startproject example_telegram_web_app # for init project
#cd example_telegram_web_app && python manage.py startapp telegram_web_app # for init app


# Function to generate secret key
generate_secret_key() {
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
}

# Generating new secret key
NEW_SECRET_KEY=$(generate_secret_key)

# Updating DJANGO_SECRET_KEY in .env file
if grep -q "^DJANGO_SECRET_KEY=" .env; then
  sed -i '' "s/^DJANGO_SECRET_KEY=.*/DJANGO_SECRET_KEY=${NEW_SECRET_KEY}/" .env
else
  echo "DJANGO_SECRET_KEY=${NEW_SECRET_KEY}" >> .env
fi

echo "SECRET_KEY successfully updated in .env file"


cd example_telegram_web_app && python manage.py makemigrations && python manage.py migrate

# ask need create superuser or not
read -p "Do you want to create superuser? (y/n): "
if [ "$REPLY" != "y" ]; then
  exit 0
fi
python manage.py createsuperuser