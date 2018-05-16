import requests
from django.shortcuts import render
import slumber
from django.shortcuts import render_to_response
from django.template.context import RequestContext



def get_atracao():
    url = 'http://localhost:8000/atracoes/'
    r = requests.get(url, auth=('admin','Vi118090134'))
    lista = r.json()
    books_list = lista
    return books_list


##consumindo API
API = slumber.API('http://localhost:8000/',auth=('admin','Vi118090134'))
def listar(request):
    ##obter objetos
    lista = API.atracoes.get()
    lista2 =get_atracao()
    ##teste de post
    # new = API.atracoes.post(
    #     {'nome': 'teste post', 'descricao': 'teste post django', 'horario_func': 'teste -01', 'idade_minima': '12'})
    context = {
        'lista': lista,
    }
    return render(request, 'lista.html', context)








# Create your views here.
