'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 6: Modulos y Funciones
Ejercicio 3:Crear un archivo llamado prac6_main.py en el cual a través de la ayuda de un menú se mandarán a
            llamar los módulos prac5 y prac6 con sus respectivos programas. 
Fecha: 29 De Septiembre De 2022
'''
from pract6 import*

continuar=7
while continuar!=8:
    menu()
    opc=int(input("Selecciona Una Opción: "))
    while opc<0 or opc>8:
        print("Captura Una Opción Valida")
        opc=input("Selecciona Una Opción: ")
    if opc<=4:
        mainPract5(opc)
    elif opc==5:
        Ejercicio_A_Main()
    elif opc==6:
        Ejercicio_B_Main()
    elif opc==7:
        Ejercicio_C_Main()
    elif opc==8:
        print("Gracias Por Usar El Programa")
        continuar=8
        break
    continuar=int(input("¿Quieres Usar El Programa Otra Vez? Presiona 8 Para Salir "))
    if continuar==8:
        print("Gracias Por Usar El Programa")
    print()
        