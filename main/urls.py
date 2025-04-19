from django.urls import path, register_converter

from main.converters import RoomTypeConverter, ServiceTypeConverter

from .views import HomeView, ServicesView, ServicesDetailView, PricesView, InfoView, ContactsView, RoomsView, \
    RoomsDetailView

register_converter(RoomTypeConverter, 'room_type')
register_converter(ServiceTypeConverter, 'service_type')
app_name = 'main'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/<service_type:service_type>/', ServicesView.as_view(), name='services'),
    path('services/<int:number>/', ServicesDetailView.as_view(), name='services_detail'),
    path('prices/', PricesView.as_view(), name='prices'),
    path('info/', InfoView.as_view(), name='info'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('rooms/<room_type:room_type>/', RoomsView.as_view(), name='rooms'),
    path('rooms/<room_type:room_type>/<int:number>/', RoomsDetailView.as_view(), name='rooms_detail'),
]
