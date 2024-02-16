from funciones.funciones import *
from menus.menus import *
from funciones.test import *

    

while True:
    clear_screen()
    menu_principal()
    opc=verify_opc("Digite su opción ",1,3)

    if opc==1:
        clear_screen()
        gestion_usuarios()
        ops=verify_opc("Digite su opción ",1,4)
        if ops==1:
            clear_screen()
            crear_usuario()
        if ops==2:
            clear_screen()
            listar_usuarios()
        if ops==3:
            clear_screen()
            modificar_usuario()
        if ops==4:
            clear_screen()
            eliminar_usuarios()
        if ops==5:
            menu_principal()
    if opc==2:
        clear_screen()
        gestion_servicios()
        opt=verify_opc("Digite su opción ",1,4)
        if opt==1:
            clear_screen()
            serv_pospago()
            opv=verify_opc("Digite su opción ",1,4)
            
        if opt==2:
            clear_screen()
            serv_prepago()
        if opt==3:
            clear_screen()
            menu_principal()
    if opc==3:
        clear_screen()
        salir_programa()
        break
