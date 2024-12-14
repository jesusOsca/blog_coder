# Proyecto Blog y Gestión de Usuarios en Django

Este proyecto es una aplicación web en Django que implementa un blog básico donde los usuarios pueden crear, leer, editar y eliminar posts. Además, los usuarios pueden registrarse, iniciar sesión y gestionar su perfil.

## Descripción

La aplicación tiene las siguientes funcionalidades principales:

- **Blog**:
  - Los usuarios pueden ver una lista de posts.
  - Los usuarios pueden ver el detalle de un post y agregar comentarios.
  - Los usuarios pueden crear, editar y eliminar sus propios posts.
  
- **Gestión de Usuarios**:
  - Los usuarios pueden registrarse y crear una cuenta.
  - Los usuarios pueden iniciar sesión y acceder a su perfil.
  - Los usuarios pueden editar su perfil (nombre, email, imagen de perfil, etc.).
  
## Requisitos

Para ejecutar este proyecto, necesitas tener instalado lo siguiente:

- Python 3.x
- Django 4.x
- SQLite (o cualquier otra base de datos compatible con Django)

## Instalación

1. **Clonar el repositorio**:

git clone https://github.com/USERNAME/REPOSITORY_NAME.git cd REPOSITORY_NAME


2. **Crear un entorno virtual**:

python3 -m venv env source env/bin/activate # En Linux/Mac env\Scripts\activate # En Windows


3. **Instalar las dependencias**:

pip install -r requirements.txt


4. **Realizar las migraciones de la base de datos**:

python manage.py migrate


5. **Crear un superusuario** (para acceder al panel de administración de Django):

python manage.py createsuperuser


6. **Iniciar el servidor de desarrollo**:

python manage.py runserver


7. Ahora puedes acceder a la aplicación en tu navegador en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Estructura del Proyecto

- `blog/`: Contiene la aplicación del blog.
- `models.py`: Modelos de los posts y comentarios.
- `views.py`: Vistas para manejar las operaciones CRUD de los posts.
- `urls.py`: Rutas para las vistas del blog.
- `templates/blog/`: Plantillas HTML para mostrar los posts y los formularios.

- `usuarios/`: Contiene la aplicación de gestión de usuarios.
- `models.py`: Modelo de usuario personalizado.
- `views.py`: Vistas para el registro, login y perfil del usuario.
- `urls.py`: Rutas para las vistas de usuario.
- `templates/usuarios/`: Plantillas HTML para las páginas de registro, login y perfil.

- `project/`: Contiene la configuración principal de Django.
- `settings.py`: Configuración del proyecto, incluyendo aplicaciones instaladas, bases de datos, etc.
- `urls.py`: Rutas principales del proyecto, incluyendo las rutas de las aplicaciones `blog` y `usuarios`.

## Funcionalidades

- **Blog**:
- Ver lista de posts.
- Ver detalle de un post.
- Crear, editar y eliminar posts (solo para el autor del post).
- Agregar comentarios a los posts.

- **Usuarios**:
- Registro de usuario con nombre, email y contraseña.
- Login de usuario.
- Perfil de usuario con la posibilidad de editar información personal y cambiar la imagen de perfil.

## Casos de prueba

Los casos de prueba documentados se encuentran en la carpeta `tests/`. Asegúrate de ejecutar los tests para verificar el correcto funcionamiento de la aplicación.

Para ejecutar los tests, utiliza el siguiente comando:

python manage.py test


## Encargado de realizar el trabajo 

- **Jesús Osca** 
  
## Video de Demostración

Aquí puedes ver un video de demostración del proyecto funcionando: [Todavia no lo hice profe estoy a full con finales :c].

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
