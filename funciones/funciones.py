import os
import json

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def verify_opc(enunciado, bajo, top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Opcion no esta en el intervalo de ({bajo}-{top})")
        except ValueError:
            print("Por favor, digite un numero valido")

