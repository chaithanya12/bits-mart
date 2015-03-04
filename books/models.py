from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookOffer(models.Model):
	user = models.ForeignKey(User)
	price = models.IntegerField()
	name = models.CharField(max_length=50)
	course_code = models.CharField(max_length=10,null=True,blank=True)
	branch = models.CharField(max_length=10,null=True,blank=True)
	closed=models.NullBooleanField(null=True,blank=True)
	phone = models.IntegerField(null=True,blank=True)
	def __unicode__(self):
		return str(self.user.username) + ' '+ str(self.name)