from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=40)
	def __unicode__(self):
		return str(self.name)
		
class Offer(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=150)
	category = models.ForeignKey(Category)
	description = models.TextField()
	price = models.IntegerField()
	closed=models.NullBooleanField(null=True,blank=True)
	img=models.ImageField(blank=True, upload_to="imageuploads")
	phone = models.IntegerField(null=True,blank=True)
	def __unicode__(self):
		return str(self.user.username) + ' '+ str(self.category)
# Create your models here.
