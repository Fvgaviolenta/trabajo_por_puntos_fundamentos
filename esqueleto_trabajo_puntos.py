import json
import funciones_trabajo_puntos as fn

asientos_vacios= [
    [" \n"],
    ["01","02","03"," ", " ","04","05","06","\n"],
    ["07","08","09"," ", " ","10","11","12","\n"],
    ["13","14","15"," ", " ","16","17","18","\n"],
    ["19","20","21"," ", " ","22","23","24","\n"],
    ["25","26","27"," ", " ","28","29","30","\n"],
    ["31","32","33"," ", " ","34","35","36","\n"],
    ["37","38","39"," ", " ","40","41","42","\n"]
]




while True:
    print("                    MENU                 ")
    print("******************************************")
    print("\n1. Cargar informacion de sesion anterior")
    print("2. Ver asiento disponible")
    print("3. Comprar asiento")
    print("4. Anular vuelo")
    print("5. Modificar datos de pasajero")
    print("6. Mostrar lista de pasajeros")
    print("7. Guardar informacion de esta sesion")
    print("8. Salir")
    try:
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            fn.cargar_archivo_pasajeros()
        elif opc == 2:
            fn.mostrar_asiento()
        elif opc == 3:
            fn.tomar_pasajero()
        elif opc == 4:
            fn.anular_vuelo()
        elif opc == 5:
            fn.modificar_datos_pasajero()
        elif opc == 6:
            fn.mostrar_pasajeros()
        elif opc == 7:
            fn.guardar_datos_pasajero()
        elif opc == 8:
            print("Gracias por su compra, vuelva pronto")
            break
        else:
            print("Ingrese una opcion valida\n")      
    except ValueError:
        print("Error: Ingrese una opcion valida\n")
