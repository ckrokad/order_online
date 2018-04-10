from django.http import HttpResponseRedirect
from django.shortcuts import render
from restaurant.forms import ItemsForm
from login.models import Restaurant
from restaurant.models import Items
from django.contrib.auth.decorators import login_required
from order.models import Order
#Create your views here.
@login_required
def add_item(request):
    restaurant = Restaurant.objects.get(User = request.user)
    item_form = ItemsForm(request.POST , request.FILES)
    if item_form.is_valid():
        #restaurant = restaurant.save()
        new_item = item_form.save(commit = True)
        new_item.image = request.FILES['image']
        new_item.save()
        #restaurant = Restaurant.objects.get(User = request.user)
        restaurant.Items.add(new_item)
        restaurant.save()
        return render(request , 'restaurant/item_added.html', {'new_item' : new_item , 'restaurant' : restaurant})
    print(item_form.errors)
    return render(request , 'restaurant/add_item.html', {'item_form' : item_form})

@login_required
def view_items(request):
    restaurant = Restaurant.objects.get(User = request.user)
    items = []
    for id in restaurant.Items.all():
        items.append(id)
    return render(request , 'restaurant/view_items.html' , {'items' : items })


@login_required
def remove_item(request):
    item_id = request.POST.get("item_id")
    item = Items.objects.filter(ITEMID = item_id)
    if item:
        item[0].delete()
    #return render(request , 'restaurant/item_removed.html' )          http://localhost:8000
    return HttpResponseRedirect('/restaurant/view_items/')

@login_required
def view_orders(request):
    restaurant = Restaurant.objects.filter(User = request.user)[0]
    all_orders = Order.objects.all()
    orders = []
    for order in all_orders:
        for item in restaurant.Items.all():
            if item in order.Items.all():
                orders.append(order)
    return render(request , 'restaurant/view_orders.html' , { 'orders' : orders})




















