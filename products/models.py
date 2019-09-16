from django.db import models

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(max_length=120) #max_length = required
	description = models.TextField(blank= True, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=1000)
	summary     = models.TextField(blank=False, null= False)
	featured 	= models.BooleanField(default=True) # null = True, default =True
	
	def get_absolute_url(self):
		return (f"/products/{self.id}")