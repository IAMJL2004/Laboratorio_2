print("*************")
print("Ejercicio 1")
print("*************")

print()

valor=int(input("Digita la cantidad de articulos a comprar -> "))

x=0
resultado=0

while x<valor:
    
    x+=1
    print()
    nombre=input(f"Digita el nombre del articulo {x} -> ")
    print()
    precio=float(input("Digita el precio del articulo $"))
    print()
    

    
    resultado=resultado+precio
    
print(f"El total a pagar es de ${resultado}")
print()
pago=float(input("Ingresa la cantidad de dinero con la vas a cancelar ->"))

if pago>resultado:
    
    total=pago-resultado
    
    print(f"Tu vuelo es de ${total}")
    print()
    print("Gracias por la compra, FELIZ DIA")
    
elif pago==resultado:
    
    print()
    print("Gracias por tu compra")
    
elif pago<resultado:
    
    print()
    print("Error, no puedes llevarte los articulos PAGO INSUFICIENTE")