from django.db import models
from app.models import CustomUser
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime

class Feed(models.Model):
	username = models.ForeignKey(User)
	date = models.DateTimeField()
	message = models.TextField(max_length=250)


	# def __unicode__(self):
	# 	return u'%s' % (self.username)


	# def get_name(self):
	#      return self.username


	# def get_message(self):
	#      return self.message

	# def get_date(self):
	#      return self.date	     

# class SubmitForm(ModelForm):
#     class Meta:
#         model = Feed
#         fields= ('message',)