from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Barbero, Servicio, Cita
from .forms import CitaForm
from django.core.mail import send_mail

def enviar_correo(destino):
    asunto = 'Nueva cita agendada'
    mensaje = 'Alguien ha solicitado una cita con usted, entre a su panel administrativo para confirmarla'
    destinatario = [destino]
    
    send_mail(asunto, mensaje, 'johmmer300@gmail.com', destinatario)

# pagina principal de citas
def citas(request):
    return render(request, 'citas/citas.html', {})

# crear una nueva cita
def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid(): 
            form_object = form.save()
            barbero = form_object.barbero.id
            get_barbero = get_object_or_404(Barbero, id=barbero)
            barbero_email = get_barbero.email
            enviar_correo(barbero_email)
            return redirect('cita_creada', cita_id=form_object.id) 
        else:
            return render(request, 'citas/crear_cita.html', {'form': form})
    else:
        form = CitaForm()
    return render(request, 'citas/crear_cita.html', {'form': form})

def cita_creada(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    return render(request, 'citas/cita_creada.html', {'cita': cita})

# ver una cita por identificador
def ver_cita(request):
    citas = Cita.objects.all()
    identificador = request.GET.get('identificador')
    if identificador not in citas.values_list('identificador', flat=True):
        return HttpResponse("Este identificador no existe.")
    cita_obj = Cita.objects.filter(identificador=identificador)
    return render(request, 'citas/ver_cita.html', {'cita': cita_obj})
 
# editar una cita
def editar_cita(request, pk):
    cita = Cita.objects.get(pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('ver_cita')}?identificador={cita.identificador}")
    else:
        form = CitaForm(instance=cita)
    return render(request, 'citas/editar_cita.html', {'form': form, 'cita': cita})

# cancelar una cita
def cancelar_cita(request, pk):
    cita = Cita.objects.get(pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('citas')
    return render(request, 'citas/cancelar_cita.html', {'cita': cita})