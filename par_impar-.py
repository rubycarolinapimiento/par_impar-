x = int(input("Ingresa un numero: "))

r = x%2
if x % 2 == 0: 
    msj = "PAR "
else: 
    msj = "IMPAR "

print("El numero " + str(x) + " es " + msj)
    