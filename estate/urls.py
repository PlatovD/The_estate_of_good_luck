from django.conf.urls.static import static
from django.urls import include
from django.contrib import admin
from django.urls import path

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
]

admin.site.site_header = "Администрация сайта усадьбы Уюта"
admin.site.index_title = "Лучший отдых"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
