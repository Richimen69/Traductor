from django.shortcuts import render
from .forms import TextoEs
from mtranslate import translate
 


def traducir(oracion):
   traduccion = translate(oracion, 'en')
   return traduccion

def index(request):
    texto_a_traducir = request.GET.get('texto', '')
    if texto_a_traducir:
        resultado = traducir(texto_a_traducir)
        print(resultado)
    else:
        resultado = ''

    print(resultado)
    return render(request, 'index.html', {
        'TextoEs' : TextoEs(initial={'texto': texto_a_traducir}),
        'resultado': resultado              
    })

def integrantes(request):
    return render(request, 'integrantes.html')

def traductor(request):
    return render(request, 'traductor.html')