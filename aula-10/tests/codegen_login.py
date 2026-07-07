# Código gerado pelo Playwright Codegen como ponto de partida.
# Comando: playwright codegen https://local-eats-unisenac.vercel.app/static/login.html
#
# Observação: este arquivo NÃO deve ser usado diretamente em produção.
# Foi refatorado para pages/login_page.py e tests/test_login.py.

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.locator("#loginEmail").fill("filiprofit2@gmail.com")
    page.locator("#loginPassword").fill("qwQW12!@")
    page.locator("#loginForm button[type='submit']").click()

    expect(page).to_have_url(re.compile(r".*/index\.html"))
    expect(page.locator("#userBadge")).to_contain_text("Olá,")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
