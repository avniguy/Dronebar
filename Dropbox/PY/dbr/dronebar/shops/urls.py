from django.contrib import admin
from django.urls import path,include
from . import views

from .views import (ShopCreateView,ShopDetailView,ShopList,ShopDeleteView, ShopUpdateView,
ServiceSiteCreateView, ServiceSiteListView, ServiceSiteDetailView,ServiceSiteUpdateView, ServiceSiteDeleteView,
MenuCreateView, MenuList, MenuDetailView, MenuUpdateView, MenuDeleteView, MenuItemCreateView, MenuItemListView,
MenuItemUpdateView, MenuItemDeleteView, MenuItemDetailView)
#
app_name='shops'

urlpatterns = [
    path('service_site_create',ServiceSiteCreateView.as_view(),name='service_site_create'),
    path('service_site_list',ServiceSiteListView.as_view(),name='service_site_list'),
    path('service_site/<int:id>/detail',ServiceSiteDetailView.as_view(),name='service_site_detail'),
    path('service_site/<int:id>/update',ServiceSiteUpdateView.as_view(),name='service_site_update'),
    path('service_site/<int:id>/delete',ServiceSiteDeleteView.as_view(),name='service_site_delete'),

    path('shop_create',ShopCreateView.as_view(),name='shop_create'),
    path('shop_list',ShopList.as_view(),name='shop_list'),
    path('shop/<int:id>',ShopDetailView.as_view(),name='shop_detail'),
    path('shop/<int:id>/update',ShopUpdateView.as_view(),name='shop_update'),
    path('shop/<int:id>/delete',ShopDeleteView.as_view(),name='shop_delete'),

    path('menu_create',MenuCreateView.as_view(),name='menu_create'),
    path('menu_list',MenuList.as_view(),name='menu_list'),
    path('menu/<int:id>',MenuDetailView.as_view(),name='menu_detail'),
    path('menu/<int:id>/update',MenuUpdateView.as_view(),name='menu_update'),
    path('menu/<int:id>/delete',MenuDeleteView.as_view(),name='menu_delete'),

    path('menu_item_create',MenuItemCreateView.as_view(),name='menu_item_create'),
    path('menu_item_list',MenuItemListView.as_view(),name='menu_item_list'),
    path('menuitem/<int:id>',MenuItemDetailView.as_view(),name='menu_item_detail'),
    path('menuitem/<int:id>/update',MenuItemUpdateView.as_view(),name='menu_item_update'),
    path('menuitem/<int:id>/delete',MenuItemDeleteView.as_view(),name='menu_item_delete'),

]
