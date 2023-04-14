from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.utils import timezone
from django.db.models import Q
import jwt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from UserManage.models import User, RoleList, UserManager, PermissionList
from UserManage.check import token_required
import json
import logging
import datetime


# Create your views here.


@csrf_exempt
def account(request):
    logger = logging.getLogger('user_manage')
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    logger.info(f'user login!\n{body}')
    username = body.get('username')
    password = body.get('password')
    user = authenticate(username=username, password=password)

    if user and user.is_authenticated:
        res = {
            "status": 'ok',
            "type": 'account',
            "currentAuthority": username,
            "token": user.token,
            "email": user.email,
            "role": User.objects.get(username=username).role.name.lower()
        }
        return JsonResponse(res)

    res = {
        "status": 'not ok',
        "type": 'account',
        "currentAuthority": username,
        "token": '',
        "email": '',
        "role": ''
    }
    return JsonResponse(res)


@csrf_exempt
def out_login(request):
    res = {
        "data": {},
        "success": True
    }

    return JsonResponse(res)


@csrf_exempt
@token_required()
def current_user(request):
    res = {
        "success": True,
        'data': {
            'name': request.user.username,
            'avatar': '/User.png',
            'userid': request.user.id,
            'email': request.user.email,
            'signature': '',
            'title': '',
            'group': '',
            'tags': [
            ],
            'notifyCount': 12,
            'unreadCount': 11,
            'country': 'China',
            'access': request.user.role.name,
            'geographic': {
            },
            'address': '',
            'phone': '',
        }
    }

    return JsonResponse(res)


@csrf_exempt
@token_required()
def list_user(request):
    logger = logging.getLogger('user_manage')
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    logger.info(body)

    username = body.get('username')
    nickname = body.get('nickname')
    role__name = body.get('role__name')
    is_active = body.get('is_active')

    kwargs = {}
    if username:
        kwargs['username__contains'] = username.strip()
    if nickname:
        kwargs['nickname__contains'] = nickname.strip()
    if role__name and role__name != 'all':
        kwargs['role__name'] = role__name.strip()
    if is_active == 'true':
        kwargs['is_active'] = True
    elif is_active == 'false':
        kwargs['is_active'] = False

    objs = User.objects.filter(**kwargs).values('id', 'username', 'email', 'is_active', 'nickname', 'role__name',
                                                'last_login')

    res = {'data': list(objs)}

    return JsonResponse(res)


@csrf_exempt
def add_user(request):
    logger = logging.getLogger('user_manage')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        del body['id']
        logger.info(f'add user!\n{body}')
        username = body.get('username').strip()
        email = body.get('email').strip()
        password = body.get('password').strip()
        nickname = body.get('nickname', '').strip()
        role_id = RoleList.objects.filter(name=body.get('role')).first().id
        exsit = User.objects.filter(username=username)
        if not exsit:
            try:
                new_user = User.objects.create(username=username, email=email, role_id=role_id, nickname=nickname)
                new_user.set_password(password)
                new_user.save()
            except Exception as e:
                result = {
                    'success': 'False',
                    'log': f'{e}'
                }
                return JsonResponse(result)
        else:
            result = {
                'success': 'False',
                'log': "用户已存在!"
            }
            return JsonResponse(result)

    result = {
        'success': 'True',
        'log': ''
    }

    return JsonResponse(result)


@csrf_exempt
def del_user(request):
    logger = logging.getLogger('user_manage')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info(f'del user!\n{body}')
        id = body.get('id')
        try:
            User.objects.filter(id=id).delete()
            result = {
                'success': 'True',
                'log': ''
            }
        except Exception as e:
            result = {
                'success': 'False',
                'log': f'{e}'
            }

        return JsonResponse(result)


@csrf_exempt
def update_user(request):
    logger = logging.getLogger('user_manage')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info(f'update user!\n{body}')
        id = body.get('id')
        username = body.get('username', '').strip()
        password = body.get('password', '').strip()
        status = body.get('status')
        role_id = RoleList.objects.filter(name=body.get('role')).first().id
        if status == '启用':
            body['is_active'] = True
        else:
            body['is_active'] = False

        del body['status']
        del body['role']
        del body['password']

        exsit = User.objects.exclude(id=id).filter(username=username)
        if not exsit:
            try:
                user = User.objects.filter(id=id).update(**body, role_id=role_id)
                if password:
                    user.set_password(password)
            except Exception as e:
                result = {
                    'success': 'False',
                    'log': f'{e}'
                }
                return JsonResponse(result)
        else:
            result = {
                'success': 'False',
                'log': "更新失败用户名已存在!"
            }
            return JsonResponse(result)

    result = {
        'success': 'True',
        'log': ''
    }

    return JsonResponse(result)


