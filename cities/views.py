from cities.forms import CityForm
from cities.models import City

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator   # Noqa

from django.shortcuts import render   # Noqa
from django.urls import reverse_lazy
from django.views import generic


# def home(request):
#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     form = CityForm()
#     qs = City.objects.all()
#
#     lst = Paginator(qs, 2)
#     page_number = request.GET.get('page')
#     page_obj = lst.get_page(page_number)
#     context = {'page_obj': page_obj, 'form': form}
#     return render(request, 'cities/home.html', context)


class CityDetailView(generic.DetailView):
    model = City
    template_name = 'cities/city_detail.html'


class CityCreateView(SuccessMessageMixin, generic.CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/city_create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'City successfully created'


class CityUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/city_update.html'
    success_message = 'City successfully updated'


class CityDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = City
    template_name = 'cities/city_delete.html'
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'City successfully deleted')
        return self.post(request, *args, **kwargs)


class CityListView(generic.ListView):
    model = City
    paginate_by = 5
    template_name = 'cities/home.html'
