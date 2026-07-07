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
