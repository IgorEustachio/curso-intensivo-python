from classe_pesquisa_anonima import AnonymousSurvey
import pytest

@pytest.fixture
def pesquisa_idioma():
    #Uma pesquisa que estará disponível para todas as funções de teste
    question = "What language did you first learn to speak?"
    pesquisa_idioma = AnonymousSurvey(question)
    return pesquisa_idioma

def test_store_single_response(pesquisa_idioma):
    #testa se uma resposta individual esta devidamente armazenada
    pesquisa_idioma.store_response('English')
    assert 'English' in pesquisa_idioma.responses


def test_store_three_responses(pesquisa_idioma):
    #Testa se três respostas individuais estão devidamente armazenadas
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        pesquisa_idioma.store_response(response)

    for response in responses:
        assert response in pesquisa_idioma.responses

        