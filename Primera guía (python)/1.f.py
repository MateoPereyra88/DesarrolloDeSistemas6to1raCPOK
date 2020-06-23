def main():
    a = float(input("Ingrese un valor: "))
    b = float(input ("Ingrese otro valor: "))
    print("({0} + {1})".format(a, b))
    print("{0}^2 + 2*{0}*{1} + {1}^2".format(a, b))
    print("{0} + {1} + {2}".format(a*a, 2*a*b, b*b))
    print(a*a + 2*a*b + b*b)
main()