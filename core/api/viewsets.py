from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet (ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,BasicAuthentication,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')

    #alterar o lookup field padrão do api
    #lookup_field = ('nome')

    ##sobrescrevendo o queryset para fazer filtragem dos itens (where)
    def get_queryset(self):
        ##filtro no query string
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset =queryset.filter(descricao__iexact=descricao)
        return queryset


    ##sobrescrevendo o GET - end point para todos
    # def list(self, request, *args, **kwargs):
    #     return Response({'teste':123})

    ## sobreescrevendo o POST
    # def create(self, request, *args, **kwargs):
    #funcionalidade que você queira implementar
    #     pass

    #sobreescrevendo o delete
    # def destroy(self, request, *args, **kwargs):
    #     pass

    # #sobre escrever get detalhe de um objeto
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    #sobreescrever o PUT- atualizar todos
    # def update(self, request, *args, **kwargs):
    #     pass

    # ##sobreescrevendo o patch - atualizar parte do objeto
    # def partial_update(self, request, *args, **kwargs):
    #     pass

    #criando a sua propria action
    # @action(methods=['get'], detail=True)
    # def denunciar (self, request, pk=None):
    #     pass