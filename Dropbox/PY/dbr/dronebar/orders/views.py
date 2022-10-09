from django.shortcuts import render,get_object_or_404,HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Order, OrderRow
from .filters import OrderCreateFilter
import datetime
from datetime import datetime
import json
from .forms import ShopOptionForm,OrderRowFormSet, OrderModelForm
from shops.models import Menu, MenuItem, Shop, ServiceSite  # START THIS IS A TEST FOR CREATING A NEW ORDER JUST LIKE IN THE APP
from drones.models import DroneType,Drone

# Create your views here.

def OrderSearchView(request):
    template_name = 'orders/order_search.html'
    context = {'page_name':"order_search,html"}
    model=Order

    if request.method == "POST":
        order_date_from = request.POST.get('date_from','').replace('-','/') # order search params
        order_date_to = request.POST.get('to_date','').replace('-','/') # order search params
        status = request.POST.get('status','') # order search params

        if len(order_date_from) == 0:
            order_date_from="2010/01/01"
        if len(order_date_to) == 0:
            order_date_to="2040/01/01"

        if status == "All":
            orders = Order.objects.filter(order_date__range=(datetime.strptime(order_date_from + " 01:00:00.000000", '%Y/%m/%d %H:%M:%S.%f'),datetime.strptime(order_date_to + " 23:59:00.000000", '%Y/%m/%d %H:%M:%S.%f')))
        else:
            orders = Order.objects.filter(status = status,order_date__range=(datetime.strptime(order_date_from + " 01:00:00.000000", '%Y/%m/%d %H:%M:%S.%f'),datetime.strptime(order_date_to + " 23:59:00.000000", '%Y/%m/%d %H:%M:%S.%f')))

        context["orders"]=orders

    return render(request,'orders/order_search.html',context)

def LiveOrdersView(request):
    template_name = 'orders/live_orders.html'
    shop_id=0

    if request.session.get('shop_id',0) > 0:
        print("request.session['shop_id']" + str(request.session.get('shop_id',0)))
        shop_id=request.session.get('shop_id',0)

    drones = Drone.objects.filter(shop_id=shop_id)

    context = {'live_orders':''}
    context["drones"] = drones
    shops = Shop.objects.all()
    context["shops"] = shops

    if request.method == "POST":
        if 'get_shops' in request.POST:
            shop_id = int(request.POST.get('shops',''))
            request.session['shop_id']= shop_id

        live_orders = Order.objects.filter(status__in = ['New','Processing','Shipped','Delievered'],shop_id=shop_id,order_date__date = datetime.today().date()).order_by('-status')
        context["live_orders"] = live_orders

        if 'next_step' in request.POST:

            order_id_proceed = request.POST.get('order_id_proceed','') # order id for next step status
            order_drone = request.POST.get('order_drone','') # order drone id
            ord_prcd = Order.objects.get(id=int(order_id_proceed))
            new_status = ''

            if ord_prcd.status == 'New':
                new_status = 'Processing'
            elif ord_prcd.status == 'Processing':
                new_status = 'Shipped'
            elif ord_prcd.status == 'Shipped':
                new_status = 'Delievered'
            elif ord_prcd.status == 'Delievered':
                new_status = 'Closed'

            ord_prcd.status = new_status
            if order_drone.isnumeric() == True and int(order_drone)>0:
                ord_prcd.drone_id = int(order_drone)

            ord_prcd.save()

    return render(request,'orders/live_orders.html',context)

def OrderCreateView(request):
    template_name = 'orders/order_create.html'
    form = ShopOptionForm(request.GET)
    context = {'form':form}
    menu = Menu.objects.all()
    model=Order

    if request.method =='GET':
        if form.is_valid():
            shop_id = form.cleaned_data.get('shop')
            shop_details = Shop.objects.get(id=shop_id)

            drn_ = Drone.objects.filter(shop_id = shop_details.id).first()
            drone_type = DroneType.objects.get(id=drn_.drone_type.id)
            # drone_type = DroneType.objects.get(id=shop_details.drone_type.id)
            max_payload = drone_type.payload_weight

            if shop_details.menu is None:
                context = {'form':form}
                context['error_msg'] = "This shop has no menu to choose from"
            else:
                context = {'form':form}
                context['error_msg'] = ""
                context['shop_id'] = shop_id
                context['max_payload'] = max_payload
                menu_details = Menu.objects.get(id = shop_details.menu.id)
                items = menu_details.items.all()
                context['menu_items'] = items

    if request.method == "POST":
        order_data = request.POST.get('total_order_data','') # order rows
        shop_id = request.POST.get('shop_id','') #order_id
        geolocation = request.POST.get('location','') #geolocation
        g = geolocation.split(",")

        # print("Geolocation="+geolocation)

        j_order_rows = []
        j_order_rows = json.loads(order_data)

        s = Shop.objects.get(id=shop_id)
        o = Order(customer=1,shop=s,status='New',order_date=datetime.now(),total_price=j_order_rows["order_price"],total_weight=j_order_rows["order_weight"],lat_location=float(g[0]),long_location=float(g[1]))
        o.save()

        for j in j_order_rows["order_rows"]:
            mi = MenuItem.objects.get(id=j["item"])
            row = OrderRow(order=o,item=mi,quantity=j["quantity"],item_price=j["item_price"])
            row.save()

        object_list = Order.objects.all()
        context = {'object_list':object_list}
        return render(request,'orders/order_list.html',context)
    return render(request,'orders/order_create.html',context)

class OrderListView(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'orders/order_list.html'

class OrderDetailView(DetailView):
    template_name = 'orders/order_detail.html'
    model=Order
    context_object_name = 'order'
    order_id = 0

    def get_object(self):
        id_ = self.kwargs.get("id")
        self.order_id=id_ #TEST
        print("order id is:" + str(self.order_id))
        return get_object_or_404(Order,id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        od = OrderRow.objects.filter(order_id=self.order_id)
        context['rows'] = od
        return context

class OrderUpdateView(UpdateView):
    template_name = 'orders/order_update.html'
    form_class = OrderModelForm
    model=Order
    context_object_name = 'order'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Order,id=id_)

    def get_success_url(self):
        id_ = self.kwargs.get("id")
        return reverse("orders:order_detail",kwargs={"id":id_})

class OrderDeleteView(DeleteView):
    template_name = 'orders/order_delete.html'
    model=Order

    def delete(self,*args,**kwargs):
        context={}
        obj=self.object = self.get_object()
        success_url = self.get_success_url()
        my_order = Order.objects.get(id=obj.id)
        my_order.status='Canceled'
        my_order.save()
        return HttpResponseRedirect(success_url)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Order,id=id_)

    def get_success_url(self):
        return reverse('orders:order_list')
