from django.db import models

# Create your models here.
class Baby(models.Model):
    baby_id = models.IntegerField(null = True, blank = True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank = True)
    gender = models.CharField(max_length=255)
    


class Sitter(models.Model):
    sitter_firstname = models.CharField(max_length=255)
    sitter_lastname= models.CharField(max_length=255)
    sitter_price = models.FloatField()
    start_date = models.DateField()

# Enrolled kids, Payment
class EnrolledStudent(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    sitters = models.ForeignKey(Sitter, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)

class Transactions(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.SET_NULL, null=True)
    sitter = models.ForeignKey(Sitter, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()