import unittest
from hypothesis import given, example, settings, strategies as st
from cpf import CPF, gera_cpf


VALIDO = "113.451.253-80"
INVALIDO = "31354110274"


class CPFTest(unittest.TestCase):

    def test_cpf_valid(self):
        self.assertTrue(CPF(VALIDO).isValid())

    def test_cpf_invalid(self):
        self.assertFalse(CPF(INVALIDO).isValid())

    @given(st.builds(gera_cpf))
    def test_valid_cases(self, cpf):
        self.assertTrue(CPF(cpf).isValid())

    @given(st.lists(st.integers(min_value=0, max_value=9), max_size=10))
    def test_normalize_equally(self, cpf):
        self.assertEqual(CPF(cpf), CPF(str(cpf)))

    @given(st.just(VALIDO))
    @example(VALIDO.replace('.', ''))
    @example([int(x) for x in VALIDO if x not in '.-'])
    def test_manual_values(self, cpf):
        self.assertTrue(CPF(cpf).isValid())
