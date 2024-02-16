class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, id, nombre, email):
        usuario = Usuario(id, nombre, email)
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Email: {usuario.email}")

    def buscar_usuario_por_id(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None

    def modificar_usuario(self, id, nombre, email):
        usuario = self.buscar_usuario_por_id(id)
        if usuario:
            usuario.nombre = nombre
            usuario.email = email
            print("Usuario modificado con éxito.")
        else:
            print("Usuario no encontrado.")

    def eliminar_usuario(self, id):
        usuario = self.buscar_usuario_por_id(id)
        if usuario:
            self.usuarios.remove(usuario)
            print("Usuario eliminado con éxito.")
        else:
            print("Usuario no encontrado.")

# Función principal del programa
def main():
    sistema = SistemaUsuarios()

    while True:
        print("\nMenú:")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Modificar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            email = input("Ingrese el email del usuario: ")
            sistema.agregar_usuario(id, nombre, email)

        elif opcion == "2":
            sistema.listar_usuarios()

        elif opcion == "3":
            id = input("Ingrese el ID del usuario a modificar: ")
            nombre = input("Ingrese el nuevo nombre del usuario: ")
            email = input("Ingrese el nuevo email del usuario: ")
            sistema.modificar_usuario(id, nombre, email)

        elif opcion == "4":
            id = input("Ingrese el ID del usuario a eliminar: ")
            sistema.eliminar_usuario(id)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
