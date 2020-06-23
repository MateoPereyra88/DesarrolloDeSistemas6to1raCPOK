import math
def main():
    num = float(input("ingrese un numero real: "))
    p_Entera = int(num)
    p_Decimal = num - p_Entera
    print("la parte entera es ", p_Entera)
    if p_Decimal != 0:
        print("y la parte decimal es ", p_Decimal)
main()