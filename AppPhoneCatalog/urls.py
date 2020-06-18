

from django.conf.urls import url,re_path
from . import views

app_name ='AppPhoneCatalog'
urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.Register.as_view()),
    url (r'^logIn/$', views.LogIn.as_view()),
    url (r'^logout/$', views.Logout.as_view()),
    url (r'^passwordChange/$', views.PasswordChange.as_view()),
    url(r'^post/$', views.post, name='post'),
    url(r'^msg_list/$', views.msg_list, name='msg_list'),
    re_path(r'^admin/$', views.admin, name='admin'),
    re_path(r'^post_Inform/$', views.postInform, name='postInform'),
    re_path(r'^subscribe/$', views.SubscribeView.as_view(), name='subscribeview'),
    re_path(r'^unsubscribe/$', views.unsubscribe, name='unsubscribe'),
]