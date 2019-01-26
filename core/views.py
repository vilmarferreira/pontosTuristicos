import requests
from django.shortcuts import render
import slumber
from django.shortcuts import render_to_response
from django.template.context import RequestContext



def get_atracao(token):
    url = 'http://localhost:8000/atracoes/'
    headers = {'Authorization': 'Token %s' % token}
    r = requests.get(url, headers=headers)
    lista = r.json()
    books_list = lista
    return books_list


##consumindo API
API = slumber.API('http://localhost:8000/',auth=('admin','Vi118090134'))
def listar(request):
    us= request.user.username
    se=request.user.auth_token
    ##obter objetos
    lista = API.atracoes.get()
    lista2 =get_atracao(se)
    ##teste de post
    # new = API.atracoes.post(
    #     {'nome': 'teste post', 'descricao': 'teste post django', 'horario_func': 'teste -01', 'idade_minima': '12'})
    context = {
        'lista': lista2,
    }
    return render(request, 'lista.html', context)








# Create your views here.
