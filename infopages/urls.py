from django.conf.urls import url
from .views import view_page

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', view_page, name='page_view'),
]
