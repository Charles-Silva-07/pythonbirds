from unittest import TestCase

from oo.carro import Motor


class Teste_Carro(TestCase):

    def teste_velocidade(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

