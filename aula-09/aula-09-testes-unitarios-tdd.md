# Aula 9 – Testes Unitários e TDD

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrante: Filipe Tenedini Domingos

---

## 📁 Estrutura do Projeto

```
senac-localeats/
├── src/
│   ├── __init__.py
│   └── pedido.py
├── tests/
│   └── test_pedido.py
├── requirements.txt
└── aula-09-testes-unitarios-tdd.md
```

---

## 🔹 1. Funcionalidade escolhida

### 🍔 Cálculo do total do pedido com valor mínimo

**Arquivo da implementação:** `src/pedido.py`  
**Arquivo de testes:** `tests/test_pedido.py`

#### O que faz

Soma os valores dos itens do pedido e verifica se o total atinge o valor mínimo exigido pelo restaurante antes de permitir a finalização.

#### Problema que resolve

Evita pedidos inválidos que não atendem às regras comerciais do restaurante. No LocalEats, durante os testes manuais da Aula 6 (CT-09), foi possível finalizar pedidos com um único item (ex.: Prato Especial 0 — R$ 87,12), mas não havia validação explícita de valor mínimo — uma regra de negócio crítica que deveria existir no backend.

#### Importância

É regra central do fluxo de compra. Sem ela, o restaurante pode receber pedidos abaixo do ticket mínimo, gerando prejuízo operacional (custo de entrega/preparo maior que a receita).

#### Regras de negócio

| Regra | Descrição |
|---|---|
| Total | Soma dos preços de todos os itens do pedido |
| Valor mínimo | Se `total < valor_minimo` → erro |
| Pedido válido | Se `total >= valor_minimo` → retorna o total |

#### Implementação final

```python
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
```

---

## 🔹 2. Testes Unitários

Foram implementados **3 testes**, cobrindo 2 cenários de sucesso (happy path) e 1 cenário de erro.

---

### Teste 1 – Total acima do valor mínimo (happy path)

**Nome descritivo:** Deve calcular corretamente o total do pedido quando valor mínimo é atingido

**Cenário testado:** Valida se a função retorna o total quando a soma dos itens é maior que o valor mínimo exigido.

**Dados de entrada:**
- `itens = [{"nome": "Prato Especial 1", "preco": 51.25}, {"nome": "Prato Especial 2", "preco": 17.49}]`
- `valor_minimo = 30`

**Resultado esperado:** Retornar `68.74`. Não deve gerar erro.

```python
def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [
        {"nome": "Prato Especial 1", "preco": 51.25},
        {"nome": "Prato Especial 2", "preco": 17.49},
    ]
    valor_minimo = 30

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == pytest.approx(68.74)
```

---

### Teste 2 – Total exatamente no valor mínimo (happy path / borda)

**Nome descritivo:** Deve aceitar pedido quando total é exatamente igual ao valor mínimo

**Cenário testado:** Valida o limite inferior permitido — total igual ao mínimo deve ser aceito.

**Dados de entrada:**
- `itens = [{"nome": "Prato Especial 2", "preco": 30}]`
- `valor_minimo = 30`

**Resultado esperado:** Retornar `30`. Não deve gerar erro.

```python
def test_deve_aceitar_pedido_quando_total_e_exatamente_o_valor_minimo():
    itens = [{"nome": "Prato Especial 2", "preco": 30}]
    valor_minimo = 30

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 30
```

---

### Teste 3 – Total abaixo do valor mínimo (erro)

**Nome descritivo:** Deve rejeitar pedido abaixo do valor mínimo

**Cenário testado:** Valida que pedidos inválidos geram erro antes de serem finalizados.

**Dados de entrada:**
- `itens = [{"nome": "Prato Especial 2", "preco": 17.49}]`
- `valor_minimo = 30`

**Resultado esperado:** Lançar `ValorMinimoNaoAtingidoError` com mensagem descritiva.

```python
def test_deve_lancar_erro_quando_total_fica_abaixo_do_valor_minimo():
    itens = [{"nome": "Prato Especial 2", "preco": 17.49}]
    valor_minimo = 30

    with pytest.raises(ValorMinimoNaoAtingidoError, match="Valor mínimo do pedido não atingido"):
        calcular_total_pedido(itens, valor_minimo)
```

---

## 🔹 3. Aplicação do TDD

O ciclo TDD completo foi aplicado na funcionalidade **validação de valor mínimo do pedido**, usando o Teste 3 como guia.

### 🔴 Red — Escrever o teste antes da implementação

Primeiro, escrevi o teste que espera um erro quando o total fica abaixo do mínimo:

```python
def test_deve_lancar_erro_quando_total_fica_abaixo_do_valor_minimo():
    itens = [{"nome": "Prato Especial 2", "preco": 17.49}]
    valor_minimo = 30

    with pytest.raises(ValueError, match="Valor mínimo do pedido não atingido"):
        calcular_total_pedido(itens, valor_minimo)
```

**Resultado:** o teste falhou com `ImportError` / `ModuleNotFoundError`, pois a função `calcular_total_pedido` ainda não existia.

