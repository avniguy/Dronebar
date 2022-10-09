from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import ShopModelForm,ServiceSiteModelForm, MenuModelForm, MenuItemModelForm
from .models import Shop, ServiceSite, Menu, MenuItem
from drones.models import Drone
import json
from urllib.request import urlopen

# Create your views here.

class ShopList(ListView):
    model = Shop

class ShopDetailView(DetailView):
    template_name = 'shops/shop_detail.html'
    # form_class = ShopDetailForm
    model=Shop
    context_object_name = 'shop'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Shop,id=id_)

    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        shopid = self.object.id
        drones = Drone.objects.filter(shop_id = shopid)
        context['drones'] = drones
        return self.render_to_response(context)

class ShopUpdateView(UpdateView):
    template_name = 'shops/shop_update.html'
    form_class = ShopModelForm
    model=Shop
    context_object_name = 'shop'

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        dr_lst = request.POST['shop_droan_to_delete']
        dr_lst = dr_lst.split(',')
        for d in dr_lst:
            if d.isnumeric():
                dr = Drone.objects.get(id=int(d))
                dr.shop_id=None
                dr.save()
        return super(ShopUpdateView, self).post(request, **kwargs)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Shop,id=id_)

    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        shopid = self.object.id
        drones = Drone.objects.filter(shop_id = shopid)
        context['drones'] = drones
        return self.render_to_response(context)


        # def get_success_url(self):
        # return reverse('shops:shop_list')
        # return reverse("shops:shop_detail" ,kwargs={"id":self.id})

class ShopDeleteView(DeleteView):
    template_name = 'shops/shop_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Shop,id=id_)

    def get_success_url(self):
        return reverse('shops:shop_list')

class ShopCreateView(CreateView):
    model = Shop
    template_name = 'shops/shop_create.html'
    form_class = ShopModelForm


    def form_valid(self,form):
        self.object = form.save()
        print(form.cleaned_data)
        return super().form_valid(form)

class ServiceSiteListView(ListView):
    model = ServiceSite
    template_name = 'service_sites/servicesite_list.html'

class ServiceSiteCreateView(CreateView):
    model = ServiceSite
    template_name = 'service_sites/servicesite_create.html'
    form_class = ServiceSiteModelForm


    def form_valid(self,form):
        self.object = form.save()
        print(form.cleaned_data)
        return super().form_valid(form)

class ServiceSiteDetailView(DetailView):
    template_name = 'service_sites/servicesite_detail.html'
    model=ServiceSite
    form_class = ServiceSiteModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ServiceSite,id=id_)

class ServiceSiteUpdateView(UpdateView):
    template_name = 'service_sites/servicesite_update.html'
    form_class = ServiceSiteModelForm
    model=ServiceSite

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ServiceSite,id=id_)

class ServiceSiteDeleteView(DeleteView):
    template_name = 'service_sites/servicesite_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ServiceSite,id=id_)

    def get_success_url(self):
        return reverse('shops:service_site_list')

class MenuList(ListView):
    template_name = 'menus/menu_list.html'
    model = Menu

class MenuDetailView(DetailView):
    template_name = 'menus/menu_detail.html'
    # form_class = ShopDetailForm
    model=Menu
    context_object_name = 'menu'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Menu,id=id_)

class MenuUpdateView(UpdateView):
    template_name = 'menus/menu_update.html'
    form_class = MenuModelForm
    model=Menu
    context_object_name = 'menu'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Menu,id=id_)

class MenuDeleteView(DeleteView):
    template_name = 'menus/menu_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Menu,id=id_)

    def get_success_url(self):
        return reverse('shops:menu_list')

class MenuCreateView(CreateView):
    model = Menu
    template_name = 'menus/menu_create.html'
    form_class = MenuModelForm


    def form_valid(self,form):
        self.object = form.save()
        print(form.cleaned_data)
        return super().form_valid(form)

class MenuItemCreateView(CreateView):
    model = MenuItem
    template_name = 'menus/menuitem_create.html'
    form_class = MenuItemModelForm


    def form_valid(self,form):
        self.object = form.save()
        print(form.cleaned_data)
        return super().form_valid(form)

class MenuItemListView(ListView):
    template_name = 'menus/menuitem_list.html'
    model = MenuItem

class MenuItemUpdateView(UpdateView):
    template_name = 'menus/menuitem_update.html'
    form_class = MenuItemModelForm
    model=MenuItem
    context_object_name = 'menuitem'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(MenuItem,id=id_)

class MenuItemDeleteView(DeleteView):
    template_name = 'menus/menuitem_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(MenuItem,id=id_)

    def get_success_url(self):
        return reverse('shops:menu_item_list')

class MenuItemDetailView(DetailView):
    template_name = 'menus/menuitem_detail.html'
    # form_class = ShopDetailForm
    model=Menu
    context_object_name = 'menuitem'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(MenuItem,id=id_)
