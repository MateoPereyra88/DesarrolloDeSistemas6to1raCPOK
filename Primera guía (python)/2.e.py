def main():
    cambio = int(input("ingrese el cambio: "))
    bCien = cambio//100
    cambio -= bCien*100
    bCincuenta = cambio//50
    cambio -= bCincuenta*50
    bDiez = cambio//10
    cambio -= bDiez*10
    bCinco = cambio//5
    cambio -= bCinco*5
    mUno = cambio
    
    print("para este cambio se necesitan: ")
    if bCien != 0:
        print(bCien, "billetes de cien")
    if bCincuenta != 0:
        print(bCincuenta, "billete de cincuenta")
        #solo puede haber 1 billete de 50 como mucho
    if bDiez != 0:
        print(bDiez, "billetes de diez")
    if bCinco != 0:
        print(bCinco, "billete de cinco")
        #pasa lo mismo que con el de cincuenta
    if mUno != 0:
        print(mUno, "monedas de uno")
main()