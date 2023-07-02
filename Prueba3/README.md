## carniceria carvajal django

verificar si esta instalado python y pip

## verificacion pythoin y pip

**comando verificacion python**
```shell
python --version
```

**resultado**
```shell
$ python --version
Python 3.11.1
```

**comando verifiacion pip**
```shell
$ python --version
Python 3.11.1
```

**resultado**
```shell
$ pip --version
pip 23.1.2 from C:\Users\username\AppData\Local\Programs\Python\Python311\Lib\site-packages\pip (python 3.11)
```

## configuracion entorno virtual

para configurar un entorno virtual en python debemos ejecutar el siguiente comando.

**comandoc reacion entorno virtual**
```shell
virtualenv env
```

nota: env representa el nmombre del entorno virtual. por lo tgeneral se utiliza como nombres env, dev, developert. etc

**comando apra activar entorno virtual (windos con gitbash)**
```shell
. env/Scripts/activate
```

**resultado**
```shell
. env/Scripts/activate
(env)
```


## creacion proyecto django

para crear un proyecto Django ejecutaremos el siguiente comando.

**comando apra instalar libreria django**
```shell
pip install Django
```

**resultado**
```shell
$ pip install Django
Collecting Django
  Using cached Django-4.2.2-py3-none-any.whl (8.0 MB)
Collecting asgiref<4,>=3.6.0 (from Django)
  Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1 (from Django)
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Collecting tzdata (from Django)
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-4.2.2 asgiref-3.7.2 sqlparse-0.4.4 tzdata-2023.3
(env) 
```
una vez instalada la librerias de django, ejecutaremos el siguiente comando para crear nuestro proyecto

**comando crear projecto en django con nombre carniceria_carvajal**

```shell
django-admin startproject carniceria_carvajal
```

para desplegar la aplicacion por defecto(sin cambios), ejecutaremos el comando.

```shell
python manage.py runserver
```

**comando para crear archivo con librerias**
```shell
pip freeze > requirements.txt
```

**comando para instalar o ejecutar txt con librerias**
```shell
pip install -r requirements.txt
```

**isntalar mysql client**
```shell
pip install mysqlclient
```

## comando migracion bd

**comando migracion bd**
```shell
python manage.py makemigrations
```

***comando docker para descargar imagen**
```shell
docker build -t musql-division-db:1.0.0 .
```

***comando docker para crear container en docker**
```shell
docker run -d -p 9090:3306 --name mysql-carniceria-container mysql-division-db:1.0.0
```
