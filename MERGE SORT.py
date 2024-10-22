# MERGE SORT
N = int(input("Ingrese la cantidad de elementos del Array: "))
Array = []

for i in range(N):
    n = int(input(f"Ingrese el valor {i+1}: "))
    Array.append(n)

print("El Array original es: ")
for i in range(N):
    print(Array[i], end=" ")
print()

m = 1
while m < N:
    for Iizq in range(0, N, 2 * m):
        medio = min(Iizq + m, N)
        Fder = min(Iizq + 2 * m, N)

        tam_izq = medio - Iizq
        tam_der = Fder - medio

        # Creamos sub listas temporales
        IZQ = Array[Iizq:medio]
        DER = Array[medio:Fder]

        i = j = 0
        k = Iizq

        # Combinamos las sub listas
        while i < tam_izq and j < tam_der:
            if IZQ[i] <= DER[j]:
                Array[k] = IZQ[i]
                i += 1
            else:
                Array[k] = DER[j]
                j += 1
            k += 1

        # Terminamos de copiar los datos que faltan
        while i < tam_izq:
            Array[k] = IZQ[i]
            i += 1
            k += 1

        while j < tam_der:
            Array[k] = DER[j]
            j += 1
            k += 1

    m *= 2

print("\nEl Array ordenado es: ")
for i in range(N):
    print(Array[i], end=" ")
