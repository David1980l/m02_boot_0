def normal(i):
    return i

def cuadrado(x):
    return x * x

def sumaTodo(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    return resultado

print(sumaTodo(100, normal))
print(sumaTodo(3, cuadrado))