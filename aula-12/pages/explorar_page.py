from playwright.sync_api import Page, expect

BASE_URL = "https://local-eats-unisenac.vercel.app/static"


class ExplorarPage:
    URL = f"{BASE_URL}/index.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.grid = page.locator("#restaurantGrid")
        self.cards = page.locator(".rest-card")

    def acessar(self) -> None:
        self.page.goto(self.URL)
        self.aguardar_listagem_carregada()

    def aguardar_listagem_carregada(self) -> None:
        expect(self.grid).not_to_contain_text("Carregando os melhores restaurantes", timeout=15000)
        expect(self.cards.first).to_be_visible(timeout=15000)

    def selecionar_filtro(self, categoria: str) -> None:
        self.page.locator(f'.filter-btn[data-cuisine="{categoria}"]').click()
        self.aguardar_listagem_carregada()

    def selecionar_filtro_por_nome(self, nome: str) -> None:
        if nome == "Todos":
            self.page.locator('.filter-btn[data-cuisine=""]').click()
        else:
            self.selecionar_filtro(nome)
        self.aguardar_listagem_carregada()

    def assert_filtro_ativo(self, nome: str) -> None:
        if nome == "Todos":
            filtro = self.page.locator('.filter-btn[data-cuisine=""].active')
        else:
            filtro = self.page.locator(f'.filter-btn[data-cuisine="{nome}"].active')
        expect(filtro).to_be_visible()

    def assert_apenas_culinaria(self, culinaria: str) -> None:
        total = self.cards.count()
        assert total > 0, "Nenhum restaurante exibido na listagem"

        for indice in range(total):
            card = self.cards.nth(indice)
            meta = card.locator(".card-meta")
            expect(meta).to_contain_text(culinaria)

    def assert_culinarias_diversas(self) -> None:
        total = self.cards.count()
        assert total >= 5, f"Esperava listagem ampla, mas encontrou {total} restaurantes"

        culinarias = set()
        for indice in range(total):
            texto = self.cards.nth(indice).locator(".card-meta").inner_text()
            for tipo in ("Italiana", "Japonesa", "Brasileira", "Mexicana"):
                if tipo in texto:
                    culinarias.add(tipo)

        assert len(culinarias) >= 2, "A listagem deveria exibir ao menos duas culinárias diferentes"
