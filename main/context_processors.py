from main.models import Service


def get_services(request):
    return {
        'services_indoor': Service.manager.not_special(),
    }
