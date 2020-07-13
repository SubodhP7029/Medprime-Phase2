from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class AdminProfile(models.Model):

    market_segment = (
        ("medclg", "Medical College"),
        ("pathological", "Pathological Laboratories"),
        ("hospitals", "Hospitals"),
        ("medpro", "Medical Professionals"),
        ("sciclg", "Science College"),
        ("schools", "Schools"),
        ("rnd", "R&D Institues"),
        ("agriculture", "Agriculture"),
        ("veterinary", "Veterinary"),
        ("industrial", "Industrial"),
    )
    tests = (
        ("invoice","Invoice"),
        ("slideimaging","Whole slide imaging"),
        ("Bloodsmear","Peripheral Blood Smear"),
        ("malaria","Malaria"),
        ("sperm","Sperm"),
        ("Urine","urine"),
    )
    adminname = models.CharField(max_length=100)
    password = models.CharField(max_length=32, default='password')
    institutiontype = models.CharField(blank=False,null=True, max_length=50, choices=market_segment)
    institutionname= models.CharField(max_length=50)
    testallowed = MultiSelectField(max_choices=3,max_length=30,default='choices',choices=tests)
    noofuser = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.adminname 

class AllCounters(models.Model):

    name = models.CharField(max_length=150)
    counter = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class adminstorage(models.Model):
    creatorid = models.IntegerField(null=True, blank=True)
    deletorid = models.IntegerField(null=True, blank=True)
    typeofchange = models.CharField(max_length=500, blank=True)
