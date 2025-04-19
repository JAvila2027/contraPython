# gestor de usuarios con interfaz grafica
# descripcion
este proyecto permite registrar usuarios "unicos" con sus contraseñas encriptadas y validar que no se repitan nombres de usuario mostrar todos los usuarios registrados y eliminarlos desde la interfaz
# tecnologias usadas
python 3.13.0
flet: para la interfaz grafica
os: para gestion de archivos y carpetas
hashlib: para encriptar contraseñas
# instalacion
clona el proyecto o descarga los archivos
abre la terminal y navega a la carpeta de la aplicacion
# opcional crear un entorno virtual
python -m venv venv
activa el entorno virtual
para windows .\venv\Scripts\activate
para macos o linux source venv/bin/activate
# instalar dependencias
pip install -r requirements.txt
# ejecucion
asegurate de estar dentro de la carpeta del proyecto
ejecuta el archivo principal main.py
# ¿como funciona?
introduce un nombre de usuario y contraseña y clickea guardar usuario
mostrar usuarios presiona mostrar usuarios para ver los registrados
eliminar un usuario introduce el nombre de un usuario registrado y presiona eliminar usuario
# estructura del proyecto
CONTRASEÑAPYTHON
|__ contraseñaPython
|   |__ main.py el archivo principal en donde se ejecuta el programa
|   |__ readme.md documentacion del proyecto
|   |__ requirements.txt dependencias del proyecto
|   |__ contraseñaPython la carpeta donde se almacena el archivo .txt: "usuarios_guardados.txt"
|   |   |__ usuarios_guardados.txt