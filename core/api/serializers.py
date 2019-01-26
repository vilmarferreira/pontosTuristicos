from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.models import Atracao
from core.models import PontoTuristico, DecIdentificacao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco

class DocIndentificacaoSerializer (ModelSerializer):
    class Meta:
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    atracao = AtracaoSerializer(many = True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIndentificacaoSerializer()
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao','aprovado','foto', 'atracao',
                  'endereco','comentarios', 'avaliacoes','descricao_completa',
                  'descricao_completa2', 'doc_identificacao')
        read_only_fields = ('comentarios', 'avaliacoes')


    ## ManyToMany
    def cria_atracoes(self,atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao) #criando atracoes no banco de dados
            ponto.atracoes.add(at) ##relacionando atracoes com o ponto turistico


    def create(self, validated_data):

        atracoes = validated_data['atracoes'] ##recebendo os dados e criando uma lista de atracoes
        del validated_data['atracoes'] ## deletando a lista de atracoes da lista recebida.

        endereco = validated_data['endereco']  # recebe os dados enviado e separa o endereco em uma variavel
        del validated_data['endereco']  # deleta variavel

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DecIdentificacao.objects.create(**doc)


        ponto = PontoTuristico.objects.create(**validated_data) #adicionando ponto turistico, depois de excluir atracoes da lista de ados recebido.
        self.cria_atracoes(atracoes,ponto)


        ## Forekey
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()
        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)