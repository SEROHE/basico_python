#str (string) en Python es inmutable ¿cómo puedo comprobar esto en un pequeño programa?

class StringInmutable:

    n='serafin'
    print(n[0])
    print(len(n), id(n))
    n2=n+' rojas'
    print(len(n2),n2)
    print(id(n2))
