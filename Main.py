import random

letters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
L = int(input("Que longitud quieres que tenga tu contraseña: "))
Final_password = ""

for i in range(L):
    Final_password += random.choice(letters)
print("Tu contraseña es: ",Final_password)








for i in range(1,6):
    print("*" * i)


nombre = input("Ingresa un nombre: ")

print("*" * (len(nombre) + 2))
print("*" + nombre + "*")
print("*" * (len(nombre) + 2))

n = int(input("Ingresa un número: "))

suma = 0
for i in range(1, n + 1):
    suma += i

print("La suma es:", suma)




import random

numero_random = random.randint(1, 20)

for i in range(5):
    numero = int(input(f"Intento {i + 1}: Adivina el número del 1 al 20: "))

    if numero == numero_random:
        print("¡Felicidades! Adivinaste el número.")
        break
    elif numero < numero_random:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
else:
    print("No quedan más intentos. El número secreto era", numero_random)   
