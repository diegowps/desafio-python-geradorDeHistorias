"""
test_gerador_historia.py
------------------------
Testes automáticos para o Gerador de Histórias.
Utiliza a biblioteca padrão unittest.
"""
import unittest
from gerador_historia import gerar_historia, TEMAS

class TestGeradorHistoria(unittest.TestCase):
    def test_historia_fantasia(self):
        historia = gerar_historia('fantasia')
        self.assertIsInstance(historia, str)
        self.assertIn('Era uma vez', historia)
    def test_historia_ficcao(self):
        historia = gerar_historia('ficcao')
        self.assertIsInstance(historia, str)
        self.assertIn('Era uma vez', historia)
    def test_historia_misterio(self):
        historia = gerar_historia('misterio')
        self.assertIsInstance(historia, str)
        self.assertIn('Era uma vez', historia)
    def test_tema_invalido(self):
        with self.assertRaises(ValueError):
            gerar_historia('terror')

if __name__ == "__main__":
    unittest.main()
