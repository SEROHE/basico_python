#Calculadora con 4 metodos y parametros con enteros
#Queremos usar type() para ver como Python decide los tipos en base a los valores de inicialización que le damos

class calculadora_enteros:
    n1 = int(input("Introduce tu primer número: "))
    n2 = int(input("Introduce tu segundo número: "))

    def sumar(n1,n2):
        print("RESULTADO: La suma de", n1, "+", n2, "es igual a", n1 + n2)
        print(type(n1,n2))
    def restar(n1,n2):
        print("RESULTADO: La resta de", n1, "-", n2, "es igual a", n1 - n2)

    def multiplicar(n1,n2):
        print("RESULTADO: La multiplicacion de", n1, "*", n2, "es igual a", n1 * n2)

    def division(n1,n2):
        print("RESULTADO: La division de", n1, "/", n2, "es igual a", n1 / n2)
    opcion=0
    while True:
        print("1) Sumar los dos números")
        print("2) Restar los dos números")
        print("3) Multiplicar los dos números")
        print("4) dividir los dos numeros")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            sumar(n1,n2)
        elif opcion == 2:
            restar(n1,n2)
        elif opcion == 3:
            multiplicar(n1,n2)
        elif opcion == 4:
            division(n1,n2)
        elif opcion == 5:
            break
