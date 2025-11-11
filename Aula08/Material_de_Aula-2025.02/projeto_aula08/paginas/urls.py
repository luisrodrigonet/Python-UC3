# paginas/urls.py
from django.urls import path
from . import views

# Define o namespace da aplicação (útil para referências em templates)
app_name = "paginas"

urlpatterns = [
    path("", views.home, name="home"),  # URL vazia será a raiz (/)
    path("sobre/", views.sobre, name="sobre"),  # URL /sobre/
    path(
        "politica-privacidade/", views.politica_privacidade, name="politica_privacidade"
    ),  # URL /politica-privacidade/
]
