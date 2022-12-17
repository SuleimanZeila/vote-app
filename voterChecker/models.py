from django.db import models
from django.contrib import admin

# Create your models here.
class Voter(models.Model):
    constituency = models.CharField(max_length = 40,default='Garissa Township')
    caw = models.CharField(max_length = 20)
    polling_center = models.CharField(max_length = 100)
    date_of_birth = models.CharField(max_length = 50)
    fname = models.CharField(max_length = 100)
    mname = models.CharField(max_length = 50,null=True)
    sname = models.CharField(max_length = 50)
    sex = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 20,null=True)
    id_passport_num = models.CharField(max_length = 20)

    def __str__(self):
    	return self.id_passport_num
    objects = models.Manager()

    
class VoterAdmin(admin.ModelAdmin):
    search_fields = ['id_passport_num']