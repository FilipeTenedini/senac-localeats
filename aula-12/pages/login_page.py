from playwright.sync_api import Page, expect

BASE_URL = "https://local-eats-unisenac.vercel.app/static"


class LoginPage:
    URL = f"{BASE_URL}/login.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.campo_email = page.locator("#loginEmail")
        self.campo_senha = page.locator("#loginPassword")
        self.botao_entrar = page.locator("#loginForm button[type='submit']")

    def realizar_login(self, email: str, senha: str) -> None:
        self.page.goto(self.URL)
        self.page.wait_for_load_state("domcontentloaded")
        self.campo_email.fill(email)
        self.campo_senha.fill(senha)
        self.botao_entrar.click()
        self.page.wait_for_url(f"{BASE_URL}/index.html", timeout=15000)
