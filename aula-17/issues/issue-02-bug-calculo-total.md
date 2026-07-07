## Severidade

Alta

## Descrição do defeito

A função `calcular_total_itens` foi implementada incorretamente retornando `len(itens)` em vez de `sum(item["preco"] for item in itens)`, fazendo o total do pedido refletir a quantidade de itens e não o valor financeiro.

## Como reproduzir

1. Alterar `calcular_total_itens` para retornar `len(itens)`
2. Executar `pytest tests/test_pedido.py -v`
3. Observar falha em `test_deve_calcular_total_quando_valor_minimo_atingido`

## Comportamento esperado

Para itens de R$ 51,25 + R$ 17,49, o total deve ser R$ 68,74 — não `2`.

## Labels sugeridas

`bug`, `qualidade`
