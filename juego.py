import time
nombre = input("¿como te llamas? ")
print(" ")
print ("Hola, "+nombre," bienvenido, es hora de jugar el ahorcado")
print(" ")
print("tu palabra tiene 6 letras")
print (" ")
print ("tiene 3 letras vocales y 3 letras consonante")
print(" ")
print("solo tienes 3 vidas ")
print("")
time.sleep(1)
print("comienza a adivinar te deseo suerte")
time.sleep(0.5)

palabra='zapato'
tupalabra=''
vidas=3

while vidas > 0:
    fallas=0
    print("")
    for letra in palabra:
        if letra in tupalabra:
            print (letra,"")
        else:
            print ("*",end="")
            fallas+=1

        if fallas == 0:
            print("felicidades, ganaste muy bien")
        break

 
tuletra=input("introduce tu letra")
tupalabra+=tuletra

if tuletra not in palabra:
    vidas-= 1
    print("equivocaciones")
    print("tu tienes ",+vidas," vidas")
if vidas == 0:  
   print("lo siento perdiste")
else:
    print("gracias por participar sera para la proxima")
    