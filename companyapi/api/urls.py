from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewset, EmpViewset, ServiceAPIView, LoginView,ServiceDetailAPIView
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'companies',CompanyViewset)
router.register(r'emp',EmpViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('login/', LoginView.as_view()),
    path('services/',ServiceAPIView.as_view()),
    path('servicedetails/<int:pk>/',ServiceDetailAPIView.as_view()),
]
