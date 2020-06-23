import math
def main():
    cat1 = float(input("ingrese el primer cateto (cm): "))
    cat2 = float(input("ingrese el segundo cateto (cm): "))
    hipotenusa = math.sqrt(pow(cat1, 2) + pow(cat2, 2))
    print("la hipotenusa mide ", hipotenusa, "cm")
main()