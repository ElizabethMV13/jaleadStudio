<h1># Pasos a seguir</h1>

Entra en wsl y crea una carpeta en mi cado fue 
``/$ mkdir NEyDW``
``/$ cd NEyDW``
Instala y crea tu entorno virtual
``/NEyDW/$ sudo apt-get install python3-virtualenv``
/NEyDW/$ virtualenv env 
Activa el entorno
/NEyDW/$ source env/bin/activate
/NEyDW/$ sudo pip install django
/NEyDW/$ sudo pip install psycopg2-binary

<h1>--> ESTA PARTE ES SOLO SI QUIEREN APRENDER COMO SE CREO EL PROYECTO Y LA API</h1>
Como crear la aplicacion de DJANGO
/NEyDW/$ django-admin startproject jaleadStudio
/NEyDW/$ cd jaleadStudio
/NEyDW/jaleadStudio/$python3 manage.py migrate

Como iniciar el proyecto o aplicacion
python manage.py runserver


Como crear una aplicacion
python manage.py startapp nombreApi

