from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import HireCreateForm
from .models import Hire

class HireCreate(CreateView):
    form_class = HireCreateForm
    template_name = 'hires/hire_form.html'
class HireUpdate(UpdateView):
    model = Hire
    fields = '__all__'

class HireDelete(DeleteView):
    model = Hire
