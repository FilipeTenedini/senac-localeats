# 🧩 Atividade PBL – Aula 10
## Testes Funcionais Automatizados – LocalEats

> Disciplina: Qualidade de Software  
> Prof.: Luciano Zanuz  
> Integrante: Filipe Tenedini Domingos

---

## 📁 Estrutura do Projeto

```
aula-10/
├── pages/
│   ├── __init__.py
│   └── login_page.py          # Page Object Model (POM)
├── tests/
│   ├── codegen_login.py       # Código bruto gerado pelo Codegen (referência)
│   └── test_login.py          # Testes refatorados com Pytest
├── conftest.py                # Configuração Pytest + credenciais
├── pytest.ini
├── requirements.txt
└── aula-10-testes-funcionais-automatizados.md
```

---

## 🔹 1. Fluxo funcional escolhido

### 🔐 Login de usuário

**Descrição:** Permite autenticar um usuário no sistema LocalEats para acessar funcionalidades como explorar restaurantes, favoritos e pedidos.

**Importância:** Fluxo crítico de entrada no sistema. Sem login funcional, nenhum outro fluxo protegido pode ser validado. Na Aula 6, o CT-01 (login válido) passou, mas o CT-02 revelou mensagem de erro em inglês — reforçando a necessidade de automação contínua.

**Cenários automatizados:**

| Cenário | Tipo | Descrição |
|---|---|---|
| Login válido | Sucesso | Credenciais corretas → redireciona para `index.html` com saudação no header |
| Login inválido | Erro | Senha incorreta → mensagem de erro visível, permanece na tela de login |
| Campos vazios | Borda | Submit sem preencher → validação HTML5 impede envio |

**Credenciais utilizadas nos testes:**

- E-mail: `filiprofit2@gmail.com`
- Senha: configurada em `conftest.py`

---

## 🔹 2. Teste automatizado com Codegen

### 💻 Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/static/login.html
```

### 📄 Código gerado automaticamente

Arquivo de referência: `tests/codegen_login.py`

```python
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("filiprofit2@gmail.com")
    page.get_by_role("textbox", name="Sua senha secreta").click()
    page.get_by_role("textbox", name="Sua senha secreta").fill("***")
    page.get_by_role("button", name="Entrar").nth(1).click()

    expect(page).to_have_url(re.compile(r".*/index\.html"))
    expect(page.locator("#userBadge")).to_contain_text("Olá,")

    context.close()
    browser.close()
```

### 🧠 Observações iniciais

**O que o Codegen fez bem:**
- Gravou o fluxo completo rapidamente (navegação → preenchimento → clique → assertion)
- Identificou os campos de e-mail e senha pela interface
- Gerou assertions básicas de URL e conteúdo

**O que gerou código desnecessário ou frágil:**
- Seletores por `get_by_role("textbox", name="teste@teste.com")` — usa o **placeholder** como nome, não o label real
- `get_by_role("button", name="Entrar").nth(1)` — ambiguidade: existem dois botões "Entrar" na página (toggle + submit)
- Código monolítico sem separação de responsabilidades
- URL hardcoded repetida em vários pontos
- Credenciais expostas diretamente no script gerado
- Sem tratamento de cenários de erro (login inválido, campos vazios)

---

## 🔹 3. Implementação do teste com Pytest

Arquivo: `tests/test_login.py`

```python
from pages.login_page import LoginPage


def test_login_com_sucesso(page, credenciais_validas):
    login = LoginPage(page)

    login.acessar()
    login.realizar_login(credenciais_validas["email"], credenciais_validas["senha"])
    login.assert_login_com_sucesso()


def test_login_com_credenciais_invalidas(page, credenciais_validas):
    login = LoginPage(page)

    login.acessar()
    login.realizar_login(credenciais_validas["email"], "senha_incorreta_123")
    login.assert_mensagem_erro_visivel()
    login.assert_permanece_na_tela_login()


def test_login_com_campos_vazios(page):
    login = LoginPage(page)

    login.acessar()
    login.clicar_entrar()
    login.assert_validacao_campo_obrigatorio()
    login.assert_permanece_na_tela_login()
