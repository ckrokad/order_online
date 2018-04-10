from django.conf.urls import url
from restaurant.views import add_item, view_items, remove_item, view_orders
urlpatterns = [
        url('/add_item/',add_item),
        url('/view_items/',view_items),
        url('/remove/',remove_item),
        url('/view_orders/',view_orders),
        ]
