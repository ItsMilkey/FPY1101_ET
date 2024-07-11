import os
import time
import csv
import random

def media(data):
    producto = 1
    for valor in data:
        producto *= valor
    return valor **(1/len(data))

def limpieza():
    clean = 'cls'
    os.system(clean)
    time.sleep(0.5)

def mensaje_salida():
    limpieza()
    print("Finalizando programa\nDesarrollado por Hans Gómez\nRUT 20.846.856-1")

trabajadores = ["Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos_base = {
    "Juan Pérez": [],
    "María García": [],
    "Carlos López": [],
    "Ana Martínez": [],
    "Pedro Rodríguez": [],
    "Laura Hernández": [],
    "Miguel Sánchez": [],
    "Isabel Gómez": [],
    "Francisco Díaz": [],
    "Elena Fernández": []
}
matriz = [
    ["Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"],
]
sueldos = []
def generador_sueldos():
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        sueldos_base[trabajador].append(sueldo)
        matriz.append(sueldo)
        sueldos.append(sueldo)
    print(matriz)
    print(sueldos)
    print("Se han generado los sueldos satisfactoriamente.")   

def clasificacion_sueldos():
    menor_800 = matriz.index(min)
    print(f"Sueldos menores a $800.000 - TOTAL = {len(menor_800)}\nNombre Empleado\tSueldo\n")
    print(matriz[menor_800])
    #
    #for trabajadores,sueldos in sueldos_base.items():
        #for sueldo in range(sueldos):
            #cantidad_trabajadores_menor800 = trabajadores
            #print(f"Sueldos menores a $800.000 - TOTAL = {len(cantidad_trabajadores_menor800)}\nNombre Empleado\tSueldo\n")
            #for trabajador in trabajadores:
                #print(f"{trabajador}\t{sueldo}")

def datos():
    for i in matriz[:11]:
        nombre_empleado = i
    for i in matriz[1:11]:
        sueldo_base = i
        descuento_salud = sueldo_base * 0.07
        descuento_afp = sueldo_base * 0.12
        sueldo_liquido = sueldo_base - (descuento_afp+descuento_salud)
    return nombre_empleado, sueldo_base, descuento_afp, descuento_salud, sueldo_liquido
    
    
def registro_csv(nombre_empleado,sueldo_base,descuento_salud,descuento_afp,sueldo_liquido,archivo_csv='Reporte_sueldos.csv'):
    with open(archivo_csv,'a',newline='')as f:
        campos = ['Nombre empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Líquido']
        escritor = csv.DictWriter(f,fieldnames=campos)
        if f.tell()==0:
            escritor.writerow({
                'Nombre empleado':nombre_empleado,
                'Sueldo Base':sueldo_base,
                'Descuento Salud': descuento_salud,
                'Descuento AFP':descuento_afp,
                'Sueldo Líquido':sueldo_liquido
            })

def leercsv(archivo_csv='Reporte_sueldos.csv'):
    if os.path.exists(archivo_csv):
        with open(archivo_csv,'r')as f:
            lector = csv.reader(f)
            for fila in lector:
                print(fila)
    else:
        print("El archivo no existe.")

def opcion4():
    res = datos()
    if res:
        nombre_empleado,sueldo_base,descuento_salud,descuento_afp,sueldo_liquido = res
        registro_csv(nombre_empleado,sueldo_base,descuento_salud,descuento_afp,sueldo_liquido)
        leercsv()
        

def menu_principal():    
    while True:
        try:
            opc = int(input(("-----------Menú Principal-----------\n1) Asginar sueldos aleatorios\n2) Clasificar sueldos\n3) Ver estadísticas\n4) Reporte de sueldos\n5) Salir del programa\nSeleccione una opción: ")))
            if opc == 1:
                limpieza()
                generador_sueldos()
            elif opc == 2:
                clasificacion_sueldos()
            elif opc == 3:
                print("")
            elif opc == 4:
                limpieza()
                opcion4()
            elif opc == 5:
                mensaje_salida()
                break
            else:
                print("Elija opción entre 1-5")
        except ValueError:
            print("Dato ingresado inválido, intente nuevamente.")

menu_principal()
        
        