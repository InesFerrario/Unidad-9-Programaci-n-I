# Ejercicio 1
#print("_"*40, "\n")
#print(f"Actividad 1\n")
#print("¡Hola!\n")

#def factorial(num):
#    if num==0 or num==1:
#        return 1
#    else:
#        return num*factorial(num-1)
     
#def validar_entero_positivo_1a998():
#    valido=False
#    while not valido:
#        num=input().strip()
#        try:
#            numero=int(num)
#            if 0<numero<999:  
#                return numero
#            else:
#                print(f"Disculpe, pero {numero} no es un número entero entre 1 y 998, intente nuevamente: ", end="")
#        except ValueError:
#            print("Disculpe, pero no ha ingresado un número entero entre 1 y 998, intente nuevamente: ", end="")

#print("Ingrese un número entero entre 1 y 998 para calcular el factorial desde 1 hasta ese número: ", end="")
#numero=validar_entero_positivo_1a998()
#for i in range(1,numero+1):
#    print(f"El factorial de {i} es: {factorial(i)}")

#print("\n¡Muchas gracias y hasta luego!\n")



#Ejercicio 2
#print("_"*40, "\n")
#print(f"Actividad 2\n")
#print("¡Hola!\n")

#def fibonacci(num):
#    if num==0:
#        return 0
#    elif num==1:
#        return 1
#    else:
#        return fibonacci(num-1)+fibonacci(num-2)
    
#print(f"Ingresa un número entero entre 1 y 35 para ver la serie de Fibonacci hasta esa posición: ", end="")   
#def validar_entre_1y35():
#    valido=False
#    while not valido:
#        num=input().strip()
#        try:
#            numero=int(num)
#            if 0<numero<36:   
#                return numero
#            else:
#                print(f"Disculpe, pero {numero} no es un número entero entre 1 y 35, intente nuevamente: ", end="")
#        except ValueError:
#            print("Disculpe, pero no ha ingresado un número entero entre 1 y 35, intente nuevamente: ", end="")

#numero=validar_entre_1y35()

#print(f"\nLa serie de Fibonacci hasta la posición {numero} es: ", end="")
#for i in range(numero):   
#    print(f"{fibonacci(i)} ", end="") 

#print("\n¡Muchas gracias y hasta luego!\n")



# Ejercicio 3.
#print("_"*40, "\n")
#print(f"Actividad 4\n")
#print("¡Hola!\n")

#def potencia(bas,exp):
#    if exp<0 and bas!=0:
#        return 1/potencia(bas,-exp)
#    elif bas==0:
#        if exp==0:
#            return "Indeterminado"
#        elif exp<0:
#            return "No se puede dividir entre 0"
#        else:
#            return 0
#    elif bas==1 or exp==0:
#        return 1
#    else:
#       return bas*potencia(bas,exp-1)

#print("\nProbando la función de potencia usando recursividad:")    
#print(f"2 elevado a la 6: {potencia(2,6)}")
#print(f"0 elevado a la 0: {potencia(0,0)}")
#print(f"0 elevado a la 5: {potencia(0,5)}")
#print(f"1 elevado a la 0: {potencia(1,0)}")
#print(f"1 elevado a la 45: {potencia(1,45)}")
#print(f"-1 elevado a la 45: {potencia(-1,45)}")
#print(f"-3 elevado a la 4: {potencia(-3,4)}")
#print(f"-3 elevado a la 3: {potencia(-3,3)}")
#print(f"2 elevado a la -1: {potencia(2,-1)}")
#print(f"2 elevado a la -3: {potencia(2,-3)}")
#print(f"1 elevado a la -1: {potencia(1,-3)}")
#print(f"0 elevado a la -4: {potencia(0,-4)}")

#print("\n¡Muchas gracias y hasta luego!\n")



# Ejercicio 4.
#print("_"*40, "\n")
#print(f"Actividad 4\n")
#print("¡Hola!\n")

#def convertir_a_binario(decimal):
#    if decimal<0:
#        return "Disculpe, pero sólo funciona con numeros enteros positivos en base 10"   
#    elif decimal==0:
#        return "0"
#    elif decimal==1:
#        return "1"
#    else:
#       return f"{convertir_a_binario(decimal//2)}{decimal%2}"
    
#print(f"El número decimal 13 en binario es: {convertir_a_binario(13)}")
#print(f"El número decimal 0 en binario es: {convertir_a_binario(0)}")
#print(f"El número decimal 1 en binario es: {convertir_a_binario(1)}")
#print(f"El número decimal -13 en binario es: {convertir_a_binario(-13)}")

#print("\n¡Muchas gracias y hasta luego!\n")



