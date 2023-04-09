"""website URL Configuration

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

from django.urls import path
from UserManage import views

urlpatterns = [
    path('userinfo', views.list_user, name='userinfo'),
    path('del_user', views.del_user, name='del_user'),
    path('add_user', views.add_user, name='add_user'),
    path('update_user', views.update_user, name='update_user'),
    path('roles', views.roles, name='roles'),
    path('role_list', views.role_list, name='role_list'),
    path('del_role', views.del_role, name='del_role'),
    path('add_role', views.add_role, name='add_role'),
    path('permissions', views.permissions, name='permissions'),
    path('del_permission', views.del_permission, name='del_permission'),
    path('add_permission', views.add_permission, name='add_permission'),
    path('update_permission', views.update_permission, name='update_permission'),
]
