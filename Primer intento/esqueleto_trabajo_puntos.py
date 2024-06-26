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
    print("1. Ver asiento disponible")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    # print("5. Mostrar lista de pasajeros")
    print("5. Salir")
    try:
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            fn.mostrar_asiento()
        elif opc == 2:
            fn.tomar_pasajero()
        elif opc == 3:
            fn.anular_vuelo()
        elif opc == 4:
            fn.modificar_datos_pasajero()
        # elif opc == 5:
        #     fn.mostrar_pasajeros()
        elif opc == 5:
            fn.guardar_datos_pasajero()
            print("Gracias por su compra, vuelva pronto")
            break
        else:
            print("Ingrese una opcion valida\n")      
    except ValueError:
        print("Error: Ingrese una opcion valida\n")