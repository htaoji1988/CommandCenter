from website import settings
import jwt
from django.http import HttpResponse
import json
from UserManage.models import User


# 校验结果封装
def response_failure(message):
    return HttpResponse(json.dumps({
        'code': 4000,
        'message': message
    }, ensure_ascii=False), 'application/json')


# 登入凭证装饰器
def token_required():
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            try:
                auth = request.META.get('HTTP_AUTHORIZATION').split()
            except AttributeError:
                return response_failure("No authenticate header")

            if auth[0].lower() == 'jwt':
                try:
                    dict = jwt.decode(auth[1], settings.SECRET_KEY, algorithms=['HS256'])
                    username = dict.get('data').get('name')
                except jwt.ExpiredSignatureError:
                    return response_failure("Token expired")
                except jwt.InvalidTokenError:
                    return response_failure("Invalid token")
                except Exception as e:
                    return response_failure("Can not get user object")

                try:
                    user = User.objects.get(username=username)
                    request.user = user
                except User.DoesNotExist:
                    return response_failure("User Does not exist")

                return view_func(request, *args, **kwargs)
            else:
                return response_failure("Error authenticate header")

        return _wrapped_view

    return decorator
