
class Estudiante:
    num_estudiante=0

    def __init__(self,nombre,edad,nota):
        self.nombre=nombre
        self.edad=edad
        self.nota=nota


    def estudiar(self,cuanto):
        print(self.nombre,)

estud1 = Estudiante("jose",20,4)
estud2 = Estudiante("pepe",25,8)

lista_estudiantes=[estud1,estud2]

for x in lista_estudiantes:
     print(x.nombre, x.edad, x.nota)
