"""django_app URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

import bithumb
import crawl
import kakao
from kakao import views
from crawl import views
from bithumb import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^keyboard/', kakao.views.keyboard),
    url(r'^message', kakao.views.message),
    url(r'^crawl', crawl.views.crawl),
    url(r'^korbit', crawl.views.korbit_api),
    url(r'^api', bithumb.views.user_transactions)
]
