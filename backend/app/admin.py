# Importa o módulo de administração do Django
from django.contrib import admin

# Importa o modelo Pessoa que será registrado na área administrativa
from .models import Pessoa

# Decorador para registrar o modelo Pessoa na interface administrativa do Django
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de objetos Pessoa no admin
    list_display = ('nome', 'cpf', 'email', 'criado_em')
    
    # Permite pesquisar pessoas no admin pelos campos nome, cpf e email
    search_fields = ('nome', 'cpf', 'email')
