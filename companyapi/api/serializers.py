from rest_framework import serializers
from api.models import company,employee, Service
from django.contrib.auth.models import User

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = company
        fields="__all__"
class EmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=employee
        fields="__all__"
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('username','password')
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'time', 'description', 'price', 'discount']
