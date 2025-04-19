import os
import flet as ft
import hashlib

def encriptar_contraseña(contraseña):
    """
    encripta una contraseña usando sha256
    contraseña (str): la contraseña a encriptar
    str: la contraseña encriptada
    """
    return hashlib.sha256(contraseña.encode()).hexdigest()
def guardar_user(usuario,contraseña):
    """
    guarda un usuario y contraseña en un archivo de texto ".txt"
    usuario (str): el nombre de usuario
    contraseña (str): la contraseña del usuario
    bool: true si el usuario se guardo y el false si ya existe
    """
    ruta_carpeta="contraseñaPython"
    os.makedirs(ruta_carpeta,exist_ok=True)
    ruta_archivo=os.path.join(ruta_carpeta,"usuarios_guardados.txt")
    usuarios_existentes={}
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo,"r") as archivo:
            for linea in archivo:
                if "=" in linea and "contraseña=" in linea:
                    partes=linea.strip().split(" ")
                    usuarios_existentes[partes[0].split("=")[1]]=partes[1].split("=")[1]
    if usuario in usuarios_existentes:
        return False
    contraseña_encriptada=encriptar_contraseña(contraseña)
    with open(ruta_archivo,"a") as archivo:
        archivo.write(f"usuario={usuario} contraseña={contraseña_encriptada}")
    return True
def ver_usuarios():
    """
    muestra una toda una lista de todos los usuarios registrados
    list: la lista de nombres de usuarios registrados
    """
    ruta_archivo=os.path.join("contraseñaPython","usuarios_guardados.txt")
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo,"r") as archivo:
            return [linea.split(" ")[0].split("=")[1] for linea in archivo.readlines()]
    return []
def eliminar_usuario(nombre_usuario):
    """
    elimina un usuario especifico del archivo de usuarios registrados
    nombre_usuario (str): nombre del usuario a eliminar
    bool: true si el usuario elegido es eliminado y el false si no esta registrado
    """
    ruta_archivo=os.path.join("contraseñaPython","usuarios_guardados.txt")
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo,"r") as archivo:
            lineas=archivo.readlines()
        usuario_encontrado=False
        with open(ruta_archivo,"w") as archivo:
            for linea in lineas:
                if f"usuario={nombre_usuario} " not in linea:
                    archivo.write(linea)
                else:
                    usuario_encontrado=True
        return usuario_encontrado
    return False
def main(page: ft.Page):
    """
    configura y ejecutar la interfaz del gestor de usuarios
    """
    page.title="gestor de usuarios"
    page.theme_mode=ft.ThemeMode.DARK
    page.bgcolor=ft.colors.BLACK
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    titulo=ft.Text("gestor de usuarios",size=32,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE)
    input_usuario=ft.TextField(
        label="nombre de usuario",
        width=300,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK
    )
    input_contraseña=ft.TextField(
        label="contraseña",
        password=True,
        width=300,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK
    )
    mensaje_resultado=ft.Text(value="",size=18,
                            color=ft.colors.RED)
    def guardar(e):
        usuario=input_usuario.value.strip()
        contraseña=input_contraseña.value.strip()
        if not usuario or not contraseña:
            mensaje_resultado.value="Error el texto no puede esta vacio"
        elif guardar_user(usuario,contraseña):
            mensaje_resultado.value=f"usuario {usuario} fue guardado con exito"
            mensaje_resultado.color=ft.colors.GREEN
            input_usuario.value=""
            input_contraseña.value=""
        else:
            mensaje_resultado.value=f"error el usuario {usuario} ya esta registrado"
            mensaje_resultado.color=ft.colors.RED
        page.update()
    def mostrar_usuarios(e):
        usuarios=ver_usuarios()
        if usuarios:
            mensaje_resultado.value="usuarios registrados\n"+"\n".join(usuarios)
            mensaje_resultado.color=ft.colors.GREEN
        else:
            mensaje_resultado.value="no hay ningun usuario registrado"
            mensaje_resultado.color=ft.colors.RED
        page.update()
    def eliminar(e):
        usuario=input_usuario.value.strip()
        if eliminar_usuario(usuario):
            mensaje_resultado.value=f"el usuario {usuario} fue eliminado"
            mensaje_resultado.color=ft.colors.GREEN
            input_usuario.value=""
        else:
            mensaje_resultado.value=f"Error el usuario {usuario} no existe"
            mensaje_resultado.color=ft.colors.RED
        page.update()
    boton_guardar=ft.ElevatedButton(text="guardar usuario",on_click=guardar)
    boton_mostrar=ft.ElevatedButton(text="mostrar usuarios",on_click=mostrar_usuarios)
    boton_eliminar=ft.ElevatedButton(text="eliminar usuarios",on_click=eliminar)
    contenedor=ft.Column(
        [
            titulo,
            input_usuario,
            input_contraseña,
            boton_guardar,
            boton_mostrar,
            boton_eliminar,
            mensaje_resultado
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    page.add(contenedor)
ft.app(target=main)