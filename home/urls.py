





from django.conf.urls import url
from . import views
from home.views import HomeView



urlpatterns = [

    url(r'^$', views.index),
    
    
    url(r'^chat', HomeView.as_view(), name = 'chat'),
    
    url(r'^home/$', views.home, name = "home"),
    url(r'^index/$', views.index, name = "index"),    
    url(r'^item/(?P<item_id>\d+)/$', views.item, name = "item"),
    url(r'^item/(?P<item_id>\d+)/book/$', views.book, name = "book"),
    url(r'^item/(?P<item_id>\d+)/payment/$', views.payment, name = "payment"),
    url(r'^item/(?P<item_id>\d+)/donate/$', views.donate, name = "donate"),
    
    url(r'^makala/$', views.makala, name = "makala"),
    url(r'^authors/$', views.authors, name = "authors"),
    

    url(r'^category/(?P<category_id>\d+)/$', views.category, name = "category"),

    url(r'^hasira/$', views.hasira, name = "hasira"),
    url(r'^gis/$', views.gis, name = "gis"),

    url(r'^gispay/$', views.gispay, name = "gispay"),
    url(r'^bitcoin/$', views.bitcoin, name = "bitcoin"),
    url(r'^matangazo/$', views.matangazo, name = "matangazo"),
    url(r'^mahesabu/$', views.mahesabu, name = "mahesabu"),
    url(r'^english/$', views.english, name = "english"),
    url(r'^lulu_book/$', views.lulu_book, name = "lulu_book"),
    url(r'^gis_project/$', views.gis_project, name = "gis_project"),

    url(r'^register/$', views.register, name = "register"),
    url(r'^class/$', views.classes_home, name = "class"),
    url(r'^make/$', views.classes_create, name = "make"),
    url(r'^detail/(?P<id>\d+)/$', views.classes_detail, name = "detail"),
    url(r'^detail/(?P<id>\d+)/edit/$', views.classes_update, name = "update"),
    url(r'^detail/(?P<id>\d+)/delete/$', views.classes_delete, name = "delete"),  
]