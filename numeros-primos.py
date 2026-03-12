# numeros-primos.py

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []

for numero in range(1, 251):
    if es_primo(numero):
        primos.append(numero)

with open("results.txt", "w") as archivo:
    for primo in primos:
        archivo.write(str(primo) + "\n")

print("Números primos entre 1 y 250:")
for primo in primos:
    print(primo)

print("\nResultados guardados en results.txt")
