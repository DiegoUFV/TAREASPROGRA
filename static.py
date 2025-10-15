
class Utilidades:

    @staticmethod
    def es_primo(n: int) -> bool:
        # Devuelve True si n es primo
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n: int) -> int:
        # Calculamos el factorial de n (1*2*3*...*n)
        if n < 0:
            return None
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    @staticmethod
    def es_palindromo(cadena: str) -> bool:
        # Devuelve True cuando la palabra es palindromo
        
        cadena = cadena.lower().replace(" ", "")
        return cadena == cadena[::-1]

    @staticmethod
    def suma_digitos(n: int) -> int:
        # Suma los dígitos del número n
        return sum(int(d) for d in str(abs(n)))
# Ejemplos de uso
if __name__ == "__main__":
    print("¿13 es primo?", Utilidades.es_primo(13))
    print("Factorial de 4:", Utilidades.factorial(4))
    print("¿'Reconocer' es palíndromo?", Utilidades.es_palindromo("Reconocer"))
    print("Suma de los dígitos de 2468:", Utilidades.suma_digitos(2468))