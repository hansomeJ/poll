from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'index/',views.index,name='index'),
    url(r'add/',views.add,name='add'),
    url(r'vote/(?P<q_id>\d+)/',views.vote,name='vote'),
    url(r'detail/(?P<q_id>\d+)/',views.detail,name='detail'),
    url(r'reg/',views.reg,name='reg'),
    url(r'login/',views.login,name='login'),
    url(r'logout/',views.logout,name='logout'),
    url(r'reset/',views.reset,name='reset'),
    url(r'active/(.*?)/',views.active,name='reset'),
]