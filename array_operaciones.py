class ArrayOperaciones:

    def sumar(x,y):
        return x+y
    def restar(x,y):
        return x-y
    def multiplicar(x,y):
        return x*y
    def dividir(x,y):
        return x/y

    array=[sumar,restar,multiplicar,dividir]
    nuevaop=array[3]
    print(nuevaop(4,2))