# Ejercicio 5. 
#print("_"*40, "\n")
#print(f"Actividad 5\n")
#print("¡Hola!\n")

#import unicodedata

#def limpiar_texto(texto):
#    texto=texto.strip().lower()
#    texto="".join(texto.split()) 
#    texto=unicodedata.normalize("NFD",texto) 
#    texto="".join(letra for letra in texto if unicodedata.category(letra) != 'Mn') 
#    return texto

#def es_palindromo(palabra):
#    palabra_limpia=limpiar_texto(palabra)
#    longitud=len(palabra_limpia)
#    if longitud<=1: 
#        return True
#    if palabra_limpia[0]!=palabra_limpia[-1]:
#        return False
#    return es_palindromo(palabra_limpia[1:-1]) 

#print("¿Es Palíndromo?\n")
#print(f"1.-     : {es_palindromo("    ")}")
#print(f"2.- a: {es_palindromo("a")}")
#print(f"3.-    b    : {es_palindromo("   b    ")}")
#print(f"4.- Reconocer: {es_palindromo("Reconocer")}")
#print(f"5.-   AÉREOpuerto   : {es_palindromo("   AÉREOpuerto   ")}")
#print(f"6.-   AÉREA   : {es_palindromo("   AÉREA   ")}")
#print(f"7.- Ne    U q U é N: {es_palindromo(" Ne    U q U é N")}")
#print(f"8.- Anita lava la tina: {es_palindromo(" Anita lava la tina")}")
#print(f"9.- Yo HAGO y o g a HOY: {es_palindromo("Yo HAGO y o g a HOY")}")
#print(f"10.- Yo HAGO y o g a HOY a la tarde: {es_palindromo("Yo HAGO y o g a HOY a la tarde")}")

#print("\n¡Muchas gracias y hasta luego!\n")



# Ejercicio 6.
#print("_"*40, "\n")
#print(f"Actividad 6\n")
#print("¡Hola!\n")

#def suma_digitos(n):
#    if n<10:
#        return n
#    else:
#        return suma_digitos(n//10) + n%10

#print(f"1234 = 1 + 2 + 3 + 4 = {suma_digitos(1234)}")
#print(f"9 = {suma_digitos(9)}")
#print(f"305 = 3 + 0 + 5 = {suma_digitos(305)}")   

#print("\n¡Muchas gracias y hasta luego!\n")



# Ejercicio 7. 
#print("_"*40, "\n")
#print(f"Actividad 7\n")
#print("¡Hola!\n")

#def contar_bloques(n):
#    if n==0:
#        return 0
#    elif n<0:
#        return "Disculpe, hay un error, no puede haber una cantidad de bloques negativa"
#    else:
#        return n + contar_bloques(n-1)
        
#print("Ejemplos de contar bloques:\n")
#print(f"1. si hay 1 bloque: {contar_bloques(1)}") 
#print(f"2. si hay 4 bloques: 4 + 3 + 2 + 1 = {contar_bloques(4)}")
#print(f"3. si hay 7 bloques: 7 + 6 + 5 + 4 + 3 + 2 + 1 = {contar_bloques(7)}") 
#print(f"4. si hay 0 bloques: {contar_bloques(0)}")
#print(f"5. si hay -3 bloque: {contar_bloques(-3)}")

#print("\n¡Muchas gracias y hasta luego!\n")



# Ejercicio 8.
#print("_"*40, "\n")
#print(f"Actividad 8\n")
#print("¡Hola!\n")

#def contar_digito(numero, digito):
#    numero=abs(numero)
#    if digito<0 or digito>10:
#        return "Disculpe, hay un error: El dígito debe estar entre 0 y 9"
#    if numero<10:
#        return 1 if numero==digito else 0
#    else:
#        return (1 if numero%10==digito else 0) + contar_digito(numero//10, digito)

#print("Ejemplos de contar dígitos en un número:\n")
#print(f"1. En el número 12233421, el dígito 2 aparece: {contar_digito(12233421, 2)} veces") 
#print(f"2. En el número 5555, el dígito 5 aparece:  {contar_digito(5555, 5)} veces")
#print(f"2. En el número 123456, el dígito 7 aparece:  {contar_digito(123456, 7)} veces") 
#print(f"3. En el número 0, el dígito 0 aparece:  {contar_digito(0, 0)} veces")
#print(f"4. En el número -132334353, el dígito 3 aparece:  {contar_digito(-132334353, 3)} veces")
#print(f"3. En el número 12345, el dígito -3 aparece:  {contar_digito(12345, -3)} veces")
#print(f"3. En el número 12345, el dígito 12 aparece:  {contar_digito(12345, 12)} veces")

#print("\n¡Muchas gracias y hasta luego!\n")