import json
import os

from funciones.funciones import *


def menu_principal():
    print("------|Menú Principal|------")
    print("")
    print("1. Gestión de Usuarios ")
    print("2. Gestión de Servicios ")
    print("3. Salir del Programa ")
    print("")
    print("---------------------------")

def gestion_usuarios():
    print("------|Gestión de Usuarios|------")
    print("")
    print("1. Registrar Usuario ")
    print("2. Listar Usuarios ")
    print("3. Actualizar Datos de Usuario ")
    print("4. Eliminar Usuarios ")
    print("5. Asignar Categoria")
    print("")
    print("--------------------------------")

def crear_usuario():
    print("------|Registro de Usuario|------")
    id_usuario = input("Número de Identificación: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccion = input("Dirección: ")
    telefono_celular = input("Teléfono Celular: ")
    telefono_fijo = input("Teléfono Fijo: ")

    nuevo_usuario = {
        "ID": id_usuario,
        "Nombres": nombres,
        "Apellidos": apellidos,
        "Dirección": direccion,
        "Teléfono Celular": telefono_celular,
        "Teléfono Fijo": telefono_fijo,
    }

    try:
        os.makedirs("data", exist_ok=True)  
        with open("data/usuarios.json", "r") as file:
            usuarios = json.load(file)
    except FileNotFoundError:
        usuarios = []

    usuarios.append(nuevo_usuario)

    with open("data/usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=2)

    input("Usuario creado. Presione Enter para continuar.")

def listar_usuarios():
    clear_screen()
    print("------|Lista de Usuarios|------")
    try:
        with open("data/usuarios.json", "r") as file:
            usuarios = json.load(file)
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for usuario in usuarios:
                    print("\nID:", usuario["ID"])
                    print("Nombres:", usuario["Nombres"])
                    print("Apellidos:", usuario["Apellidos"])
                    print("Dirección:", usuario["Dirección"])
                    print("Teléfono Celular:", usuario["Teléfono Celular"])
                    print("Teléfono Fijo:", usuario["Teléfono Fijo"])
                    print("-" * 40)
    except FileNotFoundError:
        print("No hay usuarios registrados.")

    input("Presione Enter para continuar.")

def eliminar_usuarios():
    print("------|Eliminar Usuario|------")
    id_usuario = input("Ingrese la ID del usuario a eliminar: ")

    try:
        with open("data/usuarios.json", "r") as file:
            usuarios = json.load(file)
        
        for usuario in usuarios:
            if usuario["ID"] == id_usuario:
                print("Datos del usuario a eliminar:")
                print("\nID:", usuario["ID"])
                print("Nombres:", usuario["Nombres"])
                print("Apellidos:", usuario["Apellidos"])
                print("Dirección:", usuario["Dirección"])
                print("Teléfono Celular:", usuario["Teléfono Celular"])
                print("Teléfono Fijo:", usuario["Teléfono Fijo"])
                print("-" * 40)
                confirmacion = input("¿Está seguro de que desea eliminar este usuario? (s/n): ").lower()
                if confirmacion == "s":
                    usuarios.remove(usuario)
                    with open("data/usuarios.json", "w") as write_file:
                        json.dump(usuarios, write_file, indent=2)
                        print("usuario eliminado correctamente.")
                        input("Presione Enter para continuar.")
                    return
                else:
                    print("Eliminación cancelada.")
                    input("Presione Enter para continuar.")
                    return
        
        print("usuario no encontrado.")
        input("Presione Enter para continuar.")
    except FileNotFoundError:
        print("No hay usuarios registrados.")
        input("Presione Enter para continuar.")
        

def modificar_usuario():
    print("------|Modificar  Usuario|------")
    id_usuario = input("Ingrese la ID del usuario a modificar: ")

    try:
        with open("data/usuarios.json", "r") as file:
            usuarios = json.load(file)
        
        for usuario in usuarios:
            if usuario["ID"] == id_usuario:
                print("Datos actuales del usuario:")
                print("\nID:", usuario["ID"])
                print("Nombres:", usuario["Nombres"])
                print("Apellidos:", usuario["Apellidos"])
                print("Dirección:", usuario["Dirección"])
                print("Teléfono Celular:", usuario["Teléfono Celular"])
                print("Teléfono Fijo:", usuario["Teléfono Fijo"])
                print("=" * 40)

                campo_modificar = input("Ingrese el campo a modificar: ")
                nuevo_valor = input(f"Ingrese el nuevo valor para {campo_modificar}: ")
                
                if campo_modificar in usuario:
                    usuario[campo_modificar] = nuevo_valor
                    with open("data/usuarios.json", "w") as write_file:
                        json.dump(usuarios, write_file, indent=2)
                        print("usuario modificado correctamente.")
                        input("Presione Enter para continuar.")
                else:
                    print(f"Campo {campo_modificar} no válido.")
                    input("Presione Enter para continuar.")
                return
        
        print("usuario no encontrado.")
        input("Presione Enter para continuar.")
    except FileNotFoundError:
        print("No hay usuarios registrados.")
        input("Presione Enter para continuar.")

def gestion_servicios():
    print("------|Gestión de Servicios|------")
    print("")
    print("1.  ")
    print("2.  ")
    print("3.  ")
    print("")
    print("----------------------------------")

def salir_programa():
    print("------|Cerrando Programa|------")
    print("")
    print("Gracias por usar nuestro programa")
    print("")
    print("       Tenga buen dia")
    print("")
    print("--------------------------------")

def asignar_usuario():
    print("------|Actualizar Usuario|------")
    print("")
    id_usuario = input("Ingrese la ID del usuario a actualizar: ")

    try:
        with open("data/usuarios.json", "r") as file:
            usuarios = json.load(file)
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for usuario in usuarios:
                    print("")

    except FileNotFoundError:
        print("No hay usuarios registrados.")

    input("Presione Enter para continuar.")