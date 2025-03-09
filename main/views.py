from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/home.html')


class ServicesView(ListView):
    template_name = 'main/services.html'
    allow_empty = True


class ServicesDetailView(DetailView):
    template_name = 'main/services.detail'
    pk_url_kwarg = None


class PricesView(ListView):
    template_name = 'main/prices.html'
    allow_empty = True


class InfoView(TemplateView):
    template_name = 'main/info.html'


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'


class RoomsView(ListView):
    template_name = 'main/rooms.html'
    allow_empty = True


class RoomsDetailView(DetailView):
    template_name = 'main/rooms-detail.html'
