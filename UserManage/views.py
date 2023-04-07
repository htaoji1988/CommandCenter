from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from UserManage.models import User, RoleList, UserManager
import json
import logging
import datetime


# Create your views here.


@csrf_exempt
def account(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    type = request.POST.get('type')

    res = {
        "status": 'ok',
        "type": 'account',
        "currentAuthority": 'admin'
    }

    return JsonResponse(res)


@csrf_exempt
def out_login(request):
    res = {
        "data": {},
        "success": True
    }

    return JsonResponse(res)


def current_user(request):
    res = {
        "success": True,
        'data': {
            'name': 'Serati Ma',
            'avatar': 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
            'userid': '00000001',
            'email': 'antdesign@alipay.com',
            'signature': '海纳百川，有容乃大',
            'title': '交互专家',
            'group': '蚂蚁金服－某某某事业群－某某平台部－某某技术部－UED',
            'tags': [
                {
                    'key': '0',
                    'label': '很有想法的',
                },
                {
                    'key': '1',
                    'label': '专注设计',
                },
                {
                    'key': '2',
                    'label': '辣~',
                },
                {
                    'key': '3',
                    'label': '大长腿',
                },
                {
                    'key': '4',
                    'label': '川妹子',
                },
                {
                    'key': '5',
                    'label': '海纳百川',
                },

            ],
            'notifyCount': 12,
            'unreadCount': 11,
            'country': 'China',
            'access': 'admin',
            'geographic': {
                'province': {
                    'label': '浙江省',
                    'key': '330000',
                },
                'city': {
                    'label': '杭州市',
                    'key': '330100',
                },
            },
            'address': '西湖区工专路 77 号',
            'phone': '0752-268888888',
        }
    }
    return JsonResponse(res)


@csrf_exempt
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
    if is_active == "true":
        kwargs['is_active'] = True
    elif is_active == "false":
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
        email = body.get('mail').strip()
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
                'log': e
            }

        return JsonResponse(result)


@csrf_exempt
def roles(request):
    objs = RoleList.objects.all().values('id', 'name')

    res = {}
    for o in objs:
        res[o['name']] = {"text": o['name']}

    return JsonResponse(res)
