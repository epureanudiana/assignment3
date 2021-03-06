"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
"""from django.contrib import admin
from django.urls import path, include
from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 'django.contrib.auth.views.login'),
    path('home/', home),
    path('register/', register),
    path('register/success/', register_success),
    path('accounts/login/','django.contrib.auth.views.login'),
    path('logout/', logout_page),
"""
from django.conf.urls import url, include
from django.contrib import admin
from login.views import *
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login, name='login'),
    url(r'^home/$', home, name='home'),
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success, name='register_success'),
    url(r'^accounts/login/$',login, name='login'),
    url(r'^logout/$', logout_page, name='logout_page'),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
