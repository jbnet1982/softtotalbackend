# Instalación del Backend

## Instrucciones para iniciar el proyecto

Sigue los pasos a continuación desde la **raíz del proyecto** para aplicar las migraciones y ejecutar el servidor de desarrollo:

```bash
# 1. Crear las migraciones para la app 'accounts'
python manage.py makemigrations accounts

# 2. Aplicar todas las migraciones pendientes
python manage.py migrate

# 3. Iniciar el servidor local
python manage.py runserver

