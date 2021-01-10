from src.bolera import Bolera

def test_basico_bolera():
    assert 60 == Bolera("12345123451234512345").recorrer_lista()