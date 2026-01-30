from funcao_para_teste import get_formatted_name
from funcao_cidade_pais import cidadepais

def test_first_last_name():
    # testando Janis Joplin
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
# Nomes como 'Wolfgang Amadeus Mozart' funcionam?
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'