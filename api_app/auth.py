import firebase_admin
from firebase_admin import auth
from .models import User  # Import your custom user model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        auth_parts = auth_header.split()

        if len(auth_parts) != 2 or auth_parts[0].lower() != 'bearer':
            return None

        id_token = auth_parts[1]

        try:
            decoded_token = auth.verify_id_token(id_token)
            user_id = decoded_token['uid']
            user_record = auth.get_user(user_id)
            
            custom_user, created = User.objects.get_or_create(
                firebase_id=user_id)

            return (custom_user, None)
        except Exception as e:
            raise AuthenticationFailed(
                'Authentication failed: {}'.format(str(e)))

    def authenticate_header(self, request):
        return 'Bearer'
