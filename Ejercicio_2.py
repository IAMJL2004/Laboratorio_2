#Desarrollar un programa que solicite tres números enteros desde teclado al usuario
print("************************************************")
print("             Dijite 3 numeros.")
print("************************************************")
print()

Num1 = int(input("Digita el primer numero: "))
print()
Num2 = int(input("Digita el segundo numero: "))
print()
Num3 = int(input("Digita el tercer numero: "))
print()

if Num1 > Num2 and Num2 > Num3:
    print("El numero ",Num1, " es el mas grande de los tres")
    print("El numero ",Num2, " es el mediano de los tres")
    print("El numero ",Num3, " es el mas pequeño de los tres")

elif Num1 > Num3 and Num3 > Num2: 
    print("El numero ",Num1, " es el mas grande de los tres")
    print("El numero ",Num3, " es el mediano de los tres")
    print("El numero ",Num2, " es el mas pequeño de los tres")

elif Num2 > Num1 and Num1 > Num3:
    print("El numero ",Num2, " es el mas grande de los tres")
    print("El numero ",Num1, " es el mediano de los tres")
    print("El numero ",Num3, " es el mas pequeño de los tres")

elif Num2 > Num3 and Num3 > Num1:
    print("El numero ",Num2, " es el mas grande de los tres")
    print("El numero ",Num3, " es el mediano de los tres")
    print("El numero ",Num1, " es el mas pequeño de los tres")

elif Num3 > Num1 and Num1 > Num2:
    print("El numero ",Num3, " es el mas grande de los tres")
    print("El numero ",Num1, " es el mediano de los tres")
    print("El numero ",Num2, " es el mas pequeño de los tres")

elif Num3 > Num2 and Num2 > Num1:
    print("El numero ",Num3, " es el mas grande de los tres")
    print("El numero ",Num2, " es el mediano de los tres")
    print("El numero ",Num1, " es el mas pequeño de los tres")

else:
    print("!!!ERROR!!!")

print("**fin del programa**")
