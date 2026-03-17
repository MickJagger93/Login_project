*Descripción Detallada del Proyecto

Este proyecto es una aplicación web de autenticación de usuarios desarrollada con el framework Flask en Python. 
Está diseñada para proporcionar un sistema completo de gestión de cuentas de usuario, incluyendo registro, inicio de sesión, 
restablecimiento de contraseña y cierre de sesión. La aplicación utiliza una base de datos relacional para almacenar 
la información de los usuarios y ofrece una interfaz web responsiva con plantillas HTML personalizadas.

*Arquitectura y Estructura

La aplicación sigue una arquitectura modular típica de Flask, organizada en los siguientes componentes principales:

-Aplicación Principal (app.py): Configura la instancia de Flask, inicializa la base de datos con SQLAlchemy, configura el gestor de 
sesiones con Flask-Login y registra los blueprints para las rutas de autenticación y principales.

-Modelos de Base de Datos (models.py): Define el modelo User con campos como nombre, correo electrónico y hash 
de contraseña. Utiliza SQLAlchemy para la gestión de la base de datos y Werkzeug para el hashing seguro de contraseñas.

-Formularios (forms.py): Implementa formularios con WTForms para registro, inicio de sesión y restablecimiento de contraseña, 
incluyendo validaciones de datos (como correos electrónicos válidos y coincidencia de contraseñas).

-Rutas de Autenticación (routes.py): Maneja las operaciones de registro, login, reset de contraseña y logout. 
Incluye lógica para verificar credenciales, crear usuarios y actualizar contraseñas.

-Rutas Principales (routes.py): Gestiona las páginas públicas (home) y protegidas (landing page para usuarios autenticados).

-Configuración (config.py): Define la configuración de la aplicación, incluyendo la clave secreta para sesiones y la URI de 
la base de datos (por defecto, SQLite).

-Plantillas y Estilos: Utiliza Jinja2 para renderizar plantillas HTML en layouts, con bases separadas para diferentes secciones 
(login, registro, etc.) y archivos CSS/JS en static para el diseño responsivo.

La aplicación incluye migraciones de base de datos con Alembic para gestionar cambios en el esquema, y está preparada para entornos
de desarrollo y producción mediante variables de entorno.

*Características Principales

-Registro de Usuarios: Permite crear cuentas nuevas con validación de correos únicos y contraseñas seguras.
-Inicio de Sesión: Autentica usuarios con verificación de credenciales y gestión de sesiones persistentes.
-Restablecimiento de Contraseña: Ofrece una funcionalidad para cambiar contraseñas existentes, con confirmación de coincidencia.

-Páginas Protegidas: La página de "landing" solo es accesible para usuarios logueados, mostrando información personal.
-Interfaz Web: Diseñada con HTML, CSS y JavaScript para una experiencia de usuario intuitiva, incluyendo formularios interactivos 
y navegación.
-Seguridad: Implementa hashing de contraseñas, validaciones de formularios y protección contra accesos no autorizados.
-Base de Datos: Soporta SQLite por defecto, pero es configurable para otros motores como PostgreSQL o MySQL.

*Tecnologías Utilizadas

-Backend: Flask (framework web), SQLAlchemy (ORM), Flask-Login (gestión de sesiones), Flask-Migrate (migraciones), WTForms (formularios).
-Frontend: Jinja2 (plantillas), HTML5, CSS3, JavaScript.
-Base de Datos: SQLAlchemy con soporte para SQLite (configurable).
-Entorno: Python 3.11+, con virtualenv para aislamiento de dependencias.

*Instalación y Ejecución

-Para ejecutar el proyecto localmente:

-Clona el repositorio y navega al directorio.
-Crea un entorno virtual: python -m venv env.
-Activa el entorno: activate (en Windows).
-Instala dependencias: pip install -r requirements.txt (si existe, o instala manualmente Flask, SQLAlchemy, etc.).
-Configura variables de entorno si es necesario (ej. SECRET_KEY, DATABASE_URL).
-Ejecuta migraciones: flask db upgrade.
-Inicia la app: python app.py (o flask run).

La aplicación se ejecutará en modo debug por defecto, accesible en http://localhost:5000.