---

### 🟢 Green — Implementação mínima

Implementei apenas o necessário para o teste passar:

```python
def calcular_total_pedido(itens, valor_minimo):
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total
```

**Resultado:** o teste de erro passou. Em seguida, escrevi os testes de sucesso (Testes 1 e 2) e confirmei que também passaram com essa implementação mínima.

---

### 🔵 Refactor — Melhorar mantendo os testes passando

Com todos os testes verdes, refatorei o código:

1. **Extraí `calcular_total_itens`** — separa o cálculo da soma da validação de regra de negócio (Single Responsibility).
2. **Criei `ValorMinimoNaoAtingidoError`** — exceção específica em vez de `ValueError` genérico, permitindo tratamento diferenciado no fluxo de pedidos.
3. **Mensagem de erro enriquecida** — inclui total calculado e valor mínimo exigido, facilitando debug e feedback ao usuário.
4. **Type hints** — `list[dict]` e `float` documentam o contrato da função.

```python
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
```

**Resultado:** os 3 testes continuaram passando após a refatoração.

---

## 🔹 4. Refatoração

| Melhoria | Antes | Depois | Justificativa |
|---|---|---|---|
| Separação de responsabilidades | Soma e validação na mesma função | `calcular_total_itens` + `calcular_total_pedido` | Facilita testar e reutilizar o cálculo em outros contextos (ex.: exibir subtotal no carrinho) |
| Exceção específica | `ValueError` genérico | `ValorMinimoNaoAtingidoError` | Permite ao front-end exibir mensagem amigável sem tratar todos os `ValueError` da aplicação |
| Mensagem de erro | Texto fixo | Inclui total e mínimo formatados | Ajuda o usuário a saber quanto falta para atingir o mínimo |
| Tipagem | Sem type hints | `list[dict]`, `float` | Documenta o contrato e previne erros em tempo de desenvolvimento |

---

## 🔹 5. Execução dos Testes

**Comando executado:**

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest tests/ -v
```

**Resultado:**

| Métrica | Valor |
|---|---|
| Total de testes | 3 |
| Passaram | 3 |
| Falharam | 0 |

**Evidência (log de execução):**

```
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-9.1.1, pluggy-1.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/filipe/Área de Trabalho/senac-localeats
collecting ... collected 3 items

tests/test_pedido.py::test_deve_calcular_total_quando_valor_minimo_atingido PASSED [ 33%]
tests/test_pedido.py::test_deve_aceitar_pedido_quando_total_e_exatamente_o_valor_minimo PASSED [ 66%]
tests/test_pedido.py::test_deve_lancar_erro_quando_total_fica_abaixo_do_valor_minimo PASSED [100%]

============================== 3 passed in 0.01s ===============================
```

---

## 🔹 6. Reflexão no contexto do LocalEats

### Foi difícil escrever testes antes do código?

Sim, inicialmente. A tendência natural é implementar a função e só depois pensar nos cenários. Porém, ao escrever o teste de erro primeiro, fui obrigado a definir claramente o comportamento esperado (qual exceção, qual mensagem) antes de escrever qualquer linha de lógica. Isso exige mudança de mentalidade, mas se torna mais natural após o primeiro ciclo Red → Green → Refactor.

### O TDD ajudou no desenvolvimento?

Sim. O TDD evitou implementar lógica desnecessária — a versão mínima (Green) tinha apenas 6 linhas. A refatoração veio depois, com segurança, porque os testes garantiam que o comportamento não quebrava. No contexto do LocalEats, onde a Aula 6 identificou problemas no fluxo de pedidos (CT-09), ter testes unitários nessa regra de negócio evitaria regressões ao corrigir bugs do histórico de pedidos.

### Os testes aumentaram a confiança no código?

Sim. Saber que existem 3 cenários automatizados (2 sucessos + 1 erro) permite alterar a implementação — como extrair funções ou mudar a exceção — sem medo de quebrar silenciosamente. A pergunta "se eu mudar esse código amanhã, meus testes vão garantir que nada quebre?" passa a ter resposta concreta: sim, em 0,01 segundos.

### O que melhorariam?

- Cobrir mais cenários de borda: lista de itens vazia, preço negativo, valor mínimo zero.
- Integrar os testes ao pipeline de CI/CD, conforme sugerido na Aula 3 (prática DevOps).
- Adicionar testes para as outras regras sugeridas (desconto, taxa de entrega) conforme outros integrantes do grupo.

### Como isso ajuda no projeto do grupo?

O LocalEats já apresenta falhas em produção (busca textual, histórico de pedidos com IDs internos — Aula 6). Testes unitários nas regras de negócio do backend criam uma base sólida antes de integrar com o front-end e a API. Especialmente para o fluxo de finalização de pedidos — classificado como **alta prioridade** na Aula 4 —, validar cálculos e regras com testes automatizados reduz o risco de cobranças incorretas e pedidos inválidos chegando aos restaurantes parceiros.
