from django.shortcuts import render
from minutas.models import Minuta
# Create your views here.
def inicio(request):
    nombre= "dario Guerrero"
    correo="hola@gmail.com"
    nombre_arr= nombre.split()
    iniciales= nombre_arr[0][0].upper() + nombre_arr[1][0].upper()

    minutas=Minuta.objects.all()
    
    return render(request,'inicio.html',
        {'nombre':nombre,
        'correo':correo,
        'iniciales': iniciales,
        'conteo_minutas':len(minutas)
        })