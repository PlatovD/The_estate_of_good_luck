from django.views.generic import ListView, DetailView, TemplateView

from .models import Room, Service


class HomeView(TemplateView):
    template_name = 'main/home.html'
    extra_context = {
        'rooms': Room.objects.prefetch_related('images').all(),
        'services': Service.manager.not_special().prefetch_related('images').all(),
    }


class ServicesView(TemplateView):
    template_name = 'main/services.html'

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        queryset = Service.objects.all()

        services = {
            'indoor': [],
            'special': [],
        }

        for serv in queryset:
            if serv.isSpecial:
                services['special'] += [serv]
            else:
                services['indoor'] += [serv]

        kwargs.update(services)
        return kwargs


class ServicesDetailView(DetailView):
    template_name = 'main/services-detail.html'
    model = Service
    context_object_name = 'service'
    pk_url_kwarg = 'number'

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('images')
        return queryset


class PricesView(ListView):
    template_name = 'main/prices.html'
    allow_empty = True


class InfoView(TemplateView):
    template_name = 'main/info.html'


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'


class RoomsView(TemplateView):
    template_name = 'main/rooms.html'

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        rooms = {
            'standard': [],
            'half_luxe': [],
            'luxe': [],
        }
        for room in Room.objects.all():
            if room.category.name == 'standard':
                rooms['standard'] += [room]
            elif room.category.name == 'half-luxe':
                rooms['half_luxe'] += [room]
            else:
                rooms['luxe'] += [room]
        kwargs.update(rooms)
        return kwargs


class RoomsDetailView(DetailView):
    template_name = 'main/rooms-detail.html'
    model = Room
    context_object_name = 'room'
    pk_url_kwarg = 'number'

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('images', 'convenience')
        return queryset

    def get_object(self, queryset=None):
        return super().get_object(queryset)