```

**O que cada teste faz:**

| Teste | Fluxo | Assertion principal |
|---|---|---|
| `test_login_com_sucesso` | Preenche credenciais válidas e clica Entrar | URL = `index.html` + badge exibe "Olá," |
| `test_login_com_credenciais_invalidas` | E-mail válido + senha errada | `#errorMsg` visível + permanece em `login.html` |
| `test_login_com_campos_vazios` | Clica Entrar sem preencher campos | Campo e-mail com `validity.valueMissing = true` |

---

## 🔹 4. Refatoração com Page Object Model (POM)

Arquivo: `pages/login_page.py`

```python
from playwright.sync_api import Page, expect

BASE_URL = "https://local-eats-unisenac.vercel.app/static"


class LoginPage:
    URL = f"{BASE_URL}/login.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.campo_email = page.locator("#loginEmail")
        self.campo_senha = page.locator("#loginPassword")
        self.botao_entrar = page.locator("#loginForm button[type='submit']")
        self.mensagem_erro = page.locator("#errorMsg")
        self.badge_usuario = page.locator("#userBadge")

    def acessar(self) -> None:
        self.page.goto(self.URL)
        self.page.wait_for_load_state("domcontentloaded")

    def realizar_login(self, email: str, senha: str) -> None:
        self.campo_email.fill(email)
        self.campo_senha.fill(senha)
        self.botao_entrar.click()
        self.page.wait_for_timeout(2000)

    def assert_login_com_sucesso(self) -> None:
        expect(self.page).to_have_url(f"{BASE_URL}/index.html", timeout=15000)
        expect(self.badge_usuario).to_contain_text("Olá,", timeout=15000)
```

### Melhorias realizadas na refatoração

| Aspecto | Codegen (antes) | POM (depois) |
|---|---|---|
| Seletores | Por placeholder e `.nth(1)` | Por `#id` estáveis do HTML (`#loginEmail`, `#loginPassword`) |
| Organização | Tudo em um script | Page Object separado do teste |
| Reutilização | Zero | Métodos reutilizáveis (`realizar_login`, `assert_login_com_sucesso`) |
| Credenciais | Hardcoded no script | Centralizadas em `conftest.py` via fixture |
| URL | Hardcoded parcial | Constante `BASE_URL` com caminho `/static/` correto |
| Cenários | Apenas sucesso | 3 cenários (sucesso, erro, borda) |
| Manutenção | Difícil | Alterar seletores em um único lugar |

---

## 🔹 5. Execução dos testes

### ▶️ Comandos

```bash
cd aula-10
python3 -m pip install -r requirements.txt
python3 -m playwright install chromium
python3 -m pytest
```

### 📊 Resultado

| Métrica | Valor |
|---|---|
| Total de testes | 3 |
| Passaram | 3 |
| Falharam | 0 |
| Tempo | 8,73s |

### 📸 Evidência (log de execução)

```
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-9.1.1, pluggy-1.6.0
rootdir: aula-10
plugins: base-url-2.1.0, playwright-0.8.0
collected 3 items

tests/test_login.py::test_login_com_sucesso[chromium] PASSED             [ 33%]
tests/test_login.py::test_login_com_credenciais_invalidas[chromium] PASSED [ 66%]
tests/test_login.py::test_login_com_campos_vazios[chromium] PASSED       [100%]

============================== 3 passed in 8.73s ===============================
```

---

## 🔹 6. Análise crítica dos testes

### O teste quebrou em algum momento? Por quê?

Sim, na primeira execução **todos os 3 testes falharam** com `TimeoutError: waiting for locator("#loginEmail")`. A causa foi a URL incorreta: o Playwright abria `https://local-eats-unisenac.vercel.app/login.html` (sem `/static/`), onde os elementos `#loginEmail` não existem. A correção foi usar URL absoluta com o caminho `/static/login.html`.

### Quais seletores foram mais difíceis?

