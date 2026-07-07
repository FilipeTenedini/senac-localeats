# 🧩 Atividade PBL – Aula 12
## BDD e Automação Orientada a Comportamento – LocalEats

> Disciplina: Qualidade de Software  
> Prof.: Luciano Zanuz  
> Integrante: Filipe Tenedini Domingos

---

## 📁 Estrutura do Projeto

```
aula-12/
├── features/
│   └── filtro_categoria.feature      # Cenários Gherkin
├── pages/
│   ├── login_page.py                 # Page Object – autenticação
│   └── explorar_page.py              # Page Object – página Explorar
├── tests/
│   ├── conftest.py                   # Fixtures Pytest + credenciais
│   └── test_filtro_categoria.py      # Step definitions (Given/When/Then)
├── evidencias/
│   └── execucao-testes.log           # Log da execução
├── pytest.ini
├── requirements.txt
└── aula-12-bdd-automacao-comportamento.md
```

---

## 🔹 1. Fluxo escolhido

### 🍜 Filtro por categoria de restaurantes

**O que faz:** Permite filtrar a listagem de restaurantes por tipo de culinária (Italiana, Japonesa, Brasileira, Mexicana ou Todos).

**Problema que resolve:** Melhora a usabilidade e a descoberta de restaurantes, permitindo que o usuário encontre opções alinhadas à sua preferência gastronômica.

**Importância:** Fluxo central da experiência de exploração. Na Aula 6 (CT-04), o filtro por categoria **passou** nos testes manuais, enquanto a busca textual falhou — tornando este fluxo ideal para BDD como documentação viva de comportamento validado.

**Cenários esperados:**

| Cenário | Tipo | Comportamento |
|---|---|---|
| Filtro Japonesa | Sucesso | Lista exibe apenas restaurantes japoneses |
| Filtro Todos | Sucesso | Lista restaurada com culinárias diversas |
| Filtro destacado | Validação visual | Botão da categoria ativa recebe classe `active` |

---

## 🔹 2. Escrita dos cenários BDD

Arquivo: `features/filtro_categoria.feature`

```gherkin
# language: pt
Funcionalidade: Filtro por categoria de restaurantes
  Como usuário autenticado do LocalEats
  Quero filtrar restaurantes por tipo de culinária
  Para encontrar opções gastronômicas de acordo com minha preferência

  Contexto:
    Dado que o usuário está autenticado no sistema
    E que o usuário está na página Explorar

  Cenário: Filtrar restaurantes por culinária japonesa
    Quando selecionar o filtro "Japonesa"
    Então a listagem deve exibir apenas restaurantes japoneses
    E o filtro "Japonesa" deve estar destacado

  Cenário: Restaurar listagem completa com filtro Todos
    Dado que o filtro "Japonesa" está selecionado
    Quando selecionar o filtro "Todos"
    Então a listagem deve exibir restaurantes de diferentes culinárias
    E o filtro "Todos" deve estar destacado
```

**Por que estes cenários?**

- **Cenário 1** valida a regra de negócio principal: ao filtrar, apenas restaurantes da culinária selecionada devem aparecer.
- **Cenário 2** valida o comportamento de reset: o usuário consegue voltar à listagem completa após aplicar um filtro — comportamento essencial para usabilidade.

---

## 🔹 3. Implementação da automação com pytest-bdd

Arquivo: `tests/test_filtro_categoria.py`

```python
from pathlib import Path

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from pages.explorar_page import ExplorarPage
from pages.login_page import LoginPage

FEATURES_DIR = Path(__file__).parent.parent / "features"
scenarios(FEATURES_DIR / "filtro_categoria.feature")


@pytest.fixture
def explorar(page):
    return ExplorarPage(page)


@given("que o usuário está autenticado no sistema")
def usuario_autenticado(page, credenciais_validas):
    login = LoginPage(page)
    login.realizar_login(credenciais_validas["email"], credenciais_validas["senha"])


@given("que o usuário está na página Explorar")
def acessar_pagina_explorar(explorar):
    explorar.acessar()


@given('que o filtro "Japonesa" está selecionado')
def filtro_japonesa_selecionado(explorar):
    explorar.selecionar_filtro("Japonesa")


@when(parsers.parse('selecionar o filtro "{categoria}"'))
def selecionar_filtro(explorar, categoria):
    explorar.selecionar_filtro_por_nome(categoria)


@then("a listagem deve exibir apenas restaurantes japoneses")
def validar_apenas_japoneses(explorar):
    explorar.assert_apenas_culinaria("Japonesa")


@then(parsers.parse('o filtro "{categoria}" deve estar destacado'))
def validar_filtro_destacado(explorar, categoria):
    explorar.assert_filtro_ativo(categoria)


@then("a listagem deve exibir restaurantes de diferentes culinárias")
def validar_culinarias_diversas(explorar):
    explorar.assert_culinarias_diversas()
```

**Separação comportamento vs implementação:**

| Camada | Responsabilidade |
|---|---|
| `.feature` (Gherkin) | Descreve **o que** o sistema deve fazer — legível por negócio e QA |
| `test_*.py` (steps) | Conecta cada frase Gherkin a ações Playwright |
| `pages/*.py` (POM) | Encapsula seletores e interações com a interface |

---

## 🔹 4. Organização do projeto

Boas práticas aplicadas:

- **`features/`** — cenários em linguagem natural, separados do código
- **`tests/`** — step definitions finos, delegando lógica às pages
- **`pages/`** — Page Object Model reutilizado da Aula 10 (login) + nova page (explorar)
- **`evidencias/`** — logs de execução para rastreabilidade
- **`conftest.py`** — credenciais e configuração centralizadas
- **`# language: pt`** no feature file — Gherkin em português

---

