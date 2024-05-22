from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
import os

class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'

    def ready(self):
        if not firebase_admin._apps:
            cred_path = os.path.join(os.path.dirname(
                __file__), 'serviceAccountKey.json')
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
