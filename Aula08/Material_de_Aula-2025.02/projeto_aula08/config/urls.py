from django.contrib import admin

# Aula 08 - Adicionada a função include
from django.urls import path, include

# Aula 08
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # Aula 08
    # Conecta todas as URLs da aplicação 'paginas' na raiz do site
    path("", include("paginas.urls")),
]


# Aula 08 - Apenas em modo de desenvolvimento (DEBUG=True)
if settings.DEBUG:
    # Configuração para servir Static Files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Configuração para servir Media Files (arquivos de usuário)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
