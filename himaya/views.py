    
from django.shortcuts import render, redirect,reverse
from django.http import JsonResponse
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


from himaya.models import *
from himaya.forms import ImportShapefileForm


# new loginpage




def home(request):
    template = 'himaya/home.html'
    context = {}
    return render (request, template, context)


@login_required
def announcement(request):
    template = 'himaya/announcement.html'
   
    context = {
      
    }
    
    return render (request, template, context)


def urais_mikoa(request):
    template = 'himaya/urais_mikoa.html'
   
    context = {
      
    }
    
    return render (request, template, context)

def urais_nchi(request):
    template = 'himaya/urais_nchi.html'
   
    context = {
      
    }
    
    return render (request, template, context)



def tanzania(request):
    series = Tanzania.objects.all()
    
    tz=serialize('geojson', series,
          geometry_field='geom',
          fields=('name',))
    
    
    return HttpResponse(tz, content_type='json')

def regions(request):
    series = Regions.objects.all()
    
    rg=serialize('geojson', series,
          geometry_field='geom',
          fields=('region_nam','pk','zoneid',))
        
    return HttpResponse(rg, content_type='json')


def get_regional_votes_geo(request):
    series = Regional_Votes_Geo.objects.all()
    rg=serialize('geojson', series,
          geometry_field='geom',
          fields=('region_nam','zoneid','votes','regionid'))
        
    return HttpResponse(rg, content_type='json')





def districts(request):
    series = Districts.objects.all()
    
    ds=serialize('geojson', series,
          geometry_field='geom',
          fields=('district_n','region_nam','pk',))
        
    return HttpResponse(ds, content_type='json')




def constituency(request):
    series = Constituents.objects.all()
    
    con=serialize('geojson', series,
          geometry_field='geom',
          fields=('const','district_n',' region_nam','pk','concilid'))#concilid-- fake winners
        
    return HttpResponse(con, content_type='json')


def PresVotesConst(request):
    con_id = int(request.GET['const'])
    series = PresVotesConst.objects.filter(const_id=con_id).order_by('-votes')
    rg=serialize('json', series,fields=('pk','const_id','votes','chama_id','cand_name'))
        
    return HttpResponse(rg, content_type='json')
# region votes
def get_pres_votes_Geo(request):
    series = Pres_Const_Winners_Geo.objects.all()
    rg=serialize('geojson', series,
          geometry_field='geom',
          fields=('pk','const_id','votes','chama_id','cand_name','const','region_nam'))
    return HttpResponse(rg, content_type='json') 

def regcenter(request):
    series = Regcentre.objects.all()
    rg=serialize('geojson', series,
          geometry_field='geom',
          fields=('ward','reg_centre'))
    return HttpResponse(rg, content_type='json')    

def  get_presidential_const_votes_total(request):
    series = list(PresVotesConst.objects.values('chama_id','cand_name').annotate(total_votes=Sum('votes')).order_by('-total_votes'))
    return HttpResponse(json.dumps(series))  

def get_Const_Winners(request):
    con = int(request.GET['const'])
    series = ConstVotes.objects.filter(const=con).order_by('-votes')#const_id#order by votes decending
    
    con=serialize('json', series,
          
          fields=('pk','ward_id','candidate','votes','chama_id'))
        
    return HttpResponse(con, content_type='json')


