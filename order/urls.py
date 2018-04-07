from django.urls import path
from order.views import *
from django.conf.urls import url

urlpatterns = [
        url('select_res/' ,select_restaurant ),
        url('show_items/' , show_items),
        url('finalize/', finalize_order),
        url('ordered/', ordered),
        url('view/',view_orders),
        ]
