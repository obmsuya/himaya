from django.shortcuts import render
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required

#from home.forms import HomeForm, ClassRegistration, PostForm2, Images
from himaya.models import Item, Category

# Create your views here.


def index(request):
    
    context = {
       'categories':Category.objects.all() 
    }
    return render(request, 'himaya/index.html', context)
    
    
def item(request, item_id):
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None
        
    context = {
        'item': itm
    }
    return render(request, 'himaya/item.html', context)