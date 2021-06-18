
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#from django.contrib.auth import views as auth_views

# from django.contrib.auth.views import (
#     login,
#     logout,
#     password_reset,
#     password_reset_done,
#     password_reset_confirm,
#     password_reset_complete
# )

app_name='accounts'

urlpatterns = [


    path('', views.view_profile),
    path('signup/', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('entry/', views.entry, name = 'entry'),
    
    
    path('register/', views.register, name='register'),
   
    path('profile/', views.view_profile, name='view_profile'),
    path('activate/', views.activate, name='activate'),

   
    path('<int:profile_id>/', views.view_profile, name='view_profile_with_pk'),

    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
]