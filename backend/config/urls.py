from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as drf_views

from app.views import (
    PessoaViewSet,
    ConsentimentoViewSet,
    excluir_dados_pessoais,
    gerenciar_consentimento,
)

# Router do DRF para registrar viewsets automaticamente
router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'consentimentos', ConsentimentoViewSet, basename='consentimento')  # <-- aqui

urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoints da API gerenciados pelo router do DRF
    path('api/', include(router.urls)),

    # Endpoint para obter token de autenticação
    path('api/token/', drf_views.obtain_auth_token),

    # Endpoint customizado para exclusão de dados pessoais (LGPD)
    path('api/apagar-dados/', excluir_dados_pessoais),

    # Endpoint customizado para gerenciar consentimento
    path('api/consentimento/', gerenciar_consentimento),

]
