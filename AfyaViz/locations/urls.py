from django.urls import path
from . import views

urlpatterns = [
    path('', views.LocationList.as_view(), name="locations"),
    path('details/<str:pk>/', views.LocationDetail.as_view(), name="location-details")

]