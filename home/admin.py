from django.contrib import admin
from .models import Post,Item, Category, Post4, Friend, Paymentdetail

# Register your models here.




#class UserProfileAdmin(admin.ModelAdmin):
    #list_display = ('name', 'description')

    #def user_info(self,obj):
        #return obj.name


    #def get_queryset(self, request):
        #queryset= super(UserProfileAdmin,self).get_queryset(request)
        #queryset= queryset.order_by('phone','user')
        #return queryset


#class PostModelAdmin2(admin.ModelAdmin):
#    list_display = ("title", "published_date","created_date", "subtitle")
#    list_filter = ("created_date", "published_date", "title", "subtitle")
#    search_fields = ("title", "content")
#    
#
#    def user_info(self,obj):
#        return obj.title
#
#
#    def get_queryset(self, request):
#        queryset= super(PostModelAdmin2,self).get_queryset(request)
#        queryset= queryset.order_by('title')
#        return queryset

    
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("post", "user" )

    def user_info(self,obj):
        return obj.user


    def get_queryset(self, request):
        queryset= super(PostModelAdmin,self).get_queryset(request)
        queryset= queryset.order_by('user')
        return queryset





admin.site.register(Post, PostModelAdmin)

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Post4)
admin.site.register(Friend)
admin.site.register(Paymentdetail)


