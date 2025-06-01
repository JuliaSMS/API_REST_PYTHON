from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Pessoa, Consentimento
from .serializers import PessoaSerializer, ConsentimentoSerializer
from .permissions import ConsentimentoAtivoPermission, IsAdminOrReadOnly
from django.shortcuts import render


class PessoaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para CRUD completo do modelo Pessoa.
    Requer autenticação e só permite escrita para admins (leitura aberta).
    """
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class ConsentimentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para CRUD do modelo Consentimento.
    Somente usuários autenticados podem acessar.
    Retorna apenas os consentimentos do usuário logado.
    """
    serializer_class = ConsentimentoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtra consentimentos apenas do usuário da requisição
        return Consentimento.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        # Ao criar um consentimento, associa ao usuário logado automaticamente
        serializer.save(usuario=self.request.user)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def excluir_dados_pessoais(request):
    """
    Endpoint para o usuário apagar todos os seus dados pessoais conforme LGPD.
    Apaga Pessoa e Consentimento associados e desativa o usuário no sistema.
    """
    user = request.user

    # Apaga registros do usuário
    Pessoa.objects.filter(usuario=user).delete()
    Consentimento.objects.filter(usuario=user).delete()
    
    # Desativa usuário (sem deletar)
    user.is_active = False
    user.save()

    return Response(
        {"mensagem": "Seus dados foram apagados conforme solicitado."},
        status=status.HTTP_200_OK
    )

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def gerenciar_consentimento(request):
    """
    Endpoint para consultar ou alterar o consentimento do usuário.
    GET retorna o consentimento atual.
    POST atualiza o consentimento com os dados enviados.
    """
    usuario = request.user

    # Tenta buscar consentimento existente, senão cria um novo para o usuário
    try:
        consentimento = Consentimento.objects.get(usuario=usuario)
    except Consentimento.DoesNotExist:
        consentimento = Consentimento.objects.create(usuario=usuario)

    if request.method == 'GET':
        serializer = ConsentimentoSerializer(consentimento)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ConsentimentoSerializer(consentimento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensagem': 'Consentimento atualizado com sucesso'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