## 🔹 5. Execução dos testes

### ▶️ Comandos

```bash
cd aula-12
python3 -m pip install -r requirements.txt
python3 -m playwright install chromium
python3 -m pytest
```

### 📊 Resultado

| Métrica | Valor |
|---|---|
| Total de cenários | 2 |
| Passaram | 2 |
| Falharam | 0 |
| Tempo | 9,22s |

### 📸 Evidência (log de execução)

Arquivo: `evidencias/execucao-testes.log`

```
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-9.1.1, pluggy-1.6.0
plugins: base-url-2.1.0, bdd-8.1.0, playwright-0.8.0
collected 2 items

tests/test_filtro_categoria.py::test_filtrar_restaurantes_por_culinária_japonesa PASSED [ 50%]
tests/test_filtro_categoria.py::test_restaurar_listagem_completa_com_filtro_todos PASSED [100%]

============================== 2 passed in 9.22s ===============================
```

---

## 🔹 6. Análise crítica

### O cenário escrito ficou compreensível?

Sim. Frases como *"a listagem deve exibir apenas restaurantes japoneses"* descrevem comportamento de negócio sem mencionar seletores CSS, APIs ou frameworks. Um Product Owner ou analista de negócio consegue ler o `.feature` e validar se o comportamento está correto.

### O teste automatizado ficou legível?

Sim. Os step definitions são curtos (1–3 linhas) e delegam a complexidade para `ExplorarPage`. O arquivo de teste funciona como "cola" entre Gherkin e Playwright, sem lógica de negócio misturada.

### O BDD ajudou a entender o comportamento?

Sim. Escrever primeiro o `.feature` forçou a pensar no **comportamento esperado** antes da implementação técnica — alinhado ao espírito do BDD. O Contexto compartilhado (`Background`) evitou repetir "login + navegar" em cada cenário.

### Quais dificuldades surgiram?

- **Integração pytest-bdd + Playwright:** garantir que a fixture `page` do Playwright esteja disponível nos steps
- **Steps parametrizados:** usar `parsers.parse('selecionar o filtro "{categoria}"')` para reutilizar o mesmo step com valores diferentes
- **Pré-condição do Cenário 2:** o step `Dado que o filtro "Japonesa" está selecionado` precisou ser definido separadamente do `When`
- **Sincronização:** aguardar o carregamento da grid após cada clique no filtro (spinner "Buscando...")

### Os seletores foram frágeis?

**Parcialmente.** Seletores por `data-cuisine` e `#restaurantGrid` são relativamente estáveis (atributos semânticos no HTML). Porém, a validação de culinária depende do texto dentro de `.card-meta`, que pode mudar com alterações de layout.

### O teste ficou dependente da interface?

Sim. BDD funcional sempre depende da UI. A mitigação foi usar Page Objects — se a interface mudar, apenas `explorar_page.py` precisa ser atualizado, mantendo os cenários Gherkin intactos.

### O cenário representa realmente uma regra de negócio?

Sim. "Filtrar por culinária japonesa exibe apenas restaurantes japoneses" é regra de negócio documentada na Aula 4 (estratégia de testes) e validada manualmente na Aula 6 (CT-04). O BDD transforma essa regra em documentação executável.

### O que tornaria o teste mais robusto?

- Adicionar `data-testid` nos botões de filtro (acordado com desenvolvimento)
- Interceptar a resposta da API `/restaurants/` e validar o payload, não só a UI
- Executar em CI/CD antes de cada deploy
- Cenário negativo: filtro sem resultados exibe "Nenhum restaurante encontrado"

---

## 🔹 7. Reflexão no contexto do LocalEats

### BDD melhora comunicação entre equipe?

Sim. O arquivo `.feature` pode ser lido por desenvolvedores, QA, PO e até stakeholders do restaurante. Em um projeto com problemas de requisitos ambíguos (Aula 3), BDD cria um contrato claro de comportamento.

### Todo teste deve ser escrito em BDD?

Não. Testes unitários (Aula 9) e alguns E2E técnicos (Aula 10) não precisam de Gherkin. BDD é mais valioso para **fluxos de negócio** que envolvem múltiplos papéis na equipe.

### Quando vale a pena usar BDD?

- Fluxos críticos de negócio (pedido, busca, filtro)
- Quando requisitos precisam ser documentados de forma viva
- Quando QA, dev e negócio precisam alinhar comportamento esperado
- Quando testes manuais são repetitivos e bem definidos (como CT-04 da Aula 6)

### O comportamento ficou mais claro?

Sim. Comparando com o teste E2E da Aula 10 (login), onde o comportamento está implícito no código Python, o BDD deixa explícito: *"Como usuário autenticado, quero filtrar por culinária, para encontrar opções de acordo com minha preferência."*

### Como isso ajuda no projeto do grupo?

O LocalEats tem bugs conhecidos na busca textual (CT-05, CT-06) mas filtro por categoria funciona (CT-04). Automatizar este fluxo com BDD:
1. **Documenta** o comportamento correto como referência
2. **Detecta regressões** se alguém quebrar o filtro em futuras versões
3. **Serve de modelo** para automatizar outros fluxos (pedidos, favoritos) no mesmo padrão
4. **Aproxima** a documentação de testes da linguagem de negócio, reduzindo ambiguidade identificada na Aula 3

---

## 💡 Conclusão

A atividade demonstrou como BDD transforma regras de negócio em cenários legíveis e executáveis. A integração pytest-bdd + Playwright + Page Object Model mantém a separação entre **comportamento** (`.feature`), **orquestração** (steps) e **implementação** (pages) — respondendo à pergunta central: *"O comportamento esperado do sistema está claramente documentado e automaticamente validado?"* — com **2 cenários passando em 9 segundos**.
