"""meteorological URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app import views
from meteorological import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('data2sql/', views.data2sql, name='data2sql'),

    path('', views.daoluList.as_view(), name='index'),  # 乳腺癌列表
    path('predict/', views.predict.as_view(), name='predict'),  # 乳腺癌列表
    path('my/',views.my,name='my'),
    ################################下面可能没用的



    path('test/', views.test, name='test'),
    path('my/',views.my,name='my'),








]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
