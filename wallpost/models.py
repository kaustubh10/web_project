from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 

class Category(models.Model):
	
	name = models.CharField(max_length=128,unique=True)
	slug = models.SlugField(max_length=50)
	category_user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __unicode__(self):
		return self.name
	
	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Category,self).save(*args,**kwargs)

class Post(models.Model):
	
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	post_user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=128,unique=True)
	content = models.TextField()
	post_image = models.ImageField(upload_to='post_image',blank=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	
	def __unicode__(self):
		return self.title
	
class UserProfile(models.Model):
	
	prof_choice = (
		('Student','Student'),
		('Professional','Professional'),
	)
	
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	hometown = models.CharField(max_length=128)
	currrent_city = models.CharField(max_length=128)
	profession = models.CharField(max_length=12,choices=prof_choice,default='Student')
	institution = models.CharField(max_length=128)
	profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
	about_me = models.TextField()
	
	def __unicode__(self):
		return self.user.username
