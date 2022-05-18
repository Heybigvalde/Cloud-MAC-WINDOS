a  = 40
b = 7
c = a / b
print(c) 
#si es decimal lo entrega asi

a  = 40
b = 7
c = a // b
print(c) 
#el resultado lo entrega en numero entero

a  = 40
b = 7
c = a * b
print(c)


a  = 40
b = 7
c = a ** b
print(c) 

a  = 35
b = 7
c = a % b
print(c) 


a  = 405554
b = 7555
c = a % b
print(c) 
#siempre va a ser entero

a  = 40556165.6655
b = 7514.666
c = a % b
print(c) 
#no va a ser tan acertado ya que el codigo solo trabaj con 0 y 1

#==
# !=
#<
#>
#<=
#>=


x = 70.5
z = 40
print(x == z)


x = 70.5
z = 70.5
print(x == z)

x = 70.5
z = 40
print(x != z)

x = 45
z = 45
print(x > z)
#x es mayor que z

x = 70.5
z = 40
print(x < z)
#x es menor que z

x = 44.999999
z = 45
print(x >= z)

x = 45
z = 45
print(x <= z)

x = 70.5
z = 40.5
print(x >= z)


p = True    
q = False
print(p and q)
#False

p = True    
q = True
print(p and q)
#True

p = True    
q = False
print(p or q)
#es verdadero si almenos una de los 2 es verdadera

p = False
q = False
print(p and q)
#false por que ninguna es verdadera

p = False    
q = False
r = True
print(p and q or r)


p = False    
q = False
r = True
print(not p)
#la negacion de un falso es verdadera

p = False    
q = False
r = True
print(not r)
#la negaciion de un verdadero es falso

p = False    
q = False
r = True
print(p is  not True)

p = False    
q = False
r = True
print(r is not True)

###############################################################################################################

h = 10
print (h)

h += 1
print (h)
#se suma el numero que se ponga puede ser todos eje 23


h -= 2
print (h)

h *= 4
print (h)


h /= 6
print (h)

h //= 2
print (h)
#division entere siempre va a ser entero  en este caso no ya que lleva una previas

h %= 3
print (h)