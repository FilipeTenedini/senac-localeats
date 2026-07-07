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
