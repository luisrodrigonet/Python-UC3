from django.shortcuts import render


# Aula 08
def home(request):
    """
    View para a página inicial (Home).
    Renderiza o template 'home.html'.
    """
    return render(request, "paginas/home.html", {"titulo": "Página Inicial"})


# Aula 08
def sobre(request):
    """
    View para a página 'Sobre'.
    Renderiza o template 'sobre.html'.
    """
    return render(request, "paginas/sobre.html", {"titulo": "Sobre Nós"})


# Aula 08
def politica_privacidade(request):
    """
    View para a página 'Política de Privacidade'.
    Renderiza o template 'politica_privacidade.html'.
    """
    return render(
        request,
        "paginas/politica_privacidade.html",
        {"titulo": "Política de Privacidade"},
    )
