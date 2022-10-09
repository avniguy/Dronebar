from django.contrib import admin
from django.urls import path,include
from . import views
from .views import (OrderListView, OrderDeleteView, OrderCreateView,
                    LiveOrdersView, OrderDetailView, OrderUpdateView,
                    OrderSearchView)

app_name='orders'

urlpatterns = [
    path('order_create',OrderCreateView,name='order_create'),
    path('live_orders',LiveOrdersView,name='live_orders'),
    path('order_list',OrderListView.as_view(),name='order_list'),
    path('order_search',OrderSearchView,name='order_search'),
    path('order/<int:id>/detail',OrderDetailView.as_view(),name='order_detail'),
    path('order/<int:id>/update',OrderUpdateView.as_view(),name='order_update'),
    path('order/<int:id>/delete',OrderDeleteView.as_view(),name='order_delete'),

]
