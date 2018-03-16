## Instrucciones para crear entorno de desarrollo

1.  Instalación de requisistos(requiere permisos de root o utilizar sudo)
    *   Paquetes indispensables
    ```
    apt-get install python2.7 python-pip python-pip python2.7-dev virtualenv 
    ```

2.  Instalación de aplicación y requisitos.
    *   Para el resto de de las instrucciones el directorio de trabajo será el del proyecto
    ```
    cd siesdesarrollo
    ```
    *   Entorno virtual
    ```
    virtualenv -p /usr/bin/python2.7 .venv
    source .venv/bin/activate
    ```
    *   Instalación de dependencias
    ```
    pip install -r requirements.txt
    ```
    *   Aplicar migraciones
    ```
    ./manage.py migrate
    ```
    *   Crear administrador
    ```
      ./manage.py createsuperuser
    ```
    *   Lanzar aplicación
    ```
      ./manage.py runserver
    ```
    *   Abrir la url localhost:8000 en navegador