@csrf_exempt
def roles(request):
    objs = RoleList.objects.all().values('id', 'name')

    res = {}
    for o in objs:
        res[o['name']] = {"text": o['name']}

    return JsonResponse(res)


@csrf_exempt
@token_required()
def role_list(request):
    logger = logging.getLogger('user_manage')
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    logger.info(body)
    role_name = body.get('name', '').strip()

    kwargs = {}
    if role_name:
        kwargs['name__contains'] = role_name

    objs = RoleList.objects.filter(**kwargs).values('id', 'name')

    res = {'data': list(objs)}

    return JsonResponse(res)


@csrf_exempt
def add_role(request):
    logger = logging.getLogger('user_manage')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        del body['id']
        logger.info(f'add role!\n{body}')
        role_name = body.get('name').strip()

        exsit = RoleList.objects.filter(name=role_name)
        if not exsit:
            try:
                new_user = RoleList.objects.create(name=role_name)
            except Exception as e:
                result = {
                    'success': 'False',
                    'log': f'{e}'
                }
                return JsonResponse(result)
        else:
            result = {
                'success': 'False',
                'log': "角色已存在!"
            }
            return JsonResponse(result)

    result = {
        'success': 'True',
        'log': ''
    }

    return JsonResponse(result)


@csrf_exempt
def del_role(request):
    logger = logging.getLogger('user_manage')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info(f'del role!\n{body}')
        id = body.get('id')
        try:
            RoleList.objects.filter(id=id).delete()
            result = {
                'success': 'True',
                'log': ''
            }
        except Exception as e:
            result = {
                'success': 'False',
                'log': f'{e}'
            }

        return JsonResponse(result)


@csrf_exempt
@token_required()
def permissions(request):
    logger = logging.getLogger('user_manage')
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    logger.info(body)
    name = body.get('name', '').strip()
    url = body.get('url', '').strip()

    kwargs = {}
    if name:
        kwargs['name__contains'] = name
    if url:
        kwargs['url__contains'] = url

    objs = PermissionList.objects.filter(**kwargs).values('id', 'name', 'url')

    res = {'data': list(objs)}

    return JsonResponse(res)


@csrf_exempt
def add_permission(request):
    logger = logging.getLogger('user_manage')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        del body['id']
        logger.info(f'add permission!\n{body}')
        name = body.get('name').strip()
        url = body.get('url').strip()

        exsit = PermissionList.objects.filter(Q(name=name) | Q(url=url))
        if not exsit:
            try:
                permission = PermissionList.objects.create(name=name, url=url)
            except Exception as e:
                result = {
                    'success': 'False',
                    'log': f'{e}'
                }
                return JsonResponse(result)
        else:
            result = {
                'success': 'False',
                'log': "名称或者url已经存在不能重复添加!"
            }
            return JsonResponse(result)

    result = {
        'success': 'True',
        'log': ''
    }

    return JsonResponse(result)


@csrf_exempt
def del_permission(request):
    logger = logging.getLogger('user_manage')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info(f'del permission!\n{body}')
        id = body.get('id')
        try:
            PermissionList.objects.filter(id=id).delete()
            result = {
                'success': 'True',
                'log': ''
            }
        except Exception as e:
            result = {
                'success': 'False',
                'log': f'{e}'
            }

        return JsonResponse(result)


@csrf_exempt
def update_permission(request):
    logger = logging.getLogger('user_manage')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info(f'update permission!\n{body}')
        id = body.get('id')
        name = body.get('name').strip()
        url = body.get('url').strip()

        exsit = PermissionList.objects.exclude(id=id).filter(Q(name=name) | Q(url=url))
        if not exsit:
            try:
                permission = PermissionList.objects.filter(id=id).update(name=name, url=url)
            except Exception as e:
                result = {
                    'success': 'False',
                    'log': f'{e}'
                }
                return JsonResponse(result)
        else:
            result = {
                'success': 'False',
                'log': "更新失败名称或者url已经存在!"
            }
            return JsonResponse(result)

    result = {
        'success': 'True',
        'log': ''
    }

    return JsonResponse(result)
