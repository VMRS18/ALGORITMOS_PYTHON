# COUNTING SORT
N = int(input("Ingrese la cantidad de elementos del Array: "))
Array = []

for i in range(N):
    n = int(input(f"Ingrese el valor {i+1}: "))
    Array.append(n)

print("El Array original es: ")
for i in range(N):
    print(Array[i], end=" ")
print()

# Buscar el valor mayor del array original
MAX = Array[0]
for i in range(N):
    if Array[i] > MAX:
        MAX = Array[i]

ArrNuevo = [0] * N
cont = [0] * (MAX + 1)

# Contar numero de repeticiones en el Array
for i in range(N):
    num = Array[i]
    cont[num] += 1

# Hacemos la suma acumulativa
for i in range(1, MAX + 1):
    cont[i] += cont[i - 1]

# Ordenamos
for i in range(N):
    num = Array[i]
    indice = cont[num]
    ArrNuevo[indice - 1] = num
    cont[num] -= 1

# Copiamos el array ordenado de regreso al array original
for i in range(N):
    Array[i] = ArrNuevo[i]

print("\nEl Array ordenado es: ")
for i in range(N):
    print(Array[i], end=" ")
