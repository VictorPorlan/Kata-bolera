from src.bolera import Bolera

def test_bolera():
    assert 60 == Bolera("12345123451234512345").recorrer_lista()
    assert 90 == Bolera("9-9-9-9-9-9-9-9-9-9-").recorrer_lista()
    assert 150 == Bolera('5/5/5/5/5/5/5/5/5/5/5').recorrer_lista()
    assert 149 == Bolera('8/549-XX5/53639/9/X').recorrer_lista()
    assert 111 == Bolera('9-9-9-9-9-9-9-9-9-XXX').recorrer_lista()
    assert 141 == Bolera('XXX9-9-9-9-9-9-9-').recorrer_lista()
    assert 175 == Bolera('X5/X5/XX5/--5/X5/').recorrer_lista()
    assert 120 == Bolera('XX9-9-9-9-9-9-9-9-').recorrer_lista()
