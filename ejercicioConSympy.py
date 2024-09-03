import math
#Programa para Ln(2+x)
#Valor inicial
a = 0
#Valor a aproximar
x = 0.2
#Diferencia entre x-a de la serie
h = x-a
res = [0]*6
#Funcion inicial: f(x) = ln(2+x)
#Cada funcion evaluada, es añadida al vector de resultados
res[0] = math.log(2+a)
s = res[0]
#Primera derivada: f(x) = 1/2+x
res[1] = 1/2+a
#Segunda derivada: f(x) = -1/(2+x)^2
res[2] = -1/(2+a)**2
#Tercera derivada: f(x) = 2/(2+x)^3
res[3] = 2/(2+a)**3
#Cuarta derivada: f(x) = -6/(2+x)^4
res[4] = -6/(2+a)**4
#Quinta derivada: f(x) = 24/(2+x)^5
res[5] = 24/(2+a)**5

print("Valores generados:\n")
for i in range(1, 6):
    #Se calculan los distintos factores aplicando la serie de Taylor
    r = (res[i]/math.factorial(i))*h**i
    print(f'vt{i} = {r}')
    s+=r

#Resultados
print(f'\nValor aproximado por Taylor: {s}')
print(f'Valor real: {math.log(2.2)}')
