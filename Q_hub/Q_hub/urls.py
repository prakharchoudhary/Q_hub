"""Q_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'index.html'}),
    url(r'^main/$', views.main, name='main'),
    url(r'^select/$', views.select, name='select'),
    url(r'^add_ques/$', views.add_ques, name='add_ques'),
    url(r'^view_all/$', views.view_all, name='view_all'),
    url(r'^logout/$', views.logout_page, name='logout'),
]
