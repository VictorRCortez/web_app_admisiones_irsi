### Contexto de la Aplicación

La aplicación web desarrollada es un sistema integral para la gestión de admisiones de estudiantes en una institución educativa. Su objetivo es digitalizar y automatizar procesos críticos como la autenticación segura, el registro de estudiantes, la carga masiva de datos históricos y la generación de reportes, todo bajo estándares de seguridad y usabilidad.

#### Funcionalidades Principales

- **Autenticación Segura con 2FA:** Los usuarios (administradores, directores y consultas) acceden mediante correo y contraseña, con un segundo factor de autenticación (código enviado por correo) para mayor seguridad.
- **Roles y permisos:**
  - Admin/Director: Acceso completo a todas las funcionalidades.
  - Consulta: Solo puede ver reportes.
- **Formulario de Admisión:** Permite registrar nuevos estudiantes con datos detallados, incluyendo datos personales y académicos, con validaciones automáticas para garantizar datos correctos.
- **Carga Masiva de Datos:** Los administradores pueden importar datos históricos desde archivos Excel (.xlsx), con validación automática de duplicados por DNI.
- **Reportes de Estudiantes:** Muestra un listado completo de estudiantes con filtros por país y año, accesible para todos los roles, pero con restricciones para acciones como exportar datos.

#### Tecnologías Utilizadas

- **Backend:** Python + Flask (para la lógica del servidor y rutas).
- **Base de Datos:** Microsoft SQL Server (MSSQL) para almacenamiento seguro y escalable.
- **Frontend:** HTML5, CSS3 y JavaScript (con Bootstrap 5 para diseño responsivo).
- **Seguridad:** Protección contra ataques comunes (XSS, CSRF, inyección SQL), hashing de contraseñas con bcrypt y HTTPS en producción.

#### Beneficios Clave

- **Eficiencia:** Automatiza procesos manuales (ej. carga de datos históricos).
- **Seguridad:** Autenticación robusta, protección de datos sensibles y cumplimiento de estándares (OWASP).
- **Facilidad de Uso:** Interfaz intuitiva con diseño responsivo para dispositivos móviles y de escritorio.
- **Escalabilidad:** Arquitectura modular para futuras mejoras o integraciones.

### Fases

#### Fase 0: Preparación del Entorno de Desarrollo

**Prompt:**
"Configura el entorno de desarrollo para un proyecto Flask con Python 3.8 o superior. Instala un entorno virtual (venv) y las dependencias básicas como pip y git. Organiza la estructura del proyecto con directorios como app/, static/, templates/, y archivos como models.py y run.py. Configura Git para el control de versiones y asegúrate de excluir archivos sensibles con .gitignore. Prepara archivos de configuración como .env para variables de entorno y requirements.txt para las dependencias."

#### Fase 1: Análisis y Planificación

**Prompt:**
"Realiza un análisis y planificación detallada para una aplicación Flask. Define los requisitos funcionales como autenticación segura con login, 2FA por correo y roles de usuario. Planifica la gestión de estudiantes con formularios de admisión y validación de datos, carga masiva de datos desde Excel, y generación de reportes con filtros. Establece requisitos no funcionales como el uso de tecnologías específicas, medidas de seguridad contra XSS y CSRF, y consideraciones de usabilidad y rendimiento."

#### Fase 2: Diseño de la Base de Datos y Arquitectura

**Prompt:**
"Diseña la base de datos MSSQL para una aplicación Flask, asegurándote de que las tablas como Usuarios y Estudiantes estén correctamente definidas con sus relaciones e índices. Implementa un esquema de base de datos robusto que soporte las necesidades de la aplicación. Diseña la arquitectura de la aplicación utilizando Blueprints para modularizar la autenticación y las funcionalidades principales, siguiendo el patrón Factory Pattern para inicializar Flask y sus extensiones."

#### Fase 3: Implementación del Backend (Flask + MSSQL)

**Prompt:**
"Implementa el backend de una aplicación Flask con conexión a una base de datos MSSQL. Desarrolla un sistema de autenticación seguro con formularios Flask-WTF, gestión de sesiones con Flask-Login, y envío de códigos 2FA por correo usando Flask-Mail. Implementa un módulo principal para gestionar estudiantes con validación de datos, carga de datos desde Excel con pandas, y generación de reportes con consultas SQLAlchemy. Asegúrate de implementar medidas de seguridad avanzadas como Flask-Talisman para cabeceras de seguridad y manejo de errores personalizados."

#### Fase 4: Desarrollo del Frontend (HTML/CSS/JS + Bootstrap 5)

**Prompt:**
"Desarrolla el frontend de una aplicación Flask utilizando HTML, CSS, JavaScript y Bootstrap 5. Crea plantillas Jinja2 con herencia para una navegación responsiva y mensajes flash. Diseña páginas específicas como login, autenticación en dos pasos, formularios de estudiantes, carga de Excel y reportes. Implementa un diseño responsivo con Bootstrap 5 y CSS personalizado para ajustes visuales. Añade interactividad con JavaScript para selectores dinámicos y validación del lado del cliente."

#### Fase 5: Pruebas y Optimización

**Prompt:**
"Realiza pruebas unitarias y de integración para una aplicación Flask utilizando pytest. Optimiza el rendimiento de la aplicación con índices en MSSQL, paginación en reportes, y minificación de CSS/JS. Asegúrate de que la aplicación esté segura con validación exhaustiva de entradas y logging de errores. Prepara la aplicación para despliegue con refactorización del código, configuración de logging y copias de seguridad de la base de datos."
