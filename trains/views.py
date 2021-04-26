from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from trains.forms import TrainForm
from trains.models import Train


class TrainListView(generic.ListView):
    model = Train
    paginate_by = 5
    template_name = 'trains/home.html'


class TrainDetailView(generic.DetailView):
    model = Train
    template_name = 'trains/train_detail.html'


class TrainCreateView(SuccessMessageMixin, generic.CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/train_create.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Train successfully created'


class TrainUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/train_update.html'
    success_message = 'Train successfully updated'


class TrainDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Train
    template_name = 'trains/train_delete.html'
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Train successfully deleted')
        return self.post(request, *args, **kwargs)
