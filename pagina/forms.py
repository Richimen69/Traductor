from django import forms

class TextoEs(forms.Form):
    texto = forms.CharField(widget=forms.Textarea(attrs={'class':'flex p-2.5 w-full text-2xl text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 font-Quicksand', 'placeholder': 'Introduce el texto' ,'rows':'6'}))

class InputS(forms.Form):
    opciones = (
        ('in', 'Ingles'),
        ('fr', 'Frances'),
        ('de', 'Aleman'),
        ('tr', 'Turco'),
    )
    idioma = forms.ChoiceField(choices=opciones, widget=forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-2xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 font-Quicksand'}))