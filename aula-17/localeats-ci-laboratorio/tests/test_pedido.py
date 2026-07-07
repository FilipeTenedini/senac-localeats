import pytest

from src.pedido import ValorMinimoNaoAtingidoError, calcular_total_pedido


def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [
        {"nome": "Prato Especial 1", "preco": 51.25},
        {"nome": "Prato Especial 2", "preco": 17.49},
    ]

    resultado = calcular_total_pedido(itens, valor_minimo=30)

    assert resultado == pytest.approx(68.74)


def test_deve_aceitar_pedido_quando_total_e_exatamente_o_valor_minimo():
    itens = [{"nome": "Prato Especial 2", "preco": 30}]

    resultado = calcular_total_pedido(itens, valor_minimo=30)

    assert resultado == 30


def test_deve_lancar_erro_quando_total_fica_abaixo_do_valor_minimo():
    itens = [{"nome": "Prato Especial 2", "preco": 17.49}]

    with pytest.raises(ValorMinimoNaoAtingidoError, match="Valor mínimo do pedido não atingido"):
        calcular_total_pedido(itens, valor_minimo=30)
