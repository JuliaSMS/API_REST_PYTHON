# Importações necessárias para usar sinais do Django, modelos e threading para armazenar dados locais por thread
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Pessoa, LogAcesso
from threading import local

# Cria uma variável thread-local para armazenar dados exclusivos de cada thread (requisição)
_thread_locals = local()

def get_current_user():
    """
    Função para obter o usuário atual armazenado na thread local.
    Retorna None se nenhum usuário estiver definido (ex: requisição anônima).
    """
    return getattr(_thread_locals, 'user', None)

class CurrentUserMiddleware:
    """
    Middleware que captura o usuário autenticado em cada requisição HTTP
    e o armazena em uma variável local à thread para ser acessado depois.
    """
    def __init__(self, get_response):
        self.get_response = get_response  # guarda a função que processa a requisição

    def __call__(self, request):
        # Antes de processar a requisição, armazena o usuário logado na thread local
        _thread_locals.user = request.user
        
        # Processa a requisição e retorna a resposta
        return self.get_response(request)

# Listener para o sinal pós-salvamento do modelo Pessoa
@receiver(post_save, sender=Pessoa)
def log_criacao_ou_edicao(sender, instance, created, **kwargs):
    """
    Ao criar ou atualizar um objeto Pessoa, registra no LogAcesso quem fez a ação,
    qual foi a ação (CREATE ou UPDATE) e algumas informações do objeto alterado.
    """
    usuario = get_current_user()  # pega o usuário da thread local
    acao = 'CREATE' if created else 'UPDATE'  # define o tipo da ação
    
    # Cria o registro no log de acesso
    LogAcesso.objects.create(
        usuario=usuario,
        acao=acao,
        modelo='Pessoa',
        observacoes=f"ID: {instance.id}, Nome: {instance.nome}"
    )

# Listener para o sinal pós-exclusão do modelo Pessoa
@receiver(post_delete, sender=Pessoa)
def log_exclusao(sender, instance, **kwargs):
    """
    Ao deletar um objeto Pessoa, registra no LogAcesso quem fez a exclusão
    e detalhes do objeto excluído.
    """
    usuario = get_current_user()  # pega o usuário da thread local

    # Cria o registro no log de acesso
    LogAcesso.objects.create(
        usuario=usuario,
        acao='DELETE',
        modelo='Pessoa',
        observacoes=f"ID: {instance.id}, Nome: {instance.nome}"
    )
