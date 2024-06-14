import json
banderaRut=False
datos_pasajeros = []
precio_norm = 78900
precio_vip = 240000



asientos= [
    [" \n"],
    ["01","02","03"," ", " ","04","05","06","\n"],
    ["07","08","09"," ", " ","10","11","12","\n"],
    ["13","14","15"," ", " ","16","17","18","\n"],
    ["19","20","21"," ", " ","22","23","24","\n"],
    ["25","26","27"," ", " ","28","29","30","\n"],
    ["31","32","33"," ", " ","34","35","36","\n"],
    ["37","38","39"," ", " ","40","41","42","\n"]
]
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

def guardar_datos_pasajero():
    with open("datos_pasajeros.json", "w") as archivo:
        json.dump(datos_pasajeros,archivo)
        print("JSON creado con exito")
        
def cargar_archivo_pasajeros():
    try:
        with open("datos_pasajeros.json", "r") as archivo:
            global datos_pasajeros
            datos_pasajeros = json.load(archivo)
            print("Datos cargados con exito")
            for diccionario in datos_pasajeros:
                for i in diccionario.values():
                    if i == diccionario["Asiento"]:
                        for j in asientos:
                            for z in j:
                                if i == z:
                                    asientos[asientos.index(j)][j.index(z)] = 'x' 
    except FileNotFoundError:
        print("No se encuentran datos guardados")
                        
                            
        

def mostrar_asiento():
    for fila in asientos:
        for elemento in fila:
            print(elemento,end=" ")

def tomar_pasajero():
    nombre_pasajero=input("Ingrese su nombre completo: ")
    while True:
        try:
            rut=input("Ingrese nº rut sin guión ni puntos (Ej: 10078257k): ")
            if len(rut)==9 or len(rut)==8:
                rut_invertido=""
                if len(rut)==9:
                    for i in rut:
                        rut_invertido=i+rut_invertido
                        #return rut_invertido
                elif len(rut)==8:
                    rutCompleto="0"+rut
                    for i in rutCompleto:
                        rut_invertido=i+rut_invertido
                        #return rut_invertido
                a=int(rut_invertido[1])*2
                b=int(rut_invertido[2])*3
                c=int(rut_invertido[3])*4
                d=int(rut_invertido[4])*5
                e=int(rut_invertido[5])*6
                f=int(rut_invertido[6])*7
                g=int(rut_invertido[7])*2
                h=int(rut_invertido[8])*3
                sumaRut=(a+b+c+d+e+f+g+h)/11
                sumaRut2=int(sumaRut)
                sumaRutfinal=(a+b+c+d+e+f+g+h)-(sumaRut2*11)
                dig_verificador=11-sumaRutfinal
                dig_verificador=str(dig_verificador)
                if dig_verificador=="11":
                    dig_verificador="0"
                elif dig_verificador=="10":
                    dig_verificador="k"
                if len(rut)==9:
                    if rut[8]==dig_verificador:
                        break
                    else: 
                        print("Rut inválido")
                elif len(rut)==8:
                    if rutCompleto[8]==dig_verificador:
                        banderaRut=1
                        break
                    else: 
                        print("Rut inválido")
                else:
                    print("Rut inválido")
            else:
                print("Rut inválido")
        except ValueError:
                    print("Error: Ingrese un rut valido")

        #banco_pasajero = input("Ingrese el banco con el que va a pagar (Ej: Banco Santander): ").upper()
    while True:
        try:
            telefono_pasajero = int(input("Ingrese número de teléfono (Ej: 963214683): "))
            telefono_pasajero_str = str(telefono_pasajero)
            if telefono_pasajero < 900000000 and telefono_pasajero > 999999999:
                print("Ingrese un formato de telefono valido porfavor")
            else:
                if telefono_pasajero_str.startswith("9"):
                    #print("Numero de telefono valido.")
                    break
                else:
                    print("Ingrese un número de telefono no válido")
        except ValueError:
            print("Error: Ingrese un formato de teléfono válido")

    banco_pasajero = input("Ingrese el banco con el que realizará el pago (Ej: Banco Santander): ").upper()

    while True:
        try:
            for fila in asientos:
                for elemento in fila:
                    print(elemento,end=" ")
            asiento_pasajero = input("Ingrese el asiento que desea comprar: ")
            asiento_encontrado = False
            for filaA in asientos:
                for columnaA in filaA:
                    if columnaA==asiento_pasajero:
                        asientos[asientos.index(filaA)][filaA.index(columnaA)]="X"
                        asiento_encontrado = True
            if asiento_encontrado==True:
                if int(asiento_pasajero) <= 30:
                    vip = False
                else:
                    vip = True
                print("Asiento disponible, ha quedado reservado para ti")
                break
            else:
                print("Asiento no encontrado, seleccione otro")     
        except ValueError:
            print("Error:Asiento inválido porfavor ingrese un asiento válido")
        
    if vip == True:
        pasajero_vip = "Si"
    else:
        pasajero_vip = "No"

    if vip == True:
        print(f"El precio final de su pasaje con asiento VIP es de ${precio_vip}")
    else:
        print(f"El precio final de su pasaje con asiento normal es de ${precio_norm}")
        
    if banco_pasajero == "BANCO DUOC":
        print("Se a detectado un descuento del 15% por ser socio del banco DUOC")
        if vip == True:
            descuento = precio_vip * 0.15
            precio_vip_desc = precio_vip - descuento
            precio_vip_desc = int(precio_vip_desc)
            print(f"El precio final de su pasaje con el descuento aplicado es de ${precio_vip_desc}\n")
        else:
            descuento = precio_norm * 0.15
            precio_norm_desc = precio_norm - descuento
            precio_norm_desc = int(precio_norm_desc)
            print(f"El precio final de su pasaje con el descuento aplicado es de ${precio_norm_desc}\n")
    else:
        print("No se detecto ningun descuento")
        
    while True:
        opc3 = input("Desea confirmar el monto (Si/No)? ").upper()
        if opc3 == "SI":
            print("Gracias por su compra, vuelva pronto!")
            dict_datos_pasajero = {
                "Nombre":nombre_pasajero,
                "RUT":rut,
                "Telefono":telefono_pasajero,
                "Banco":banco_pasajero,
                "Asiento":asiento_pasajero,
                "VIP":pasajero_vip
            }
            datos_pasajeros.append(dict_datos_pasajero)
            break
        elif opc3 == "NO":
            print("Compra cancelada volviendo al menu principal...")
            for filaAA in asientos_vacios:
                for columnaAA in filaAA:
                    if columnaAA==asiento_pasajero:
                        asientos[asientos_vacios.index(filaAA)][filaAA.index(columnaAA)]=asientos_vacios[asientos_vacios.index(filaAA)][i.index(columnaAA)]
                        print(columnaAA)
            break
        else: 
            print("Error: Ingrese una opcion valida")
    
