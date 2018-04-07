from django.urls import path
from login.views import  auth_view, loggedin, invalidlogin, register, res_register, logout
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
        url('login/$',auth_views.login , name ='login'),
        url('auth/$', auth_view , name = 'logout'),
        url('logout/$', logout),
        url('loggedin/$', loggedin),
        url('invalidlogin/$', invalidlogin),
         url('res_register/$',res_register),
        url('register/$',register),

        ]
