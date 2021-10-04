
from django.conf.urls import url
from django.urls import path
from . import views
from himaya.views import *

app_name='himaya'

urlpatterns = [
    path('',views.home, name='home'),

    

    url(r'^urais_mikoa/$', views.urais_mikoa, name = 'urais_mikoa'),
    url(r'^urais_nchi/$', views.urais_nchi, name = 'urais_nchi'),
    url(r'^announcement/$', views.announcement, name = 'announcement'),


    url(r'^regions/$', views.regions, name= 'regions'),
    url(r'^get_regional_votes_geo/$', views.get_regional_votes_geo, name= 'get_regional_votes_geo'),

    url(r'^get_pres_votes_Geo/$', views.get_pres_votes_Geo, name= 'get_pres_votes_Geo'),
    url(r'^regcenter/$', views.regcenter, name= 'regcenter'),

    url(r'^districts/$', views.districts, name= 'districts'), 
    url(r'^constituency/$', views.constituency, name= 'constituency'), 
    url(r'^wards/$', views.wards, name= 'wards'),
    
    url(r'^wards_in_constituency/$', views.wards_in_constituency, name= 'wards_in_constituency'),
    url(r'^get_constituencies/$', views.get_constituencies, name= 'get_constituencies'),
    url(r'^get_R_constituency/$', views.get_R_constituency, name= 'get_R_constituency'),
    url(r'^get_C_wards/$', views.get_C_wards, name= 'get_C_wards'),
    
    url(r'^get_constituency/$', views.get_constituency, name= 'get_constituency'),
    
    url(r'^get_Const_Winners/$', views.get_Const_Winners, name= 'get_Const_Winners'),
    url(r'^get_C_wards_Winners/$', views.get_C_wards_Winners, name= 'get_C_wards_Winners'),
    url(r'^get_C_wards_View/$', views.get_C_wards_View, name= 'get_C_wards_View'),

    url(r'^get_R_constituency_View/$', views.get_R_constituency_View, name= 'get_R_constituency_View'),
    url(r'^get_R_village_View/$', views.get_R_village_View, name= 'get_R_village_View'),

    
    url(r'^PresVotesConst/$', views.PresVotesConst, name= 'PresVotesConst'),
     url(r'^get_presidential_const_votes_total/$', views.get_presidential_const_votes_total, name= 'get_presidential_const_votes_total'),


    # url(r'^tanzania/$', views.tanzania, name= 'tanzania'), 

    # url(r'^necgis/$', GisPageView.as_view(), name = 'necgis'),

    # url(r'^results/$', ResultsPageView.as_view(), name = 'results'),


    # url(r'^urais/$', UraisView.as_view(), name = 'urais'),
    # url(r'^ubunge/$', UbungeView.as_view(), name = 'ubunge'),


    # url(r'^between/$', BetweenAd.as_view(), name = "between"),
    # url(r'^othermaps/$', othermaps.as_view(), name = "othermaps"),

    # url(r'^region_data/$', region_datasets, name = 'region_data'),
    # url(r'^regcenter_data/$', regcenter_datasets, name = 'regcenter_data'),



    
    
      
]