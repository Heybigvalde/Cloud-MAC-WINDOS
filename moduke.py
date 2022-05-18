for i in range(0,100, 10):
    print(i, end =" ")
#aqui tira el salto ya que  va del 0 al 100 pero como sabemos que el 10 es el incremento y solo llega hasta el nueve solo imprime hasta el 90 con 
#sus corrspondientes saltos de 10 en 10 el ultimo numero es el que le va a sumar
#se sabe que el numero es la condicion de parada en este caso la condicion de parada es el 100; asi que nunca se toma en cuenta


max = 20

for i in range(2, max+1):
    sw = True
    for j in range (2, i):
        if i % j == 0:
            sw = False
            break
    if sw == True:
        print (i) 


num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f'factorial de: {num} es: {fact}')
#en este casi i empieza en uno y se va sumadno de a uno 
#y el fact se multiolica por i que es las que se esta sumando
#factorial es el numero que se multiplica por todos sus anteriores


num = 6
fact = 1
for j in range(1,5):
    for i in range(j,1,-1):
        fact *= i
    print(f'facrtorial de: {j} es: {fact}')



x = 0

while x < 10:
    print (x)
    x += 1
#la operacion baja hasta que el operador while cumpla esa condicion
#el break sirve para que las funciones que estyan debajo de el no se ejecuten es como si no existieran
x = 0

while x < 10:
    if x == 5:
         break
    print (x)
    x += 1


