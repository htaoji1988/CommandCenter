"""bill99cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from UserManage import views as user_view

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/login/account', user_view.account, name='account'),
    path('api/login/outLogin', user_view.out_login, name='outLogin'),
    path('api/currentUser', user_view.current_user, name='currentUser'),
    path('api/user/', include('UserManage.urls')),
]
