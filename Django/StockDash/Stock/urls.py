from django.urls import path, re_path
from . import views

# 这是应用Book中的url具体配置，请求到这里才能调用该应用的视图，上一级首先是调用BookManager的url，如果没有匹配admin
# 那么进入应用的匹配Book.urls，之后才会进入这里应用的url

urlpatterns = [
    # http://127.0.0.1:8000/admin/ 匹配
    # 正则匹配，对请求地址进行正则匹配，如果路径中包含admin，就把后台站点中的url信息包含到这个项目中，指明下一集路径如何匹配
    # 如果匹配成功，那么直接调用指定的视图
    # 正则匹配，对请求地址进行正则匹配，如果路径中不包含admin，就把Book中的url信息包含到这个项目中，指明下一集路径如何匹配
    path('stockplot/', views.showlinediagram),
    path('index3', views.index3,name='index3'),
    path('json1', views.json1),
    # ex:/assetinfo/json2
    path('json2', views.json2),
    path('ajax_add/', views.ajax_add),
    path('ajax_demo1/', views.ajax_demo1),
    path('data_fresh/', views.data_fresh, name="data_fresh"),
    path('stocklist/', views.stockList),  # 这里的^表示开始，$表示结束，因为是正则表达式，所以必须严格
    re_path(r'^([1-9]\d*)/$', views.dashBoard_m)  # 调函数的时候传参数,采用正则的组，正则匹配加括号，然后传进去参数,按照顺序传
    # 这里的地址最重要，代表了访问的url地址后面
]