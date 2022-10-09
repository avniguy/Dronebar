from django.contrib import admin
from django.urls import path,include
from . import views

from .views import (DroneListView, DroneCreateView, DroneDetailView, DroneDeleteView, DroneUpdateView,
DroneTypeListView, DroneTypeCreateView, DroneTypeDetailView, DroneTypeUpdateView, DroneTypeDeleteView)
#
app_name='drones'

urlpatterns = [
    path('drone_create',DroneCreateView.as_view(),name='drone_create'),
    path('drone_list',DroneListView.as_view(),name='drone_list'),
    path('drone/<int:id>/detail',DroneDetailView.as_view(),name='drone_detail'),
    path('drone/<int:id>/update',DroneUpdateView.as_view(),name='drone_update'),
    path('drone/<int:id>/delete',DroneDeleteView.as_view(),name='drone_delete'),

    path('drone_type_create',DroneTypeCreateView.as_view(),name='drone_type_create'),
    path('drone_type_list',DroneTypeListView.as_view(),name='drone_type_list'),
    path('drone_type/<int:id>/detail',DroneTypeDetailView.as_view(),name='drone_type_detail'),
    path('dronetype/<int:id>/update',DroneTypeUpdateView.as_view(),name='drone_type_update'),
    path('dronetype/<int:id>/delete',DroneTypeDeleteView.as_view(),name='drone_type_delete'),

]
