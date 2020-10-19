from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temp/', views.temp, name='temp'),
    path('list/', views.list, name='list'),
    path('iftag/', views.iftag, name='iftag'),
    path('filter/', views.filter, name='filter'),
    path('get/', views.get, name='get'),
    path('groupby/', views.groupby, name='groupby'),
    path('review/', views.review, name='review'),

    path('root_param/<int:id>', views.root_param, name='root_param'),
    re_path('^root_param/(?P<id>[0-9]{2,3})$', views.root_param, name='root_param'),

    path('req_header/', views.req_header, name='req_header'),
    path('req_redirect/', views.req_redirect, name='req_redirect'),

    path('res_notfound/', views.res_notfound, name='res_notfound'),
    path('res_header/', views.res_header, name='res_header'),
    path('res_csv/', views.res_csv, name='res_csv'),
    path('res_json/', views.res_json, name='res_json'),
    path('setcookie/', views.setcookie, name='setcookie'),
    path('getcookie/', views.getcookie, name='getcookie'),

    path('setsesson/', views.setsesson, name='setsesson'),
    path('getsesson/', views.getsesson, name='getsesson'),

    path('temp_view/', views.MyTempView.as_view(), name='temp_view'),

    path('form_input/', views.form_input, name='form_input'),
    path('form_process/', views.form_process, name='form_process'),

    path('crud_new/', views.crud_new, name='crud_new'),
]