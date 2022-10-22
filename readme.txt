

Entra en wsl y crea una carpeta en mi cado fue 
/$ mkdir NEyDW
/$ cd NEyDW
Instala y crea tu entorno virtual
/NEyDW/$ sudo apt-get install python3-virtualenv
/NEyDW/$ virtualenv env 
Activa el entorno
/NEyDW/$ source env/bin/activate
/NEyDW/$ sudo pip install django
/NEyDW/$ sudo pip install psycopg2-binary
Como crear la aplicacion de DJANGO
/NEyDW/$ django-admin startproject jaleadStudio
/NEyDW/$ cd jaleadStudio
/NEyDW/jaleadStudio/$python3 manage.py migrate

Como iniciar el proyecto o aplicacion
python manage.py runserver


Como crear una aplicacion
python manage.py startapp nombreApi

