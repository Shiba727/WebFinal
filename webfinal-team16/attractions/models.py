from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	photo = models.ImageField(null=False,blank=False)
	content = models.CharField(max_length=2000)
	traffic = models.CharField(max_length=300)
	time = models.CharField(max_length=200)
	tags = models.CharField(max_length=200)
	equipment = models.CharField(max_length=200)
	food1_title = models.CharField(max_length=200,blank=True)
	photo_food1 = models.ImageField(null=True,blank=True)
	food1_content = models.CharField(max_length=200,blank=True)
	food1_place = models.CharField(max_length=200,blank=True)
	food2_title = models.CharField(max_length=200,blank=True)
	photo_food2 = models.ImageField(null=True,blank=True)
	food2_content = models.CharField(max_length=200,blank=True)
	food2_place = models.CharField(max_length=200,blank=True)
	food3_title = models.CharField(max_length=200,blank=True)
	photo_food3 = models.ImageField(null=True,blank=True)
	food3_content = models.CharField(max_length=200,blank=True)
	food3_place = models.CharField(max_length=200,blank=True)
	def __str__(self):
		return self.title

			