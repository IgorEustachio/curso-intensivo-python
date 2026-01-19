from funcao_cidade_pais import cidadepais

def test_cidade_pais_populacao():
    cidadepaispopulacao = cidadepais('santiago', 'chile', '20 milhoes')
    assert cidadepaispopulacao == 'Santiago, Chile - população de 20 milhoes habitantes'

