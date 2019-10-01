from config.database import key
from config.jwt import config_jwt
import datetime
import jwt
from app.main.models.user import UserModel
from flask_restplus import  marshal

from app.main.models.blacklist import BlacklistToken


class JwtHelper:

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        user = UserModel.query.filter_by(id=user_id).first()
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=config_jwt['expired_at']),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            auth_token = jwt.encode(
                payload,
                key,
                algorithm=config_jwt['algorithm']
            )
            return {"token": auth_token.decode(),
                    "expired_at": datetime.datetime.utcfromtimestamp(payload['exp']).strftime('%Y-%m-%d %H:%M:%S'),
                    "users":marshal(user,UserModel.user_fields())}
        except Exception as e:
            return False

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'