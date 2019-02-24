import os

from reverie.settings.base import * # noqa

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

# Databases
DATABASES = {
  'default': {
    'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
    'NAME': 'sqlite.db',
    'BUCKET': 'db.reverie.devenney.io'
  }
}

# Storages
AWS_STORAGE_BUCKET_NAME = 'cdn.reverie.devenney.io'
AWS_S3_CUSTOM_DOMAIN = 'cdn.reverie.devenney.io'
AWS_LOCATION = 'static'
STATIC_URL = 'https://{0}/{1}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
