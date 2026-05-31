# Proyecto: Sistema de Gestión de Citas para Barbería (Portafolio)

Breve presentación (para cualquier persona)

Esta aplicación es un proyecto de portafolio que muestra cómo se puede gestionar de forma sencilla y visual las citas de una barbería. Está pensada para demostrar diseño, flujo de usuarios y lógica de negocio, no como una guía técnica de despliegue.

Propósito

- Resolver el problema de coordinación de turnos en una barbería: evitar solapamientos, mantener historial de clientes y facilitar la gestión diaria.
- Mostrar buenas prácticas en estructuración de una aplicación web (modelado, vistas, plantillas, validaciones).

Usuarios objetivo

- Clientes: pueden consultar horarios disponibles y reservar un turno.
- Barberos/Personal: visualizan su agenda, confirman o cancelan citas.
- Administrador: gestiona barberos, clientes y revisa el histórico desde el panel administrativo.

Características clave (explicado sin tecnicismos)

- Reservar cita: un cliente selecciona fecha, hora y barbero disponible.
- Evitar conflictos: el sistema no permite dos citas al mismo tiempo para el mismo barbero.
- Editar y cancelar: tanto clientes como el personal pueden modificar o cancelar citas.
- Notas por cita: cada cita puede tener detalles (servicios solicitados, observaciones).
- Panel administrativo: un área privada para gestionar usuarios y datos globales.

Flujo de uso (historias de usuario simples)

1. Un cliente entra a la página y ve las franjas horarias disponibles.
2. Selecciona un horario y confirma la reserva con sus datos.
3. El barbero ve la nueva cita en su agenda y la confirma o marca como completada.
4. Si hay cambios, el cliente o el barbero pueden modificar o cancelar la cita.

Páginas de ejemplo (demo)

- Página principal: `/` — presentación y acceso a gestión de citas.
- Ver citas: `/citas/` — lista de citas.
- Crear cita: `/citas/crear/` — formulario para reservar.
- Ver una cita: `/citas/<id>/` — detalles y opciones.
- Panel de administración (privado): `/admin/`.

Arquitectura resumida (versión para no técnicos y desarrolladores)

- Basada en Django (un marco para crear aplicaciones web con Python).
- Organización principal:
	- La lógica de citas está en la aplicación `citas` (`citas/models.py`, `citas/views.py`).
	- Las páginas están construidas con plantillas HTML en `templates/`.
	- Estilos y scripts en `static/` y `staticfiles/`.

Modelos principales (qué datos se guardan)

- Cita: fecha, hora, barbero asignado, cliente, estado (pendiente, confirmada, cancelada), notas.
- Cliente: nombre, teléfono, email (datos básicos para contacto).
- Barbero: nombre, especialidad, horario.

Diseño y experiencia (qué se busca mostrar en el portafolio)

- Claridad en el flujo de reservas y reducción de fricción para el usuario.
- Validaciones visibles (por ejemplo, aviso si un horario ya está ocupado).
- Interfaz sencilla y enfocada en la tarea principal: agendar y gestionar citas.

Capturas y demostraciones

Incluye aquí capturas de pantalla o GIFs de la interfaz (reemplaza los placeholders por imágenes reales):

- `screenshots/home.png` — vista principal (placeholder)
- `screenshots/crear_cita.png` — formulario de creación (placeholder)

Sección técnica breve (para quien quiera profundizar)

- Lenguaje: Python
- Framework: Django
- App principal: `citas` (contiene modelos, vistas, formularios y migraciones)
- Puntos clave del código: `citas/models.py`, `citas/views.py`, `citas/forms.py`, `templates/`.

Cómo presentar este proyecto en un portafolio

- Resalta el problema que resuelve (gestión de turnos y comunicación cliente-barbero).
- Muestra los flujos de usuario con capturas o una demo en vídeo.
- Explica decisiones de diseño: por qué se previenen solapamientos, cómo se maneja la confirmación de citas.
- Añade métricas o mejoras posibles: integración de notificaciones, sincronización con calendarios externos, multi-sede.

Apéndice: instalación mínima (opcional, más técnica)

Si quieres ejecutar el proyecto localmente (solo para desarrolladores o revisores técnicos), sigue estos pasos básicos desde la carpeta que contiene `manage.py`:

```bash
# Crear un entorno virtual
python -m venv .venv
source .venv/bin/activate

# Instalar dependencias si existe requirements.txt
pip install -r requirements.txt

# Aplicar migraciones y crear superusuario
python manage.py migrate
python manage.py createsuperuser

# Ejecutar servidor de desarrollo
python manage.py runserver
```

Contacto y licencia

Si incluyes este proyecto en tu portafolio, añade tu nombre, email y un enlace al repositorio/preview. Indica la licencia si corresponde.

---

Archivo actualizado: `README.md` (orientado a portafolio, descripción y funcionalidades).
