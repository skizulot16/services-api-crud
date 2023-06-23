from django.db import models
# Create your models here.
class company(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    type=models.CharField(max_length=50,choices=(('it','it'),('ce','ce')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class employee(models.Model):
    empname=models.CharField(max_length=255)
    company=models.ForeignKey(company, on_delete=models.CASCADE)
class Service(models.Model):
    name=models.CharField(max_length=25)
    time=models.CharField(max_length=25)
    description=models.CharField(max_length=27)
    price=models.FloatField(default=0.0)
    discount=models.IntegerField(default=0)