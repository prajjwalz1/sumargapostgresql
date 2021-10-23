from django.urls import path,re_path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('',views.index,name='index'),
    # path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path("article/<int:myid>",views.article,name='article')


]