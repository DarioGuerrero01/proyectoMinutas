from django.shortcuts import render, redirect
from .models import Minuta
from django.db.models import Q


# Create your views here.



#Muestra listado de minutas
def listado(request):
    minutas = Minuta.objects.all()
    return render(request,'listado.html',{
        'minutas':minutas
    })

#Muestra el formulario para crear nueva minuta

def formularioCrearMinuta(request):
    return render(request,'formulario.html',{
        'titulo':'Crear Minuta',
        'minuta_id': -1
    })
    
# Guarda las Minutas    
def guardar(request):

    minuta_id= int(request.POST['minuta_id'])
    #si minuta id es-1 creamos una nueva minuta
    if minuta_id==-1:
        minuta=Minuta(
            titulo=request.POST['titulo'],
            secretario=request.POST['secretario'],
            texto=request.POST['texto'],
            fecha_reunion=request.POST['fecha_reunion'],
            hora_inicio=request.POST['hora_inicio'],
            hora_fin=request.POST['hora_fin'],
            asistentes=request.POST['asistentes']
        )
        minuta.save()
    # Quiere decir que vamos a editar    
        
    else:  
        minuta=Minuta.objects.get(id=minuta_id)
        minuta.titulo=request.POST['titulo']
        minuta.secretario=request.POST['secretario']
        minuta.texto=request.POST['texto']
        minuta.fecha_reunion=request.POST['fecha_reunion']
        minuta.hora_inicio=request.POST['hora_inicio']
        minuta.hora_fin=request.POST['hora_fin']
        minuta.asistentes=request.POST['asistentes']
        minuta.save()
        


    return redirect('minutas.listado')    

  
def eliminar(request, id: int):
    minuta=Minuta.objects.get(id=id)
    minuta.delete()
    return redirect('minutas.listado')


def formularioEditar(request, id: int):
    minuta=Minuta.objects.get(id=id)
    return render(request,'formulario.html',{
        'titulo':'Editar Minuta',
        'minuta_id': id,
        'minuta':minuta
    })

def ver(request, id: int):
    minuta=Minuta.objects.get(id=id)
    return render(request,'ver.html',{
        'titulo': f'Mostrando Minuta : {minuta.titulo}',
        'minuta_id': id,
        'minuta':minuta
    })

def formularioBusqueda(request):
    return render(request,'buscar.html',{
        'subtitulo':'resultados'
    })

def resultadosBusqueda(request):

    texto_a_buscar = request.POST['busqueda']
    minutas = Minuta.objects.filter( Q(titulo__contains=texto_a_buscar) | Q(texto__contains=texto_a_buscar))
    return render(request,'buscar.html',{
        'minutas' : minutas,
        'subtitulo' : f'resultados de la busqueda "{texto_a_buscar}" '
    })

