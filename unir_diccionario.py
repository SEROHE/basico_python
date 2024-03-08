#Crear dos diccionarios y unirlos
class UnirDicionarios:

    def __init__(self):
        self.d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
        self.d2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    def unir_diccionarios(self):
        dunido = self.d1.copy()  # Copia d1 para no modificar el original
        dunido.update(self.d2)   # Actualiza dunido con los elementos de d2

        x = 0
        for key, value in dunido.items():
            print(x, "{0}={1}".format(key, value))
            x += 1

# Crear una instancia de la clase y llamar al método unir_diccionarios
unir = UnirDicionarios()
unir.unir_diccionarios()