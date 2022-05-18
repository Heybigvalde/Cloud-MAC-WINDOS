#  Jerarquia de los operadore importante: de izquierda a derecha * | / | % | + | - |

#Orden de operadore
#parentesis
#potencia
#multiplicacion y division
#suma y resta
# ((2**3*(8**(1/2)/54))+5.8)/(45-654)


num = eval(input('put a number :'))
if num > 0:
    num += 2
    print(f'{num}  is positive', num)
#se usa s para facilitar y es recomendable la f por codigo limpio

    
num = eval(input('put a number :'))
if num > 0:
    print (f'{num}  is positive' )


num = int(input('put a number :'))
if num > 0:
    print (f'{num}  is positive' )
#codigo da un error si pogo un decial ya que declaro que entre un int mejor eval ya que probablemente el usuario pueda no saber


num = eval(input('put a number :'))
if num > 0:
    print (f'{num}  is positive' )
#si pongo un numero negativo no realiza nada ya que rompe con la funcion
#if suempre debajo de if

num = eval(input('put a number :'))
if num > 0:
    print (f'{num}  is positive' )
if num < 0:
    print (f'{num}  is negative' )    

#eval solo evalua los tipos de datos de numeros no string or other
#else es basicamente si no



num = eval(input('put a number :'))
if num > 0:
    print (f'{num}  is positive' )
else:
    print (f'{num}  is negative' )
#con el ese no debo poner otra condicion simplemente imvierte la anterior
#else si no acaba directamente 


num = eval(input('put a number :'))
if num > 0:
    print (f'{num}  is positive' )
else:
    print (f'{num}  is negative' )
#else tambien da una especie de igual que
#se puede tener else sin un if pero no un if sin un else


num = 0
if num > 0:
    print (f'{num}  is positive' )
if num == 0:
    print(f'{num}  is zero' )    
else:
    print (f'{num}  is negative' )



num = 58
if num > 0:
    print (f'{num}  is positive' )
if num == 0:
    print(f'{num}  is zero' )
else:
    print (f'{num}  is negative' )
#en este caso como es mayor que 0 imprime, luego no es igual a cero entonces condiciona que si no es igual a cero entonces imprima que es negativo



num = eval(input('put a number :'))
if num > 0:
    print (f'{num}  is positive' )
elif num == 0:
    print(f'{num}  is zero' )
else:
    print (f'{num}  is negative' )
#cone el elifa cambia a que solo si se cumple la de arriba para printea y no sigue verificando es decir si le da true
#si no va a seguir verificando es como un stop




#slistas de los MENUS
u = eval(input('put a number :'))
t = eval(input('put a number :'))
print ('''
MENU
1. Add 
2. Subtract
3. Multiply
4. Divide
5. Exit
''')
op = int(input('Enter your choice: '))
if op == 1:
    print(u + t)
elif op == 2:
    print(u - t) 
elif op == 3:
    print(u * t)
elif op == 4:
    print(u / t)
elif op == 5:
    print('Exit bye bitch')
else:
    print('Invalid input')
#SE PONE ELIF ya que corta en solo la opcion que le den con else de seguiria dando y preguntando
#else se usa para decir que no es ya que puso una letra o algo que no esta dentro del menu



num = 654
if num % 2 == 0 :
    print (f'{num} El numero es un par ')
else:
    print (f'{num} El numero es un impar ')

    
num = 654
if num % 2 == 0 :
    if num % 5 == 0:
        print (f'{num} El numero es un par y multiplo de 5 ')
    else:
        print (f'{num} El numero es un par ')
else:
    if num % 3 == 0 :  
        print (f'{num} El numero es un impar y multiplo de 3 ')
    else:
        print (f'{num} El numero es un impar ')
# solo se ejecuta una linea de codigo es decir estra correcta solo que por acciones anteriores no muestra

num = 650
if num % 2 == 0 :
    if num % 5 == 0:
        print (f'{num} El numero es un par y multiplo de 5 ')
    else:
        print (f'{num} El numero es un par ')
else:
    if num % 3 == 0 :  
        print (f'{num} El numero es un impar y multiplo de 3 ')
    else:
        print (f'{num} El numero es un impar ')
#par y mismo multiplo de 5

num = 27
if num % 2 == 0 :
    if num % 5 == 0:
        print (f'{num} El numero es un par y multiplo de 5 ')
    else:
        print (f'{num} El numero es un par ')
else:
    if num % 3 == 0 :  
        print (f'{num} El numero es un impar y multiplo de 3 ')
    else:
        print (f'{num} El numero es un impar ')
#27 es impar y divisible por 3

num = 29
if num % 2 == 0 :
    if num % 5 == 0:
        print (f'{num} El numero es un par y multiplo de 5 ')
    else:
        print (f'{num} El numero es un par ')
else:
    if num % 3 == 0 :  
        print (f'{num} El numero es un impar y multiplo de 3 ')
    else:
        print (f'{num} El numero es un impar ')
# es impar 


num = int(input("digite un número: "))
if num % 2 == 0 and num % 5 == 0:
    print(f"{num} es un número par y múltiplo de 5")
else:
    print(f"{num} el número no cumple la condición")
    


a = float(input('digite el número 1: '))
b = float(input('digite el número 2: '))
print(
    """Menú:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Módulo
    6. Potencia
""")
opcion = int(input('Digite la opción: '))
if(opcion == 1):
    print(f"{a} + {b} = ", a + b)
elif(opcion == 2):
    print(f"{a} - {b} = ", a - b)
elif(opcion == 3):
    print(f"{a} * {b} = ", a * b)
elif(opcion == 4):
    print(f"{a} / {b} = ", a / b)
elif(opcion == 5):
    print(f"{a} % {b} = ", a % b)
elif(opcion == 6):
    print(f"{a} ^ {b} = ", a ** b)
else:
    print("opción inválida")