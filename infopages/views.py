from django.shortcuts import render
from .models import InfoPage
# Create your views here.
def view_page(request, slug):
    # Look up the slug.
    page = InfoPage.objects.get(slug=slug)
    page_data = {
        "page": page
    }
    return render(request, 'infopages/view_page.html', page_data)
