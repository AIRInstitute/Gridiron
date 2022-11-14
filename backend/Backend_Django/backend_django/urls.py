"""backend_django URL Configuration

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

#Django
from django.contrib import admin
from django.urls import path

from backend_django import views as local_views
from entities import views as entities_views
from keyrock import views as keyrock_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world', local_views.hello_world),
    path('hi', local_views.hi),
    path('entities', entities_views.get_entities),
    path('get_entity_by_id', entities_views.get_entity_by_id),
    path('get_complete_entity_by_id', entities_views.get_complete_entity_by_id),
    path('get_image_without_liquid', entities_views.get_image_without_liquid),
    path('get_image_with_liquid', entities_views.get_image_with_liquid),
    path('execute_first_protocol', entities_views.execute_first_protocol),
    path('execute_second_protocol', entities_views.execute_second_protocol),
    path('execute_third_protocol', entities_views.execute_third_protocol),
    path('execute_fourth_protocol', entities_views.execute_fourth_protocol),
    path('execute_fifth_protocol', entities_views.execute_fifth_protocol),
    path('get_token', keyrock_views.get_token),
    path('get_token_oauth', keyrock_views.get_token_oauth),
    path('create_user', keyrock_views.create_user),
    path('list_users', keyrock_views.list_users),
    path('delete_users', keyrock_views.delete_users),
    path('get_user_info', keyrock_views.get_user_info),
    path('update_user', keyrock_views.update_user),
    path('testActuator', local_views.testActuator),
]