def get_constituencies(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    consts = Constituents.objects.filter(const__icontains=q)
    results = []
    for pl in consts:
      const_json = {}
      const_json = pl.const + "," + pl.district_n+"-" + str(pl.pk)
      results.append(const_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def get_constituency(request):
    con = request.GET['con']
    series = Constituents.objects.filter(pk=con)
    
    con=serialize('geojson', series,
          geometry_field='geom',
          fields=('const','district_n',' region_nam','pk',))
        
    return HttpResponse(con, content_type='json')

def get_R_constituency(request):
    con = request.GET['region']
    series = Constituents.objects.filter(region_nam=con)
    
    con=serialize('geojson', series,
          geometry_field='geom',
          fields=('const','district_n',' region_nam','pk','concilid'))
        
    return HttpResponse(con, content_type='json')

def get_R_constituency_View(request):
    con = request.GET['region']
    series = Const_Winners_Geo.objects.filter(region_nam=con)
    
    con=serialize('geojson', series,
          geometry_field='geom',
          fields=('constid','const','district_n',' region_nam','chama_id','concilid','votes'))
        
    return HttpResponse(con, content_type='json')

def get_R_village_View(request):
    con = request.GET['region']
    series = Village.objects.filter(regname=con)
    
    con=serialize('geojson', series,
          geometry_field='geom',
          fields=('street','ward_name',' regname'))
        
    return HttpResponse(con, content_type='json')


def wards(request):
    series = Wards.objects.all()
    
    wd=serialize('geojson', series,
          geometry_field='geom',
          fields=('ward_name','district_n','const','pk','constid'))#constid-- fake winners
        
    return HttpResponse(wd, content_type='json')

def wards_in_constituency(request):
    #id 125... must capture geometry here only
    const=Constituents.objects.filter(constid=125).values('geom')
    
    series = Wards.objects.filter(geom__intersects=const)
    
    wd_const=serialize('geojson', series,
          geometry_field='geom',
          fields=('ward_name','district_n','const','pk',))
        
    return HttpResponse(wd_const, content_type='json')


# def get_C_wards(request):
#     con = request.GET['region']
#     series = Wards.objects.filter(region_nam=con)
    
#     con=serialize('geojson', series,
#           geometry_field='geom',
#           fields=('ward_name','district_n','const','constid'))
        
    # return HttpResponse(con, content_type='json')

def get_C_wards(request):
    con = request.GET['region']
    series = Wards.objects.filter(region_nam=con)
    
    con=serialize('geojson', series,
          geometry_field='geom',
          fields=('ward_name','const',' region_nam'))
        
    return HttpResponse(con, content_type='json')


# #views


def get_C_wards_View(request):
    con = request.GET['const']
    series = Wards_Winners_Geo.objects.filter(const=con)
    
    con=serialize('geojson', series,
          geometry_field='geom',
          fields=('wardid','ward_name','district_n','const','chama_id','constid','votes'))
        
    return HttpResponse(con, content_type='json')

def get_C_wards_Winners(request):
    con = int(request.GET['ward'])
    series = WardVotes.objects.filter(ward=con).order_by('-votes')#ward_id
    
    con=serialize('json', series,
          
          fields=('pk','ward_id','candidate','votes','chama_id'))
        
    return HttpResponse(con, content_type='json')











# # dav github

# class UraisView(TemplateView):
#     template_name = 'home/urais.html'

    
#     def dispatch(self, *args, **kwargs):
#         return super(UraisView, self).dispatch(*args, **kwargs)

# class UbungeView(TemplateView):
#     template_name = 'home/ubunge.html'

    
#     def dispatch(self, *args, **kwargs):
#         return super(UbungeView, self).dispatch(*args, **kwargs)


# class GisPageView(TemplateView):
#     template_name = 'home/necgis.html'

#     # @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(GisPageView, self).dispatch(*args, **kwargs)

# class ResultsPageView(TemplateView):
#     template_name = 'home/results.html'

#     # @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(ResultsPageView, self).dispatch(*args, **kwargs)

# class BetweenAd(TemplateView):
#     template_name = 'home/between.html'

#     # @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(BetweenAd, self).dispatch(*args, **kwargs)

class othermaps(TemplateView):
    template_name = 'home/othermaps.html'

    

@login_required
def region_datasets(request):
    mikoa = serialize('geojson', region.objects.all())
    return HttpResponse(mikoa,content_type='json')
    



def regcenter_datasets(request):
    points = serialize('geojson', reg_center.objects.all())
    return HttpResponse(points,content_type='json')










     



