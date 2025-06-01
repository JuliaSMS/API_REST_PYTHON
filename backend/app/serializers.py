from rest_framework import serializers
from .models import Pessoa
from .models import Consentimento
import re
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def validate_cpf(self, value):
        # Remove qualquer caractere que não seja número
        cpf_numeros = re.sub(r'\D', '', value)

        if len(cpf_numeros) != 11:
            raise serializers.ValidationError("O CPF deve conter 11 dígitos numéricos.")

        # Verificação de CPF inválido repetido
        if cpf_numeros == cpf_numeros[0] * 11:
            raise serializers.ValidationError("CPF inválido.")

        # (Opcional: validar dígitos verificadores)

        return value

    def validate_email(self, value):
        if Pessoa.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este e-mail já está cadastrado.")
        return value

    def validate_nome(self, value):
        if not value.strip():
            raise serializers.ValidationError("O nome não pode estar vazio.")
        return value

# app/serializers.py

from rest_framework import serializers
from .models import Consentimento

class ConsentimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consentimento
        fields = ['aceitou', 'data_consentimento']

