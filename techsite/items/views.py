from django.shortcuts import render
from .models import Category
# Create your views here.
def display_items(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, "items/item_list.html", {
        "categories": categories,
    })
