from django.shortcuts import render
from .forms import TextoEs, InputS
from mtranslate import translate
import pyttsx3


def traducir(oracion, lenguaje):
    traduccion = translate(oracion, lenguaje)
    # Inicializar el motor de síntesis de voz
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad de reproducción (opcional)
    # Reproducir la traducción como voz
    engine.say(traduccion)
    engine.runAndWait()
    return traduccion

def index(request):
    texto_a_traducir = request.GET.get('texto', '')
    idioma = request.GET.get('idioma', 'in')  # Obtener el valor del idioma seleccionado, por defecto es 'Español'
    resultado = ''
    lblOrigen = 'Español'
    lblDestino = 'Inglés'
    idioma_codigo = {
    'in': 'in',
    'de': 'de',
    'tr': 'tr',
    }

    if texto_a_traducir and idioma in idioma_codigo:
         resultado = traducir(texto_a_traducir, idioma_codigo[idioma])
    else:
        if texto_a_traducir:
            resultado = traducir(texto_a_traducir, 'fr')



    print(resultado)
    print(idioma)

    return render(request, 'index.html', {
        'TextoEs' : TextoEs(initial={'texto': texto_a_traducir}),
        'InputS' : InputS(initial={'idioma': idioma}),
        'resultado': resultado,
        'lblOrigen': lblOrigen,
        'lblDestino': lblDestino
    })

def integrantes(request):
    return render(request, 'integrantes.html')

