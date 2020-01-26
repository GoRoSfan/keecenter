import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
