"""
Django settings para o projeto config.

Baseado em Django 5.2.1
"""

from pathlib import Path
from decouple import config  # para carregar variáveis de ambiente de forma segura
import os

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações rápidas para desenvolvimento (não use DEBUG=True em produção!)
SECRET_KEY = 'django-insecure-1wrb)*bi(_a8(s=!*n#w@xsa#=61-k=iw+@0*4dg*#7u^438id'  # chave secreta (deve ser protegida)
DEBUG = True  # habilita mensagens de erro detalhadas (não usar em produção)

ALLOWED_HOSTS = []  # hosts permitidos para requisições HTTP


# Apps instalados no projeto
INSTALLED_APPS = [
    # apps padrão do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # apps de terceiros
    'rest_framework',              # Django REST Framework
    'rest_framework.authtoken',   # Autenticação via token
    
    # app local do projeto
    'app',
]

# Middleware: processos intermediários em cada requisição/resposta
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # proteção contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Middleware customizado para capturar usuário atual na request (para logging)
    'app.signals.CurrentUserMiddleware',
    
    # Obs: 'MessageMiddleware' e 'XFrameOptionsMiddleware' estão repetidos, pode remover a duplicata
]

ROOT_URLCONF = 'config.urls'  # arquivo de rotas do projeto

# Configuração dos templates (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # pasta(s) adicionais para buscar templates
        'APP_DIRS': True,  # habilita busca em app/templates/
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # adiciona request ao contexto
                'django.contrib.auth.context_processors.auth',  # adiciona info de usuário autenticado
                'django.contrib.messages.context_processors.messages',  # mensagens do Django
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'  # ponto de entrada WSGI para o servidor


# Configuração do banco de dados - MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),          # nome do banco (de .env)
        'USER': config('DB_USER'),          # usuário do banco
        'PASSWORD': config('DB_PASSWORD'),  # senha do banco
        'HOST': config('DB_HOST', default='localhost'),  # host do banco
        'PORT': config('DB_PORT', default='3306'),       # porta do banco
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # modo estrito SQL
        },
    }
}


# Validação de senhas do Django (padrão)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Configuração do Django REST Framework (DRF)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # token na header Authorization
        'rest_framework.authentication.SessionAuthentication',  # autenticação por sessão Django
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # API acessível só por usuários logados
    ]
}

# Chaves para criptografia com Fernet (se usar encriptação custom)
FERNET_KEYS = [
    "0Tnp8Cmv2ieOxpHwDoqGZeMDsdk1uhetcQ9nNGhneSk=",  # chave para criptografia
]

STATIC_URL = '/static/'

# Internacionalização (idioma e fuso horário)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True   # habilita internacionalização
USE_TZ = True    # habilita uso de timezone


# Configurações de arquivos estáticos (CSS, JS, imagens)
STATIC_URL = 'static/'

# Tipo padrão para campos de chave primária nas models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
