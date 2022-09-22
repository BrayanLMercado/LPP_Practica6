'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 6: Modulos y Funciones
Ejercicio 1: Crea un módulo llamado prac5.py con 4 de los programas creados
             en la práctica anterior (practica 5).
Fecha: 29 De Septiembre De 2022
'''

def entrada(edad):
    if edad<15:
        print("Lo Sentimos, Pero No Puedes Entrar A La Fiesta")
    elif edad==15:
        print("Puedes Entrar A La Fiesta Gratis")
    else:
        print("Puedes Entrar, Pero Necesitas Un Regalo")

def opcPago1 (costo,ingresos):
    enganche=costo*0.15
    pagoRestante=costo-enganche
    mensualidadesTotales=12*15
    pagoMensual=pagoRestante/mensualidadesTotales
    print("Monto De Enganche:",enganche)
    print(mensualidadesTotales,"Mensualidades Requeridas De",round(pagoMensual,2))

def opcPago2 (costo,ingresos):
    enganche=costo*0.30
    pagoRestante=costo-enganche
    mensualidadesTotales=12*7
    pagoMensual=pagoRestante/mensualidadesTotales
    print("Monto De Enganche:",enganche)
    print(mensualidadesTotales,"Mensualidades Requeridas De",round(pagoMensual,2))

def acceso (user,password):
    print("2 Horas Más Tarde...")
    usuario=str(input("Nombre De Usuario: "))
    contrasena=str(input("Contraseña: "))
    intentos=1
    if usuario!=user or contrasena!=password: # Si Los Datos No Coinciden
        while (usuario!=user or contrasena!=password) and intentos<4: # Ciclo Para Seguir Intentando
            print("Información Incorrecta")
            usuario=str(input("Nombre De Usuario: "))
            contrasena=str(input("Contraseña: "))
            intentos+=1
            if intentos==4:
                print("No Se Puede Acceder A La Cuenta")
                break
            elif usuario==user and contrasena==password: # Se Muestra Cuando Los Datos Coinciden
                print("Feliz Inicio De Sesión")
    else:
        print("Feliz Inicio De Sesión")

def factorial(num):
    n=1
    fact=1
    while n<num+1:
        fact*=n
        n+=1
    return fact
