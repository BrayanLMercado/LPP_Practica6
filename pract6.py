'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 6: Modulos y Funciones
Ejercicio 2: Crea un módulo llamado prac6.py utilizando los programas solicitados a continuación:
                a. Crea un programa que capture 10 números e imprima el numero mayo, el menor y la media.
                b. Crea un programa que capture 5 calificaciones y retorne el promedio.
                c. Crea un programa que capture dos números y a través de una función calcule el máximo
                   común divisor de dos números y este elemento sea retornado.
Fecha: 29 De Septiembre De 2022
'''

from pract5 import*

def Ejercicio_A_Main():
    lista=[]
    for x in range(10):
        num=float(input("Captura Un Número: "))
        lista.append(num)
    print("El Número Mayor Es:",mayor(lista))
    print("El Número Menor Es:",menor(lista))
    print("El Promedio Es:",promedio(lista))

def Ejercicio_B_Main():
    lista=[]
    for x in range(5):
        calif=float(input("Captura La Calificación: "))
        while calif<0 or calif>100:
            print("Captura Una Calificación Valida")
            calif=float(input("Captura La Calificación: "))
        lista.append(calif)
    print("El Promedio De Las Calificaciones Es:",promedio(lista))

def Ejercicio_C_Main():
    num1=int(input("Captura Un Número Entero: "))
    num2=int(input("Captura Un Número Entero: "))
    print("El Máximo Cómun Divisor De",num1, "y", num2, "Es",MCD(num1,num2))

def mainPract5(opc):
    if opc==1:
        num=int(input("Captura Un Número: "))
        print("El Factorial De",num,"Es",factorial(num))
    elif opc==2:
        edad=int(input("¿Cuantos Años Tienes? "))
        while edad<0 :
            print("Captura Una Edad Valida")
            edad=int(input("¿Cuantos Años Tienes? "))
        entrada(edad)
    elif opc==3:
            ingresos=float(input("Ingresos Al Mes: "))
            costo=float(input("Costo De La Casa Que Desea Comprar: "))
            while ingresos<0 or costo<0:
                print("Captura Valores Validos")
                ingresos=float(input("Ingresos Al Mes: "))
                costo=float(input("Costo De La Casa Que Desea Comprar: "))
            if ingresos<=8000:
                opcPago1(costo,ingresos)
            else:
                opcPago2(costo,ingresos)
    elif opc==4:
        user=str(input("Nombre Del Nuevo Usuario: "))
        password=str(input("Contraseña Del Nuevo Usuario: "))
        acceso(user,password)

def mayor(lista):
    mayor=lista[0]
    for x in lista:
        if x>mayor:
            mayor=x
    return mayor

def menor(lista):
    menor=lista[0]
    for t in lista:
        if t<menor:
            menor=t
    return menor

def promedio(lista):
    suma=0
    size=0
    for y in lista:
        suma+=y
        size+=1
    promedio=suma/size
    return round(promedio,2)

def MCD(num1,num2):
    if num1==0:
        return num2
    return MCD(num2%num1,num1)

def menu():
    print("                   ** Menu **         ")
    print("1) Factorial De Un Número")
    print("2) Entrada A La Fiesta")
    print("3) Compra De Casas Y Mesualidades")
    print("4) Usuario y Contrseña")
    print("5) Numero Mayor, Menor y Promedio De 10 Números")
    print("6) Promedio De 5 Calificaciones")
    print("7) Máximo Cómun Divisor De 2 Números")
    print("8) Salir")
