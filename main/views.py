from django.views.generic import ListView, DetailView, TemplateView

from .models import Room, Service


class HomeView(TemplateView):
    template_name = 'main/home.html'
    extra_context = {
        'rooms': Room.objects.prefetch_related('images').all(),
        'services': Service.manager.not_special().prefetch_related('images').all(),
    }


class ServicesView(ListView):
    template_name = 'main/services.html'
    model = Service
    context_object_name = 'services'

    def get_queryset(self):
        if self.kwargs['service_type'] == 'indoors':
            return Service.manager.not_special().prefetch_related('images').all()
        elif self.kwargs['service_type'] == 'special':
            return Service.manager.special().prefetch_related('images').all()


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
    model = Room
    context_object_name = 'rooms'

    def get_queryset(self):
        name = self.kwargs['room_type']
        return Room.objects.filter(category__name=name).prefetch_related('images').all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'люкс' if self.kwargs['room_type'] == 'luxe' else 'стандарт' if self.kwargs[
                                                                                               'room_type'] == 'standard' else 'полулюкс'
        return context


class RoomsDetailView(DetailView):
    template_name = 'main/rooms-detail.html'
    model = Room
    slug_url_kwarg = 'number'
    slug_field = 'id'
