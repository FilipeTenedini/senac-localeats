import pytest

BASE_URL = "https://local-eats-unisenac.vercel.app/static"

CREDENCIAIS_VALIDAS = {
    "email": "filiprofit2@gmail.com",
    "senha": "qwQW12!@",
}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "base_url": BASE_URL,
    }


@pytest.fixture
def credenciais_validas():
    return CREDENCIAIS_VALIDAS.copy()
