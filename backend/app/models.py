from django.db import models
from django.contrib.auth.models import User
from fernet_fields import EncryptedCharField

class Pessoa(models.Model):
    # nome completo
    nome = models.CharField(max_length=150)

    # CPF da pessoa 
    cpf = EncryptedCharField(max_length=14)  # 000.000.000-00
    
    # Email da pessoa
    email = EncryptedCharField(max_length=100)
    
    # Data de criação preenchido automaticamente
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome



class LogAcesso(models.Model):
    ACOES = [
        ('CREATE', 'Criação'),
        ('UPDATE', 'Atualização'),
        ('DELETE', 'Exclusão'),
        ('READ', 'Leitura'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    acao = models.CharField(max_length=10, choices=ACOES)
    modelo = models.CharField(max_length=100)
    data_hora = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.acao} - {self.modelo} - {self.data_hora}"
    
class Consentimento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    consentiu = models.BooleanField(default=False)
    data_consentimento = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.usuario.username} - {"Consentiu" if self.consentiu else "Não consentiu"}'

