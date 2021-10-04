

from __future__ import unicode_literals
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

# Create your models here.



# class Zones(models.Model):
#     #gid = models.AutoField()
#     zone = models.CharField(max_length=250, blank=True, null=True)
#     reg_total = models.IntegerField(blank=True, null=True)
#     dist_total = models.IntegerField(blank=True, null=True)
#     const_tota = models.IntegerField(blank=True, null=True)
#     zoneid=models.BigIntegerField(primary_key=True)
#     leveltypid = models.SmallIntegerField(blank=True, null=True)
#     geom = models.MultiPolygonField(srid=4326, blank=True, null=True)
#     objects = GeoManager()
#     class Meta:
#         managed = False
#         db_table = 'zones'
        
class Tanzania(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)
    objects=GeoManager()
    class Meta:
        managed = False
        db_table = 'tanzania'

class Regions(models.Model):
    #gid = models.AutoField()
    region_nam = models.CharField(max_length=50, blank=True, null=True)
    regionid = models.BigIntegerField(primary_key=True)
    zone = models.CharField(max_length=250, blank=True, null=True)
    zoneid = models.SmallIntegerField(blank=True, null=True)
    leveltypei = models.SmallIntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326,blank=True, null=True)
    objects = GeoManager()    
    class Meta:
        managed = False
        db_table = 'regions'

class RegionalVotes(models.Model):
    region = models.CharField(max_length=50, blank=True, null=True)
    votes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'regional_votes'






class Regional_Votes_Geo(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    
    region_nam = models.CharField(max_length=50, blank=True, null=True)
    regionid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zone = models.CharField(max_length=250, blank=True, null=True)
    zoneid = models.BigIntegerField(blank=True, null=True)
    leveltypei = models.BigIntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)
    region = models.CharField(max_length=50, blank=True, null=True)
    votes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    objects = GeoManager()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'regional_votes_geo'



class Districts(models.Model):
    #gid = models.AutoField()
    region_nam = models.CharField(max_length=50, blank=True, null=True)
    district_n = models.CharField(max_length=50, blank=True, null=True)
    distid = models.SmallIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326,blank=True, null=True)
    objects = GeoManager()
    class Meta:
        managed = False
        db_table = 'districts'





class Constituents(models.Model):
    #gid = models.AutoField()
    region_nam = models.CharField(max_length=50, blank=True, null=True)
    district_n = models.CharField(max_length=50, blank=True, null=True)
    const = models.CharField(max_length=50, blank=True, null=True)
    constid = models.BigIntegerField(primary_key=True)
    concilid = models.SmallIntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326,blank=True, null=True)
    objects=GeoManager()
    class Meta:
        managed = False
        db_table = 'constituents'




class Wards(models.Model):
    #gid = models.AutoField()
    region_nam = models.CharField(max_length=50, blank=True, null=True)
    district_n = models.CharField(max_length=50, blank=True, null=True)
    ward_name = models.CharField(max_length=50, blank=True, null=True)
    const = models.CharField(max_length=50, blank=True, null=True)
    wardid=models.SmallIntegerField(primary_key=True)
    constid = models.BigIntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326,blank=True, null=True)
    objects=GeoManager()
    class Meta:
        managed = False
        db_table = 'wards'





class ConstVotes(models.Model):
    candidate_id = models.BigIntegerField(primary_key=True)
    const = models.ForeignKey('Constituents', models.DO_NOTHING)
    chama_id = models.SmallIntegerField()
    votes = models.BigIntegerField()
    candidate = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'const_votes'
     

class Const_Winners_Geo(models.Model):
    region_nam = models.CharField(max_length=50, blank=True, null=True)
    district_n = models.CharField(max_length=50, blank=True, null=True)
    const = models.CharField(max_length=50, blank=True, null=True)
    constid = models.BigIntegerField(blank=True, null=True)
    concilid = models.BigIntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)
    votes = models.BigIntegerField(blank=True, null=True)
    chama_id = models.SmallIntegerField(blank=True, null=True)
    const_id = models.BigIntegerField(blank=True, null=True)
    objects = GeoManager()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'const_winners_geo'

class WardVotes(models.Model):
    candidate_id = models.BigIntegerField()
    ward_id = models.BigIntegerField()
    chama_id = models.SmallIntegerField(blank=True, null=True)
    votes = models.BigIntegerField(blank=True, null=True)
    candidate = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ward_votes'





class Wards_Winners_Geo(models.Model):
    # gid = models.IntegerField(blank=True, null=True)
    # id = models.BigIntegerField(blank=True, null=True)
    region_nam = models.CharField(max_length=50, blank=True, null=True)
    district_n = models.CharField(max_length=50, blank=True, null=True)
    ward_name = models.CharField(max_length=50, blank=True, null=True)
    const = models.CharField(max_length=50, blank=True, null=True)
    wardid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    constid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)
    votes = models.BigIntegerField(blank=True, null=True)
    chama_id = models.SmallIntegerField(blank=True, null=True)
    ward_id = models.BigIntegerField(blank=True, null=True)
    objects = GeoManager()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'wards_winners_geo'


class PresVotesConst(models.Model):
    vote_id = models.BigIntegerField(primary_key=True)
    #const_id = models.ForeignKey('Constituents', models.DO_NOTHING)#ward_id
    const_id = models.BigIntegerField()
    chama_id = models.SmallIntegerField()
    votes = models.BigIntegerField()
    cand_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pres_votes_const'

# class PresVotesConst(models.Model):
#     vote_id = models.IntegerField(primary_key=True)
#     # const_id = models.BigIntegerField()
#     chama_id = models.IntegerField()
#     votes = models.BigIntegerField()
#     cand_name = models.CharField(max_length=40)

#     class Meta:
#         managed = False
#         db_table = 'pres_votes_const'
        
# region layer
class Pres_Const_Winners_Geo(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    region_nam = models.CharField(max_length=50, blank=True, null=True)
    district_n = models.CharField(max_length=50, blank=True, null=True)
    const = models.CharField(max_length=50, blank=True, null=True)
    constid = models.BigIntegerField()
    concilid = models.SmallIntegerField(blank=True, null=True)
    geom =  models.MultiPolygonField(srid=4326)
    objects = GeoManager()
    chama_id = models.SmallIntegerField()
    votes = models.BigIntegerField()
    const_id = models.BigIntegerField()
    cand_name=models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'pres_winners_geo'

class Village(models.Model):
    geom = models.MultiPolygonField(srid=4210, blank=True, null=True)
    regname = models.CharField(max_length=30, blank=True, null=True)
    ward_name = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    objects = GeoManager()

    class Meta:
        managed = False
        db_table = 'Village'

class Regcentre(models.Model):
    geom = models.MultiPointField(srid=32737, blank=True, null=True)
    n_op = models.CharField(max_length=13, blank=True, null=True)
    ward = models.CharField(max_length=254, blank=True, null=True)
    reg_centre = models.CharField(max_length=254, blank=True, null=True)
    reg_id = models.BigIntegerField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    shrtname = models.CharField(max_length=50, blank=True, null=True)
    objects = GeoManager()

    class Meta:
        managed = False
        db_table = 'RegCentre'


