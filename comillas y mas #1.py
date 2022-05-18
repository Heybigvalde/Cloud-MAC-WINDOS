

A = 'paragnaricutirimicuaro'
print('la posicion 4 es :',A[4])
print (A[0:6])
#se usa ese tipo de corchetes recto para la posicion
#tambien se cuenta desde 0


s = '''Hi 
how
are you ?'''   
print(s)


s = 'Hi how are you ?'
print('tipo de v es :',type(s))
#el type sirve para saber el tipo de dato



l = True
print('tipo de v es :',type(l))


d = 250
print('tipo de v es :',type(d))

g = 35.65
print('tipo de v es :',type(g))


b = input('put your name: ')
print('Bonapetito bitch',b)

ñ = eval(input ('put your age: '))
print('you have',ñ,'years old', type(ñ))
#El eval sirve para trasnformar un tipo de dato en el mejor para el codigo sin importar el dato ingrsado


print (float(5.65665465))

print (int(5.65665465))



print('Primer mensaje',end=' ')
print('Segundo mensaje', end = " " )
print('Tercer mensaje')


print('Primer mensaje', 'segundo mensaje', 'tercer mensaje')

print('Primer mensaje', 'segundo mensaje', 'tercer mensaje', sep = '-')


print('Primer mensaje', 'segundo mensaje', 'tercer mensaje', sep = '/n')
#lo que ponga entre las comillas despues del sep son el carater que va a separar

print('Primer mensaje', 'segundo mensaje', 'tercer mensaje', sep = '\n')



print ("total de estudiantes: %3.1d, niños : %2.2d" %(240 , 120))

# potencia **

print ("total de estudiantes: %4.1d, niños : %2.2d" %(240 , 120))


print ("total de estudiantes: %4.3f, niños : %1.2d" %(24550.555 , 120))
#primer numero espacios y segundo despues de la coma


print ('yo soy un aloca:%3.4s' %('alocado'))


print("numero decimal: %d, numero hexadecimal: %x, notacion cientifica: %4.2e, flag g: %4.2g" %(4869, 4869, 123654.54236, 4864.54))
#la g se usa para que acomode el ancho mas adecuado //notacion cientifica y falg aproxima de golpe

name = input("gift me your name : ")
print (f'Hola {name}, !Que dice mi perro¡')
#importancia de la f sabe que va dentro del string pero afuera de las comillas


#le puedes cambiar el valor a la variable facilmente
o =  9999
print (o)
o ='hell dath bitch'
print (o)


o =  9999
print (o,  type(o))
o ='hell dath bitch'
print (o, type (o))



#string no se puede sumar con itn asi que se le da el (int para trsnfromar el string en int)
l = 55
t = "5568"
print(l + int(t))


l = 55
t = "5568"
print(str(l) + t)
#pero cuando se cambia a str loq que suma son valores mas no hace operaciones