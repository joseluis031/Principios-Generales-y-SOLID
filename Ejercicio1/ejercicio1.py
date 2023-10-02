#ejercicio que fui haciendo a la vez que Germi

#clase matriz
class Matriz():
    def __init__(self, elementos: list):
        self.elementos = elementos
       

             
class Traspuesta(Matriz):
    def __init__(self, elementos: list): #no hace falta list
        super().__init__(elementos)
        self.elementos = elementos
    def traspuesta(self):
        return [[self.elementos[j][i] for j in range(len(self.elementos))] for i in range(len(self.elementos[0]))]
    
class Imprimir(Matriz):
    def __init__(self, elementos: list):
        super().__init__(elementos)
        self.elementos = elementos
    def imprimir(self):
        for i in self.elementos:
            print(i)
  #habria que hacer otra clase pa meter esto en una funcion y que no se vea feo
  
class Lanzador():
    def __init__(self, elementos: list):
        self.elementos = elementos
    def lanzar(self):
        mat = Imprimir(self.elementos)
        mat.imprimir()
        mat2 = Traspuesta(self.elementos)
        print(mat2.traspuesta())
        

def main():
    mat = Imprimir([[1,2,3],[4,5,6],[7,8,9]])
    mat.imprimir()
    mat2 = Traspuesta(mat.elementos)
    print(mat2.traspuesta())
    
    

    
    
class Otrolanzador(Imprimir, Traspuesta):
    #creame un metodo que me llame a la funcion imprimir y a la funcion traspuesta y que me lo recoja con
    #un input o output de los elemntos de la matriz
    
    def __init__(self):
        self.elementos = []
        self.filas = int(input("Introduce el numero de filas: "))
        self.columnas = int(input("Introduce el numero de columnas: "))
        self.createMatriz()
        super().__init__(self.elementos)
        
    def createMatriz(self):
        for i in range(self.filas):
            self.elementos.append([])
            for j in range(self.columnas):
                self.elementos[i].append(int(input("Introduce el elemento: ")))
                
    def lanzar(self):
        mat = Imprimir(self.elementos)
        mat.imprimir()
        print("La traspuesta es:")
        mat2 = Traspuesta(self.elementos)
        print(mat2.traspuesta())
        
class Main2():
    def __init__(self):
        self.Lanzador = Otrolanzador()
        self.Lanzador.lanzar()

if __name__ == "__main__":
    Main2()