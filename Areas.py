
def area_cuadrado(a:int)->int:
    print("El area del cuadrado es:" , a * a);

def area_triangulo(b:int,a:int)->float:
    print("El area del triangulo es: " , (b*a)/2);

def area_circulo(r:float)->float:
    print("El area del circulo es: ", 3.1416 * (r*r));

print("Dame la medida del lado del cuadrado para calcular su area: ")
cuadrado = int(input())

area_cuadrado(cuadrado)

print("Dame la base del triangulo para calcular su area:  ")
base = int(input())

print("Dame la altura del triangulo para calcular su area: ")
altura = int(input())

area_triangulo(base,altura)

print("Dame el radio del circulo para calcular su area: ")
radio = int(input())

area_circulo(radio)

