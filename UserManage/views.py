from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def account(request):
    print(request.GET.get('username'))
    res = {
        "status": "ok"
    }
    return JsonResponse(res)


@csrf_exempt
def current_user(request):
    return HttpResponse("admin")