- **Botão "Entrar"** — o Codegen gerou `.nth(1)` porque há dois botões com o mesmo texto (toggle de aba + submit do formulário). Solução: `#loginForm button[type='submit']`.
- **Campos de input** — o Codegen usou placeholders como seletores (`teste@teste.com`, `Sua senha secreta`). Solução: IDs `#loginEmail` e `#loginPassword` presentes no HTML.
- **Mensagem de erro** — `#errorMsg` existe no DOM mas fica com `display: none` até ocorrer erro. Foi necessário usar `to_be_visible()` com timeout.

### O Codegen ajudou ou gerou problemas?

**Ajudou** como ponto de partida — acelerou o mapeamento do fluxo e identificou os elementos interativos. **Gerou problemas** ao usar seletores frágeis (placeholder, `.nth()`) que quebrariam se o placeholder ou ordem dos botões mudasse.

### O teste é confiável? Por quê?

**Parcialmente confiável.** Os seletores por `#id` são estáveis porque vêm do HTML estático. Porém, o teste depende de:
- Conexão com a API em produção (`/users/login`)
- Credenciais válidas no banco remoto
- Texto "Olá," no badge (pode mudar com i18n)

### O que tornaria o teste mais robusto?

- Usar variáveis de ambiente para credenciais (`LOCAL_EATS_EMAIL`, `LOCAL_EATS_PASSWORD`)
- Substituir `wait_for_timeout(2000)` por `wait_for_url()` ou `wait_for_response()` na API de login
- Adicionar screenshot automático em falhas (`pytest --screenshot=only-on-failure`)
- Executar em CI/CD antes de cada deploy
- Mockar a API em ambiente de teste para independência do backend

### Quais são os riscos de manutenção?

- **Mudança de IDs no HTML** — quebraria todos os seletores (mitigação: usar `data-testid` acordado com devs)
- **Mudança de fluxo de auth** — ex.: OAuth em vez de form login
- **Dependência de produção** — indisponibilidade da API ou mudança de credenciais invalida os testes
- **Mensagens de erro em inglês** — detectado na Aula 6 ("Invalid credentials"); o teste valida visibilidade, não o texto exato

---

## 🔹 7. Reflexão no contexto do LocalEats

### Testes automatizados substituem testes manuais?

Não substituem completamente. Na Aula 6, testes manuais revelaram bugs que automação ainda não cobre (busca textual CT-05, abas Cardápio/Avaliações CT-08). Porém, automação elimina a repetição de fluxos críticos como login, que hoje é testado manualmente a cada release.

### Vale a pena automatizar todos os fluxos?

Não todos. Seguindo a pirâmide da Aula 4, devem ser priorizados:
1. **Login** (entrada no sistema) — já automatizado
2. **Finalização de pedido** (impacto financeiro)
3. **Busca de restaurantes** (funcionalidade central com bugs conhecidos)

Fluxos como favoritos ou filtros visuais podem permanecer manuais ou ser automatizados depois.

### Qual tipo de teste deve ser priorizado?

| Camada | Prioridade no LocalEats | Justificativa |
|---|---|---|
| Unitários (Aula 9) | Alta | Regras de pedido, desconto, taxa — rápidos e baratos |
| E2E funcional (Aula 10) | Média-alta | Fluxos críticos: login, pedido, busca |
| Manuais exploratórios | Média | Encontrar bugs não previstos (CT-06: filtro + busca) |

### Como isso ajuda no projeto do grupo?

O LocalEats tem taxa de falha de 44% nos testes manuais (Aula 6). Automação E2E do login garante que, a cada mudança no frontend, o fluxo de entrada continua funcional — reduzindo regressões e aumentando confiança em deploys. Combinado com testes unitários (Aula 9) e plano de testes (Aula 6), forma uma estratégia em camadas que endereça os problemas de qualidade identificados desde a Aula 3.

---

## 💡 Conclusão

A automação funcional com Playwright + Pytest + POM transformou um fluxo manual repetitivo (login) em 3 testes executáveis em menos de 9 segundos. O Codegen foi útil como ponto de partida, mas a refatoração com seletores estáveis e Page Object Model foi essencial para obter testes legíveis, organizados e mantíveis — alinhados com a mentalidade: *"Se a interface mudar amanhã, meus testes ainda vão funcionar?"*
