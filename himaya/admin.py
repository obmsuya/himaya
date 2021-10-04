    #pass
from django.contrib import admin


from himaya.models import Regions,RegionalVotes, Regional_Votes_Geo, Constituents, Village, Regcentre, Pres_Const_Winners_Geo, PresVotesConst
# , Districts, Wards, ConstVotes, Const_Winners_Geo, WardVotes, Wards_Winners_Geo
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class RegcentreAdmin(LeafletGeoAdmin):
    #pass
    list_display =('reg_centre','n_op')

class VillageAdmin(LeafletGeoAdmin):
    #pass
    list_display =('street','regname')

class RegionAdmin(LeafletGeoAdmin):
    #pass
    list_display =('region_nam','zone')

class Regional_Votes_GeoAdmin(LeafletGeoAdmin):
    #pass
    list_display =('region_nam','votes')

class ConstituentsAdmin(LeafletGeoAdmin):
    #pass
    list_display =('const','constid')
    search_fields = ('const', 'constid' )

# class ConstVotesAdmin(LeafletGeoAdmin):
#     #pass
#     list_display =('const', 'candidate_id', 'chama_id','candidate')
#     search_fields = ('candidate','chama_id', 'const')


admin.site.register(Regions, RegionAdmin)
admin.site.register(Village, VillageAdmin)
admin.site.register(Regcentre, RegcentreAdmin)
admin.site.register(Regional_Votes_Geo, Regional_Votes_GeoAdmin)

admin.site.register(Constituents, ConstituentsAdmin)
admin.site.register(PresVotesConst, admin.ModelAdmin)
admin.site.register(Pres_Const_Winners_Geo, admin.ModelAdmin)

# admin.site.register(Village, admin.ModelAdmin)
# admin.site.register(Regcentre, admin.ModelAdmin)

# admin.site.register(Districts, admin.ModelAdmin)


# admin.site.register(Wards, admin.ModelAdmin)


# admin.site.register(ConstVotes, ConstVotesAdmin)
# admin.site.register(Const_Winners_Geo, admin.ModelAdmin)
# admin.site.register(WardVotes, admin.ModelAdmin)
# admin.site.register(Wards_Winners_Geo, admin.ModelAdmin)

admin.site.site_header = "NEC GIS ADMIN SITE"