from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^item/(?P<tech_id>[0-9])', views.item_view, name='item_view'),
    url(r'^search/', views.search_list, name='search_list'),
    url(r'^basket/add/', views.add_to_cart, name='add_to_cart'),
    url(r'^basket/remove/', views.remove_from_cart, name='remove_from_cart'),
    url(r'^basket/', views.get_cart, name='view_cart'),
    url(r'^$', views.item_list, name='post_list'),
]
