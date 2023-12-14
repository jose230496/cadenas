import os
os.system('cls')
mensaje = "fundamentos de programacion"
contadorConsonantes =int(0)
vocales =int(0)
lstvocales = " a,e,i,o,u"
for caracter in mensaje:
    if caracter in lstvocales:
          vocales +=1
    elif caracter.isalpha():
            if 'a' in "a,e,i,o,u":
                print ('hay vocales')
    if 'a' in "a,b,c,d,e,f,g,h,i,j,k,l,ll,m,n,o,p,q,r,s,t,u,v,w,x,y,z":
        print ('hay consonantes ')

    else:
        consonantes +=1
        print(f"el total de vocales es = {vocales}")
        print(f"el total de las consonantes es = {consonantes} ")
        for item in range (0.5):
            print(iten)

        for i,item in  enumerate (mensaje):
            print(f"Pos {i} - {item}")
        mensaje. replace(item)
        print


#for caracter in mensaje
#   print (caracter)
