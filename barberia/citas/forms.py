from django import forms
from .models import Cita
from datetime import timedelta
from django.contrib.admin import widgets as admin_widgets
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'barbero', 'servicio', 'cliente_nombre', 'cliente_telefono', 'notas']
        widgets = {
            'fecha': DateTimePickerInput(options={
                'format': 'YYYY-MM-DD hh:mm A',  # Formato de 12 horas
                'useCurrent': True,
                'showClose': True,
                }
            ),
            'barbero': forms.Select(attrs={'id' : 'barbero', 'class': 'form-group form-control'}),
            'servicio': forms.Select(attrs={'id' : 'servicio', 'class': 'form-control form-group'}),
            'cliente_nombre': forms.TextInput(attrs={'id' : 'nombreCliente', 'class': 'form-control form-group', 'placeholder': 'Nombre Completo del Cliente'}),
            'cliente_telefono': forms.TextInput(attrs={'id' : 'telefonoCliente', 'class': 'form-control form-group', 'placeholder': '000-000-0000', 'pattern': '[0-9]{3}-[0-9]{3}-[0-9]{4}'}),
            'notas': forms.Textarea(attrs={'id' : 'notas', 'class': 'form-control form-group', 'rows': 3,'placeholder': 'Escriba aquí cualquier detalle adicional sobre la cita que el barbero deba conocer. (opcional)'}),
        }
        labels = {
            'fecha': 'Fecha y Hora',
            'barbero': 'Barbero',
            'servicio': 'Servicio',
            'cliente_nombre': 'Nombre Completo del Cliente',
            'cliente_telefono': 'Teléfono del Cliente',
        }
    def clean(self):
        cleaned_data = super().clean()
        barbero = cleaned_data.get('barbero')
        nueva_fecha = cleaned_data.get('fecha')

        if barbero and nueva_fecha:
            inicio = nueva_fecha
            fin = inicio + timedelta(hours=1)

            citas_existentes = Cita.objects.filter(barbero=barbero).exclude(pk=self.instance.pk)

            for cita in citas_existentes:
                cita_inicio = cita.fecha
                cita_fin = cita_inicio + timedelta(hours=1)

                if (inicio < cita_fin) and (fin > cita_inicio):
                    self.add_error('fecha', 'El barbero ya tiene una cita programada en este horario. Deberá elegir otro horario.')
                    break

        return cleaned_data
    
class CitaFormAdmin(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha','identificador' , 'barbero', 'servicio', 'cliente_nombre', 'cliente_telefono', 'estado', 'notas']
        
        labels = {
            'fecha': 'Fecha y Hora',
            'identificador': 'Identificador',
            'barbero': 'Barbero',
            'servicio': 'Servicio',
            'cliente_nombre': 'Nombre Completo del cliente',
            'cliente_telefono': 'Teléfono del Cliente',
            'estado': 'Estado de la Cita',
            'notas': 'Notas',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        barbero = cleaned_data.get('barbero')
        nueva_fecha = cleaned_data.get('fecha')

        if barbero and nueva_fecha:
            inicio = nueva_fecha
            fin = inicio + timedelta(hours=1)

            citas_existentes = Cita.objects.filter(barbero=barbero).exclude(pk=self.instance.pk)

            for cita in citas_existentes:
                cita_inicio = cita.fecha
                cita_fin = cita_inicio + timedelta(hours=1)

                if (inicio < cita_fin) and (fin > cita_inicio):
                    self.add_error('fecha', 'El barbero ya tiene una cita programada en este horario. Deberá elegir otro horario.')
                    break

        return cleaned_data
    