from django.conf.urls.static import static
from django.urls import include, re_path
from django.contrib import admin
from django.urls import path

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
]

admin.site.site_header = "Администрация сайта усадьбы Уюта"
admin.site.index_title = "Лучший отдых"
if not settings.DEBUG:
    from django.views.static import serve

    urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
