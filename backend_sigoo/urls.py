from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls')),
    path('', TemplateView.as_view(template_name='index.html')),  # Adiciona esta linha
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)