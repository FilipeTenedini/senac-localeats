import pytest

from src.pedido import ValorMinimoNaoAtingidoError, calcular_total_pedido


def test_deve_calcular_total_quando_valor_minimo_atingido():
    # Nome descritivo:
    # Deve calcular corretamente o total do pedido quando valor mínimo é atingido
    #
    # Cenário testado:
    # Valida se a função retorna o total quando a soma dos itens
    # é maior que o valor mínimo exigido pelo restaurante.
    #
    # Dados de entrada:
    # itens = [{"nome": "Prato Especial 1", "preco": 51.25}, {"nome": "Prato Especial 2", "preco": 17.49}]
    # valor_minimo = 30
    #
    # Resultado esperado:
    # Retornar 68.74
    # Não deve gerar erro

    itens = [
        {"nome": "Prato Especial 1", "preco": 51.25},
        {"nome": "Prato Especial 2", "preco": 17.49},
    ]
    valor_minimo = 30

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == pytest.approx(68.74)


def test_deve_aceitar_pedido_quando_total_e_exatamente_o_valor_minimo():
    # Nome descritivo:
    # Deve aceitar pedido quando total é exatamente igual ao valor mínimo
    #
    # Cenário testado:
    # Valida o limite inferior permitido — total igual ao mínimo.
    #
    # Dados de entrada:
    # itens = [{"nome": "Prato Especial 2", "preco": 30}]
    # valor_minimo = 30
    #
    # Resultado esperado:
    # Retornar 30
    # Não deve gerar erro

    itens = [{"nome": "Prato Especial 2", "preco": 30}]
    valor_minimo = 30

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 30


def test_deve_lancar_erro_quando_total_fica_abaixo_do_valor_minimo():
    # Nome descritivo:
    # Deve rejeitar pedido abaixo do valor mínimo
    #
    # Cenário testado:
    # Valida que pedidos inválidos geram erro antes de serem finalizados.
    #
    # Dados de entrada:
    # itens = [{"nome": "Prato Especial 2", "preco": 17.49}]
    # valor_minimo = 30
    #
    # Resultado esperado:
    # Lançar ValorMinimoNaoAtingidoError com mensagem descritiva

    itens = [{"nome": "Prato Especial 2", "preco": 17.49}]
    valor_minimo = 30

    with pytest.raises(ValorMinimoNaoAtingidoError, match="Valor mínimo do pedido não atingido"):
        calcular_total_pedido(itens, valor_minimo)
