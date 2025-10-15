

# Clase base para todas las operaciones

class Operacion:
    def calcular(self, a, b):
        pass  # Se define en las clases hijas
###############################################

class Sumar(Operacion):
    def calcular(self, a, b):
        return a + b

class Restar(Operacion):
    def calcular(self, a, b):
        return a - b

class Multi(Operacion):
    def calcular(self, a, b):
        return a * b

class Div(Operacion):
    def calcular(self, a, b):
        if b == 0:
            return "Error: división por cero"
        return a / b

# Nueva operación añadida sin modificar las anteriores
class Potencia(Operacion):
    def calcular(self, a, b):
        return a ** b
    
class Calculadora:
    def __init__(self):
        # Creamos un diccionario con las operaciones disponibles
        self.operaciones = {
            "Sumar": Sumar(),
            "Restar": Restar(),
            "Multi": Multi(),
            "Div": Div(),
            "Potencia": Potencia()  
        }

    def operar(self, tipo, a, b):
        if tipo in self.operaciones:
            return self.operaciones[tipo].calcular(a, b)
        else:
            return "Operación no válida"


if __name__ == "__main__":
    calc = Calculadora()

    print("Sumar:", calc.operar("Sumar", 7, 3))
    print("Restar:", calc.operar("Restar", 4, 1))
    print("Multiplicación:", calc.operar("Multi", 10, 100))
    print("División:", calc.operar("Div", 5, 1))
    print("Potencia:", calc.operar("Potencia", 2, 4))