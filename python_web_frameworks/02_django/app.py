import sys
import os
from django.conf import settings
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.core.management import execute_from_command_line

# Django 示例：
# - "Batteries-included" (内置电池) 理念
# - 包含 ORM, 管理后台, 认证系统等
# - 适合大型、复杂的 Web 应用

# 最小化配置
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='secretkey',
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],
    )

def hello_world(request):
    return HttpResponse("Hello, Django Training!")

def get_info(request):
    return JsonResponse({
        "framework": "Django",
        "type": "Full-stack framework",
        "description": "Powerful and robust"
    })

urlpatterns = [
    path('', hello_world),
    path('api/info', get_info),
]

if __name__ == '__main__':
    execute_from_command_line([sys.argv[0], 'runserver', '8000'])
