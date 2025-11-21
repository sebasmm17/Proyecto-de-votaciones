Para ejecutar el proyecto localmente toca hacer los siguientes pasos: 
1) Crear una carpeta en el escritorio.
2) Abrirla con el cmd y crear un entorno virtual con el siguiente comando: python -m venv env
3) luego de que se cree el entorno virtual, se activan los Scripts con el siguiente comando: env\Scripts\activate
4) Instala django en el entorno virtual con este comando: pip install django
5) Instalar el mysqlclient para que se conecte a bases de datos de mySql que es con el siguiente comando: pip install mysqlclient.
6) luego clona el repositorio en el gitbash con el siguiente comando : git clone https://github.com/sebasmm17/Proyecto-de-votaciones.git
7) crea una base de datos llamada votaciones en mysql
8) abre el proyecto en el visual estudio code luego de clonarlo.
9) utiliza el siguiente comando para verificar las tablas que se van a migrar a la base de datos votaciones: python manage.py makemigrations
10) luego utiliza este otro para hacer la migracion: python manage.py migrate
11) por ultimo ejecuta el programa con el siguiente comando: python manage.py runserver

listo, siguiendo estos pasos deberia de funcionar el proyecto de forma local.
