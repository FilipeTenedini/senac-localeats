class ValorMinimoNaoAtingidoError(ValueError):
    def __init__(self, total: float, valor_minimo: float) -> None:
        self.total = total
        self.valor_minimo = valor_minimo
        super().__init__(
            f"Valor mínimo do pedido não atingido: "
            f"total R$ {total:.2f}, mínimo R$ {valor_minimo:.2f}"
        )


def calcular_total_itens(itens: list[dict]) -> float:
    return sum(item["preco"] for item in itens)


def calcular_total_pedido(itens: list[dict], valor_minimo: float) -> float:
    total = calcular_total_itens(itens)

    if total < valor_minimo:
        raise ValorMinimoNaoAtingidoError(total, valor_minimo)

    return total
