"""StockDash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from Stock import views

urlpatterns = [
    # http://127.0.0.1:8000/admin/ 匹配
    # 正则匹配，对请求地址进行正则匹配，如果路径中包含admin，就把后台站点中的url信息包含到这个项目中，指明下一集路径如何匹配
    path('admin/', admin.site.urls),
    # 正则匹配，对请求地址进行正则匹配，如果路径中不包含admin，就把Book中的url信息包含到这个项目中，指明下一集路径如何匹配
    path('', include('Stock.urls')),
]
