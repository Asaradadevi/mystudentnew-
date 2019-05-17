from django.contrib import admin
#from django.urls import path
from django.conf.urls import include,url
from studentnew1 import views

urlpatterns = [
    #url('', views.index, name = 'index'),
    #url('add_student/', views.add_student, name = 'add_student'),
    #url(r'^$',views.index, name = 'index'),
    url(r'^$',views.add_student, name = 'add_student'),
    url('admin/', admin.site.urls,name='admin'),
]
