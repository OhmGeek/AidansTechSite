from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.detail import DetailView

from .models import TechItem
from cart.cart import Cart
import json
from django.http import HttpResponse
# todo replace this with a home page/latest selection
def item_list(request):
    """View a list of all the items"""
    items = TechItem.objects.all()
    return render(request, 'tech/item_list.html', {'items': items})


def search_list(request):
    """Search using request params"""
    text_search_query = ""
    try:
        text_search_query = request.GET['q']
    except MultiValueDictKeyError:
        pass

    # default to an empty string if no search term present
    items = TechItem.objects.filter(name__icontains=text_search_query)
    tags = TechTag.objects.all()
    return render(request, 'tech/item_list.html', {'items': items, 'itemtags': tags})

def item_view(request):
    """View a list of all the items"""
    tech_id = request.GET['id']
    item = TechItem.objects.get(pk=tech_id)

    return render(request, 'tech/tech_item.html', {'item': item})

def add_to_cart(request):
    product_id = request.GET['id']
    quantity = request.GET['quantity']

    item = TechItem.objects.get(pk=product_id)
    cart = Cart(request)
    try:
        cart.add(item, item.cost, quantity)
    except Exception as e:
        return HttpResponse(json.dumps({'itemid': product_id, 'added': False, 'err': "Can't add the item"}), content_type="application/json")
    return HttpResponse(json.dumps({'itemid': product_id, 'added': True}), content_type="application/json")

def remove_from_cart(request):
    product_id = request.GET['id']
    item = TechItem.objects.get(id=product_id)
    cart = Cart(request)
    try:
        cart.remove(item)
    except Exception as e:
        return HttpResponse(json.dumps({'itemid': product_id, 'removed': False, 'err': "Can't remove the item, sorry."}), content_type="application/json")
    return HttpResponse(json.dumps({'itemid': product_id, 'removed': True}), content_type="application/json")

def get_cart(request):
    return render(request, 'tech/cart.html', {'cart': Cart(request)})
#
# # registration for tech
# def register_user(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password1'],
#                 email=form.cleaned_data['email']
#             )
#             return HttpResponseRedirect('/')
#     else:
#         form = UserRegistrationForm()
#
#         return render(request)
