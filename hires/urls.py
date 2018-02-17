from .views import HireCreate, HireUpdate, HireDelete
from django.conf.urls import url, include
urlpatterns = [
    # ...
    url('hire/new/', HireCreate.as_view(), name='author-add'),
    url('hire/<int:pk>/', HireUpdate.as_view(), name='author-update'),
    url('hire/<int:pk>/delete/', HireDelete.as_view(), name='author-delete'),
]
