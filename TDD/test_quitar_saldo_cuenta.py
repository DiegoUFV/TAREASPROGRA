
import unittest
from src.cuenta import Cuenta

class TestQuitarSaldo(unittest.TestCase):

    def test_retirar_dinero_menor_al_saldo(self):
        cuenta = Cuenta()
        cuenta.retirar(500)
        self.assertEqual(cuenta.saldo, 1500)

    def test_retirar_dinero_mayor_al_saldo(self):
        cuenta = Cuenta()
        cuenta.ingresar(1500)
        with self.assertRaises(Exception):
            cuenta.retirar(3000)

if __name__ == '__main__':

    unittest.main()
