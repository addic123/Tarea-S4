def suma(x,y):
    sumar = x+y
    print ("Su suma es =",sumar)
def resta (x,y):
    restar = x-y
    print (" Su resta es = ",restar)
def multiplicar(x,y):
    multiplicarr= (x*y)
    print (" su multplicacion es =",multiplicarr)
def dividir(x,y):
 dividirr = int (x/y)
 print (" Su divicion es =",dividirr)

print ("##Calculadora Sencilla##")    
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

Opcion = int(input("elija una opcion:"))
if (Opcion ==1):
   Digito1 = int(input("Coloque el primer digito a sumar"))
   Digito2 = int(input("Coloque el segundo digito a sumar"))
   suma(Digito1,Digito2)

if (Opcion ==2):
   Digito1 = int(input("Coloque el primer digito a restar"))
   Digito2 = int(input("Coloque el segundo digito a restar"))
   resta(Digito1,Digito2)

if (Opcion ==3):
   Digito1 = int(input("Coloque el primer digito a multiplicar"))
   Digito2 = int(input("Coloque el segundo digito a multiplicar"))
   multiplicar(Digito1,Digito2)

if (Opcion ==4):
   Digito1 = int(input("Coloque el primer digito a dividir"))
   Digito2 = int(input("Coloque el segundo digito a dividir"))
   dividir(Digito1,Digito2)

