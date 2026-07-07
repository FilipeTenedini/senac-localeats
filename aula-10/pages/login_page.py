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

    def preencher_email(self, email: str) -> None:
        self.campo_email.fill(email)

    def preencher_senha(self, senha: str) -> None:
        self.campo_senha.fill(senha)

    def clicar_entrar(self) -> None:
        self.botao_entrar.click()

    def realizar_login(self, email: str, senha: str) -> None:
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_entrar()
        self.page.wait_for_timeout(2000)

    def limpar_sessao(self) -> None:
        self.page.evaluate(
            "() => { localStorage.removeItem('userId'); localStorage.removeItem('userName'); }"
        )

    def assert_login_com_sucesso(self) -> None:
        expect(self.page).to_have_url(f"{BASE_URL}/index.html", timeout=15000)
        expect(self.badge_usuario).to_contain_text("Olá,", timeout=15000)

    def assert_mensagem_erro_visivel(self) -> None:
        expect(self.mensagem_erro).to_be_visible(timeout=10000)

    def assert_permanece_na_tela_login(self) -> None:
        expect(self.page).to_have_url(f"{BASE_URL}/login.html")

    def assert_validacao_campo_obrigatorio(self) -> None:
        expect(self.campo_email).to_have_js_property("validity.valueMissing", True)
