#if
numero1 = 10
numero2 = 15
if numero1 > numero2:
    print("El número " + str(numero1) + " es mayor que " + str(numero2))
elif numero2 > numero1:
    print("El número " + str(numero2) + " es mayor que " + str(numero1))
else:
    print("Los dos números son iguales")

#switch
mes = "Enero"
match mes:
    case "Enero":
        print("Enero es el primer mes del año")
    case "Febrero":
        print("Febrero es el segundo mes del año")

#bucle for
numeros = [4, 78, 9, 84]
for n in numeros:
    print(n)

#bucle while
i = 1
while i < 5:
    print(i)
    i+=1
