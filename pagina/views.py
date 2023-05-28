from django.shortcuts import render
from .forms import TextoEs
from mtranslate import translate
import pyttsx3

def traducir_y_reproducir_voz(oracion):
    traduccion = translate(oracion, 'en')

    # Inicializar el motor de síntesis de voz
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad de reproducción (opcional)

    # Reproducir la traducción como voz
    engine.say(traduccion)
    engine.runAndWait()

    return traduccion

def traducir(oracion):
   traduccion = translate(oracion, 'en')
   return traduccion

def index(request):
    texto_a_traducir = request.GET.get('texto', '')
    if texto_a_traducir:
        resultado = traducir(texto_a_traducir)
        print(resultado)
        resultado = traducir_y_reproducir_voz(texto_a_traducir)
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

