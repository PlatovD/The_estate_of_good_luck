from main.models import Service


class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context['services'] = Service.objects.prefetch_related('images').all()
        context.update(kwargs)
        return context
