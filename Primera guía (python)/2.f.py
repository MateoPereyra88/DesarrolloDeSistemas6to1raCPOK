def main():
    valorProducto = float(input("Ingrese el valor del producto: "))
    variacion = cuotas = 0
    
    print("Planes disponibles: ")
    print("1.Totalmente contado con descuento del 15%.")
    print("2.Mitad contado y 2 cuotas iguales del resto. El precio incremento 18%.")
    print("3.La tercera parte contado y cuatro cuotas iguales. El precio incremento 25%.")
    print("4.Totalmente financiado a 6 cuotas iguales. incremento del precio en 30%.")
    
    plan = int(input("Ingrese el número de plan que desea: "))
    
    if(plan == 1):
        variacion = -15/100
        cuotas = 1
    elif(plan == 2):
        variacion = 18/100
        cuotas = 2
    elif(plan == 3):
        variacion = 25/100
        cuotas = 4
    elif(plan == 4):
        variacion = 30/100
        cuotas = 6
    else:
        print("No contamos con ese número de plan")
    
    if cuotas > 0:
        valorTotal = valorProducto + valorProducto * variacion
        valorCouta = valorTotal / cuotas
        
        print("Valor de producto: $", valorProducto)
        if cuotas > 1:
            print(cuotas, "cuotas de: $", valorCouta)
        print("Valor total de pago: $",valorTotal)
    
    
main()