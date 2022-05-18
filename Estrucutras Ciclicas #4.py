max = 10 
i = 0
while i <= max:
    print(f' 2 por {i} = {2**i}')
    i += 1
 #la ultima i cambia el valor de la la i de arriba ya que el codigo sube y baja
 # es decir arriba i es 0 pero se ejecuta el codigo y luego pasa a unp por que la i de aabajo es uno y asi sucesivamente de 1 en 1 o el numero que le agrege a la i   

max = 25 
i = 0
while i <= max:     
    print (f' 3 elevado a {i} = {3**i}')
    i += 5
       
#en el caso del uso de un for de range si usco print de 0 a 10 , solo printeara del  0 al 9


a = 5
b = int(input('digite el número 2: '))
salida = False

while salida == False :
    print ("""
    Menu.
    1. Suma
    2. Resta
    3. multiplicacion
    4. potencia
    0. salida
    """)
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print(a + b)
    elif opcion == 2:
        print(a - b)
    elif opcion == 3:
        print(a * b)
    elif opcion == 4:
        print(a ** b)
    elif opcion == 0:
        salida = True
    else:
        print("opcion no valida")
#Hasta que la salida de true es alli donde se termina la ejecucion del codigo      
#al final la salida es true por erso el ciclo no se vuelve a cumplir, ya que hasta hay quedari por que la salida es true y arriba debe ser false
#while true es un ciclo infinito

while True:
    print ("""
    Menu.
    1. Suma
    2. Resta
    3. multiplicacion
    4. potencia
    0. salida
    """)
    # en este caso la es infinito la ejecucion por el true
    #pero abajo el break le da un stoppor completo
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print(a + b)
    elif opcion == 2:
        print(a - b)
    elif opcion == 3:
        print(a * b)
    elif opcion == 4:
        print(a ** b)
    elif opcion == 0:
        break
    else:
        print("opcion no valida")
#el  eslse sirve para que si pongo un  numero fure de ese rango planteado debe imprimir que es no valido.


#donde dice contador lo que se us aprincipalmente es solo una letra contador = (i) la cual usualmente es iteracion
#el in permite evaluar si ua exprecion a la cual se le hace en call si esta dentro de una lista, la cual regresa verdadero si, si esta lli
for contador in range("inicio,parada,incremento"):
    print('hi bitch')



for i in range(0,10):
    print(i, end =" ")