from app.funcao import funcao_ola

def test_funcao_ola_retorna_ola():
    saida = funcao_ola()
    gabarito = "Olá pessoas!"
    assert saida == gabarito