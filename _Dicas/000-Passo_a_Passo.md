Passo 00 - Ambiente Virtual

0.1 - Criação (primeira vez)

0.2 - Ativar o ambiente (activate.bat / activate.ps1)

0.3 - Instalações / Atualizações (pip ; python -m pip)

Passo 01 - Projeto

1.0 - Criar pasta do projeto (django_projeto_aula08)

1.1 - Criar Projeto (django-admin startproject config .)

1.2 - Ajustar as configurações (config/settings.py)

    - import os
    
    - TEMPLATES 
    
        - "DIRS": [BASE_DIR / "templates"], 
        
        - "APP_DIRS": True,  
        
        - "django.template.context_processors.debug",
    
    - Internationalization
    
        - LANGUAGE_CODE = "pt-br"
        
        - TIME_ZONE = "America/Sao_Paulo" 
    
    - Arquivos Estáticos
   
        - STATICFILES_DIRS 
        
        - STATIC_ROOT 
        
        - STATIC_URL
    
    - Imagens do Banco
    
        - MEDIA_URL
        
        - MEDIA_ROOT

1.3 Ajustar as URLs (config/urls.py)

    - settings.DEBUG
    
        - urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

        - urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Passo 02 - Aplicação

2.1. Criar a aplicação (python manage.py startapp nome_da_app)

2.2. Criar os modelos de banco de dados (models.py) 

2.3. Criar as funções ou classes de visualização (views.py)

2.4. Criar as rotas no arquivo URLs.py da aplicação

2.5. Criar os templates para as Views (app\templates\app\arquivo.html)

2.6. Registar a aplicação no settings.py (config\settings.py)

2.7. Registar o arquivo de URLs da aplicação (app\urls.py) no arquivo de aplicação do projeto (config\urls.py)

2.8. Migrar o modelo de banco de dados para o banco de dados físico

    - python manage.py makemigrations
    
    - python manage.py migrate
    
2.9. Registra as classes do modelo no arquivo admin.py

2.10. Criar um "Super Usuário" para acessar a aplicação "Admin"
