from src.bolera import Bolera

def test_basico_bolera():
    assert 60 == Bolera("12345123451234512345").recorrer_lista()
def test_creador_turnos():
    assert [['1','2'],['3','4'],['5','1'],['2','3'],['4','5'],['1','2'],['3','4'],['5','1'],['2','3'],['4','5']] == Bolera("12345123451234512345").divisor_turnos()
    assert [['X'],['3','/'],['5','-'],['X'],['4','5'],['1','2'],['3','4'],['5','1'],['2','3'],['4','5']] == Bolera("X3/5-X451234512345").divisor_turnos()
    assert [['X'],['3','/'],['5','-'],['X'],['4','5'],['1','2'],['3','4'],['5','1'],['2','3'],['4','5']] == Bolera("X3/5-X451234512345").divisor_turnos()
    assert [['X'],['X'],['X'],['X'],['X'],['X'],['X'],['X'],['X'],['X','X','X']] == Bolera("XXXXXXXXXXXX").divisor_turnos()
    assert [['X'],['X'],['X'],['X'],['X'],['X'],['X'],['X'],['X'],['4','/','X']] == Bolera("XXXXXXXXX4/X").divisor_turnos()
