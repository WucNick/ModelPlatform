from django.urls import path

# 函数导入
from model.views import listorders, listorders1

urlpatterns = [
    # 模型管理路由
    path('1', listorders),

    path('2', listorders1)
]