def mostrar_pasajeros():
    print(datos_pasajeros)

def anular_vuelo():
    try:
        rut_pasajero = input("Ingrese el rut del pasajero del vuelo que desea cancelar: ")
        asiento_pasajero = input("Ingrese el asiento correspondiente a su rut: ")
        
        for diccionario in datos_pasajeros:
            if diccionario["RUT"] == rut_pasajero and diccionario["Asiento"] == asiento_pasajero:
                for i in asientos_vacios:
                    for j in i:
                        if j==asiento_pasajero:
                            asientos[asientos_vacios.index(i)][i.index(j)]=asientos_vacios[asientos_vacios.index(i)][i.index(j)]
                datos_pasajeros.remove(diccionario)
          
                break
            else:
                print("RUT y asiento no coinciden")    
            
                    
    except ValueError:
        print("Error: formato de rut invalido") 

def modificar_datos_pasajero():
    rut_pasajero = input("Ingrese el rut del pasajero del vuelo que desea modificar datos: ")
    asiento_pasajero = input("Ingrese el asiento correspondiente a su rut: ")
    
    for diccionario in datos_pasajeros:
        if diccionario["RUT"] == rut_pasajero and diccionario["Asiento"] == asiento_pasajero:
            while True:
                print("\nMenu de cambio de datos")
                print("1. Cambiar nombre")
                print("2. Cambiar Telefono")
                print("3. Salir")
                try:
                    opc1 = int(input("Ingrese el dato que desea modificar:"))
                    if opc1 == 1:
                        nuevo_nombre_pasajero = input("Ingrese nuevo nombre: ")
                        diccionario["Nombre"] = nuevo_nombre_pasajero
                        print("Nombre cambiado con éxito\n")
                    elif opc1 == 2:
                        try:
                            nuevo_fono_pasajero = int(input("Ingrese nuevo número de telefono: "))
                            if nuevo_fono_pasajero < 900000000 and nuevo_fono_pasajero > 999999999:
                                diccionario["Telefono"] = nuevo_fono_pasajero
                                print("Número de teléfono cambiado con éxito")
                        except ValueError:
                            print("Error: Ingrese un formato de numero valido")
                    elif opc1 == 3:
                        print("Volviendo al menu principal")
                        break
                    else:
                        print("Ingrese una opción válida\n")
                except ValueError:
                    print("Error: Ingrese una opcion válida")
