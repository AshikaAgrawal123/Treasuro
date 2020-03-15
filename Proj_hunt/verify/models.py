from django.db import models

# Create your models here.
class verification(models.Model):
	signid=models.CharField(max_length=12,unique=True,null=True)


	def __str__(self):
		return self.signid