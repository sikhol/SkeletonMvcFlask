from app.main.models.user import UserModel
from app.main.models.blacklist import BlacklistToken
from flask_restplus import Resource,reqparse,fields, marshal, marshal_with
from .response_helper import ResponseHelper
from .jwt_helper import JwtHelper


class Auth:

    @staticmethod
    def login_user(data):

        try:
            user = UserModel.query.filter_by(username=data.get('username')).first()
            if user and user.check_password(data.get('password')):
                auth_token = JwtHelper.encode_auth_token(user.id)
                if auth_token:
                    return ResponseHelper.success_custom_with_data('Successfully logged in.', auth_token)
                else:
                    return ResponseHelper.error_custom(500, 'Generate token failed.')
            else:
                return ResponseHelper.error_custom(401, 'username or password does not match.')

        except Exception as e:
            print(e)
            return ResponseHelper.error_custom(500, 'Try again')

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")
        else:
            auth_token = ''

        if len(auth_token) == 2:
            resp = JwtHelper.decode_auth_token(auth_token[1])
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return BlacklistToken.save_token(token=auth_token[1])
            else:
                return ResponseHelper.error_custom(401, resp)
        else:
            return ResponseHelper.error_custom(401,'Provide a valid auth token.')

    @staticmethod
    def get_user(new_request):
        # get the auth token
        header_authorization = new_request.headers.get('Authorization')

        if header_authorization is None:
            return ResponseHelper.error_custom(401, 'Provide a valid auth token.')

        auth_token = header_authorization.split(" ")
        if len(auth_token) == 2:
            resp = JwtHelper.decode_auth_token(auth_token[1])
            if not isinstance(resp, str):
                user = UserModel.query.filter_by(id=resp).first()

                if not user:
                    return ResponseHelper.error_custom(204, 'Data user not found.')
                return ResponseHelper.success_with_data(marshal(user,UserModel.user_fields()))
            return ResponseHelper.error_custom(401, resp)
        else:
            return ResponseHelper.error_custom(401,'Provide a valid auth token.')
