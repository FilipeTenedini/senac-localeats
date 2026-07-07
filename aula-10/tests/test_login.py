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
