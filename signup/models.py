from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class siteUser(models.Model):
	username = models.CharField(max_length=15, unique=True)
	firstName = models.CharField(max_length=30, unique=False)
	lastname = models.CharField(max_length=30, unique=False)
	email = models.CharField(max_length=50, unique=False)
	password = models.CharField(max_length=20, unique=False)
	active=models.IntegerField(default=1)

class history(models.Model):
	uid = models.ForeignKey(siteUser, related_name='historyusers', on_delete=models.CASCADE)
	recent = models.CharField(max_length=100, unique=False)
	wishlist = models.CharField(max_length=100, unique=False)
	
class destination(models.Model):
	place = models.CharField(max_length=50, unique=False)
	state = models.CharField(max_length=50, unique=False)
	desc = models.TextField(max_length=2000, unique=False)
	imghome = models.CharField(max_length=30, unique=False)
	img1 = models.CharField(max_length=30, unique=False)
	img2 = models.CharField(max_length=30, unique=False)
	img3 = models.CharField(max_length=30, unique=False)
	
class review(models.Model):
	uid = models.ForeignKey(siteUser, related_name='reviewusers', on_delete=models.CASCADE)
	did = models.ForeignKey(destination, related_name='reviewdestinations', on_delete=models.CASCADE)
	review = models.TextField(max_length=2000, unique=False)
	
class state(models.Model):
	name = models.CharField(max_length=50, unique=False)
	img = models.CharField(max_length=50, unique=False)
	