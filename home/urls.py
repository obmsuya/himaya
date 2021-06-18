





from django.conf.urls import url
from django.urls import path, re_path
from . import views
from home.views import HomeView

app_name='home'

urlpatterns = [

    path('', views.index),
    
    
    path('chat', HomeView.as_view(), name = 'chat'),
    
    path('home/', views.home, name = "home"),
    path('index/', views.index, name = "index"), 
 
    
    re_path(r'^item/(?P<item_id>\d+)/$', views.item, name = "item"),
    re_path(r'^item/(?P<item_id>\d+)/book/$', views.book, name = "book"),
    re_path(r'^item/(?P<item_id>\d+)/payment/$', views.payment, name = "payment"),
    re_path(r'^item/(?P<item_id>\d+)/donate/$', views.donate, name = "donate"),
    


    path('activate/', views.activate, name = "activate"),
    path('activatefriend/', views.activatefriend, name = "activatefriend"),

    path('makala/', views.makala, name = "makala"),
    path('authors/', views.authors, name = "authors"),
    

    re_path(r'^category/(?P<category_id>\d+)/$', views.category, name = "category"),

    path('hasira/', views.hasira, name = "hasira"),
    path('gis/', views.gis, name = "gis"),
    path('myrefference/', views.myrefference, name = "myrefference"),

    path('gispay/', views.gispay, name = "gispay"),
    path('bitcoin/', views.bitcoin, name = "bitcoin"),
    path('matangazo/', views.matangazo, name = "matangazo"),
    path('mahesabu/', views.mahesabu, name = "mahesabu"),
    path('uaminifu/', views.uaminifu, name = "uaminifu"),
    path('english_book/', views.english_book, name = "english_book"),
    path('lulu_book/', views.lulu_book, name = "lulu_book"),
    path('gis_project/', views.gis_project, name = "gis_project"),
    path('wito/', views.wito, name = "wito"),
    path('nisome_kabla/', views.nisome_kabla, name = "nisome_kabla"),
    


    path('register/', views.register, name = "register"),
    
      
]