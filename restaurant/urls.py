from django.conf.urls import url
from restaurant.views import add_item
urlpatterns = [
        url('/add_item/',add_item),
        ]
