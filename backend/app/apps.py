# Importa a classe base para configurar o app Django
from django.apps import AppConfig

# Define a configuração do app chamado 'app'
class AppConfig(AppConfig):
    # Define o campo padrão para chaves primárias nos modelos (usar BigAutoField)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nome do app (deve ser o mesmo da pasta do app)
    name = 'app'

    # Método chamado quando o app é carregado e pronto
    def ready(self):
        # Importa os sinais do app para que eles sejam registrados na inicialização
        import app.signals
