from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.template import loader


from home.forms import HomeForm, ClassRegistration, PostForm2, Images, FriendForm
from home.models import Post,Item, Category,Post4, Downliner, Friend, Paymentdetail
from django.contrib.auth.decorators import login_required

#These class views is for chating
    
class HomeView(TemplateView):
    template_name ='home/chat.html'
        
    def get(self, request):
        form =HomeForm()
        posts = Post.objects.all().order_by('created')
        users = User.objects.all()
        #exclude(id=request.user.id)
    
        friend = Friend.objects.get(current_user=request.user)
    
        friends = friend.users.all()
      
        args = {'form': form, 'posts': posts, 'users': users, 'friends':friends}
        #'friends':friends
        return render(request, self.template_name, args)
        
    def post(self,request):
        form =HomeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user =request.user
            post.save()
            text = form.cleaned_data['post']
            
            
            form = HomeForm()
            return redirect('home:chat')
            
        args = {'form': form, 'text':text}
        return render(request, self.template_name, args)


def activate(request):
        form = HomeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            create = form.save()
            create.save
            
            return redirect('home:activatefriend')
            
        args = {'form': form}
        return render(request, 'home/activate.html', args)

def activatefriend(request):
        form = FriendForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            create = form.save()
            create.save
            
            return redirect('home:chat')
            
        args = {'form': form}
        return render(request, 'home/activatefriend.html', args)



def home(request):
    context = {
       'categories':Item.objects.all() 
    }
    return render (request, "home/home.html", context)
 
def index(request):
    
    context = {
       'categories':Category.objects.all() 
    }
    return render(request, 'home/index.html', context)



def donate(request, item_id):
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None
        
    context = {
        'item': itm
    }

    return render (request, "home/donate.html", context)

def item(request, item_id):
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None
        
    context = {
        'item': itm
    }
    return render(request, 'home/item.html', context)

def category(request, category_id):
    try:
        catg = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        catg = None
    context = {
        'category': catg,
        'categories': Category.objects.all(),
        'count': Item.objects.filter(category=category_id).count()
    }
    return render(request, 'home/category.html', context)





#This view is for class registration- 
def register(request):
        form = ClassRegistration(request.POST or None)
        if form.is_valid():
            create = form.save()
            create.save
            
            return redirect('accounts:login')
            
        args = {'form': form}
        return render(request, 'home/create.html', args)
        
@login_required
def book(request, item_id):
    form = PostForm2(request.POST or None, request.FILES or None)
   
    if form.is_valid():
        create = form.save(commit=False)
        create.save()
            
        return redirect('home:payment', item_id)
            
    item = {'form': form}
        
    return render(request, 'home/book_request.html', item)

@login_required
def payment(request, item_id):
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None
        
    context = {'item': itm}

    return render (request, "home/payment.html", context)

def authors(request):
    return render (request, "home/authors.html", {})



def hasira(request):
    return render (request, "home/hasira.html", {})
def gis(request):
    return render (request, "home/gis.html", {})

def gispay(request):
    return render (request, "home/gispay.html", {})
def makala(request):
    return render (request, "home/makala.html", {})
@login_required
def bitcoin(request):
    return render (request, "home/bitcoin.html", {})
def matangazo(request):
    return render (request, "home/matangazo.html", {})
def mahesabu(request):
    return render (request, "home/matangazo.html", {})
@login_required
def english(request):
    return render (request, "home/english_intro.html", {})
@login_required
def lulu_book(request):
    return render (request, "home/lulu_book.html", {})

def gis_project(request):
    return render (request, "home/gis_project.html", {})

def myrefference(request):
    return render (request, "home/myrefference.html", {})




















#post_list      
def classes_home(request):
    queryset = Classes.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, "home/class_index.html", context)

#post_detail    
def classes_detail(request,id):
    try:
        itm = Classes.objects.get(id=id)
    except Classes.DoesNotExist:
        itm = None
        
    context = {
        'detail': itm,
        "title":itm.title,
        "itm":itm,   
    }
            
    return render(request, "home/class_detail.html", context)   

#post create 


def classes_create(request):
    form = PostForm2(request.POST or None, request.FILES or None)
   
    if form.is_valid():
        create = form.save(commit=False)
        create.save()
            
        return redirect('home:class')
            
    args = {'form': form}
        
    return render(request, 'home/class_create.html', args)
   
#post_update
def classes_update(request,id):
    try:
        instance = Classes.objects.get(id=id)
    except Classes.DoesNotExist:
        instance = None
    
    form = PostForm(request.POST or None, instance=instance)
   
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect (reverse('home:class'))
        
    context = {
        "title":instance.title,
        "instance":instance,
        'form': form,
    }
    return render(request, "home/class_update.html", context)

def classes_delete(request,id):
    try:
        itm = Classes.objects.get(id=id)
    except Classes.DoesNotExist:
        itm = None
    itm.delete()
    return redirect (reverse('home:class'))
     



