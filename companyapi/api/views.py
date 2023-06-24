from django.shortcuts import render
from rest_framework import viewsets,status
from .models import company,employee
from .serializers import CompanySerializer,EmpSerializer,ServiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import Service
# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=CompanySerializer
class EmpViewset(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=EmpSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh=RefreshToken.for_user(user)
            return Response({'status':'auth success',
                            'access_token':str(refresh.access_token),
                            "refresh":str(refresh)})   
        else:
            return Response({'status':'not authenticated'},status=status.HTTP_401_UNAUTHORIZED)
        
class ServiceAPIView(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ServiceDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
