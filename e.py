
def factorial(n):
    if n <= 0:
        return 1
    factorial = 1
    while n > 0:
        factorial = factorial * n
        n -= 1
    return factorial



print("--------------- Vamos a calcular el numero e ------------")

print("Introduce el limite para el calculo de e: ")

limite = int(input())

n = 0
e = 0
while n < limite:
	e += 1/factorial(n) # se llama a la función factorial creada por ti
	n = n + 1



print("e = ", e)

 
 
 
 
