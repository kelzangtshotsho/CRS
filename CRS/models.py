from django.db import models


# Create your models here.
 

# class Category(models.Model):
# 	Space = models.CharField(max_length=100, null=False, blank=False)

# 	def __str__(self):
# 		return self.Space

class Photo(models.Model):
	Image = models.ImageField(null=False, blank=False)
	CID = models.IntegerField(null=True)
	Name = models.CharField(max_length=100)
	Account = models.IntegerField()
	Phone = models.IntegerField(null=True)
	Type = models.CharField(max_length=100, null=False, blank=False)
	Capacity= models.IntegerField()
	Rate = models.CharField(max_length=100)
	PickLocation = models.CharField(max_length=100, null=False)


	def __int__(self):
		return self.Type

	def __int__(self):
		return self.Capacity

	def __int__(self):
		return self.Account

	def __str__(self):
		return self.Name

	# def __int__(self):
	# 	return self.Price

class Rent(models.Model):
	Owner = models.IntegerField(null=True)
	CID = models.IntegerField(null=True)
	PickDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
	DropDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
	PickLocation = models.CharField(max_length=100, null=False)
	DropLocation = models.CharField(max_length=100, null=False)


	def __int__(self):
		return self.Owner

	def __int__(self):
		return self.PickDate

	def __int__(self):
		return self.PickDrop

	def __str__(self):
		return self.PickLocation

	def __str__(self):
		return self.DropLocation



		

