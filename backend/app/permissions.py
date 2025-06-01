# app/permissions.py

from rest_framework import permissions
from .models import Consentimento

class ConsentimentoAtivoPermission(permissions.BasePermission):
    """
    Permissão que verifica se o usuário consentiu com o tratamento de dados.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        try:
            consentimento = Consentimento.objects.get(usuario=request.user)
            return consentimento.consentiu
        except Consentimento.DoesNotExist:
            return False

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permite acesso total apenas para administradores. Usuários comuns só podem visualizar (GET).
    """

    def has_permission(self, request, view):
        # Permite leitura (GET, HEAD, OPTIONS) para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        # Permite escrita apenas para admin
        return request.user and request.user.is_staff