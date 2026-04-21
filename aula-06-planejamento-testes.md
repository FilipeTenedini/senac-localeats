# Aula 6 – Planejamento e Execução de Testes

# 1. Plano de Testes

## 1.1 Objetivo

Validar as principais funcionalidades do sistema LocalEats (https://local-eats-unisenac.vercel.app/), garantindo que os fluxos críticos — login, busca de restaurantes, favoritos, cardápio e pedidos — funcionem corretamente, apresentem comportamento consistente e ofereçam uma experiência adequada ao usuário final.

---

## 1.2 Escopo

### O que será testado
- Login e autenticação (credenciais válidas, inválidas e campos vazios)
- Busca e filtros de restaurantes (por categoria e texto)
- Visualização de detalhes do restaurante (cardápio, avaliações)
- Funcionalidade de favoritos (favoritar, verificar persistência)
- Fluxo de pedido (adicionar item, finalizar, verificar histórico)

### O que NÃO será testado
- Criação de conta (cadastro de novo usuário)
- Testes de desempenho e carga
- Testes de segurança (SQL injection, XSS)
- Integração com sistemas externos de pagamento
- Versão mobile / responsividade

---

## 1.3 Funcionalidades selecionadas

- Login / Autenticação
- Busca e filtros de restaurantes
- Visualização de detalhes do restaurante (cardápio e avaliações)
- Favoritar restaurante
- Finalização de pedido e histórico

---

## 1.4 Estratégia de Testes

- Tipos de teste:
  - (x) Funcional
  - (x) Usabilidade
  - ( ) Outros

- Abordagem:
  > Testes manuais baseados em cenários definidos previamente, executados diretamente na aplicação web em produção (https://local-eats-unisenac.vercel.app/). Para cada caso de teste, foram documentados os passos executados, os dados de entrada utilizados e o resultado obtido, com evidências descritivas baseadas no comportamento real observado no sistema.

---

## 1.5 Responsáveis

| Nome | Responsabilidade |
|------|----------------|
| [Nome 1] | Planejamento dos testes e definição dos casos |
| [Nome 2] | Execução dos testes e registro de evidências |
| [Nome 3] | Análise dos resultados e identificação de bugs |
| [Nome 4] | Elaboração do relatório final e reflexão |

---

# 2. Casos de Teste

---

## CT-01 – Login com credenciais válidas

**Pré-condição:**
Usuário já possui conta cadastrada no sistema. Não estar logado (sessão limpa).

**Passos:**
1. Acessar https://local-eats-unisenac.vercel.app/static/login.html
2. Preencher o campo E-mail com um email válido cadastrado
3. Preencher o campo Senha com a senha correta
4. Clicar no botão "Entrar"

**Dados de entrada:**
- E-mail: filiprofit@gmail.com
- Senha: (senha válida do usuário)

**Resultado esperado:**
O sistema redireciona para a página principal (index.html), exibindo o nome do usuário no cabeçalho (ex.: "Olá, Filipe") e a lista de restaurantes disponíveis.

---

## CT-02 – Login com credenciais inválidas

**Pré-condição:**
Estar na tela de login, sem sessão ativa.

**Passos:**
1. Acessar https://local-eats-unisenac.vercel.app/static/login.html
2. Preencher o campo E-mail com um email cadastrado
3. Preencher o campo Senha com uma senha incorreta
4. Clicar no botão "Entrar"

**Dados de entrada:**
- E-mail: filiprofit@gmail.com
- Senha: senhaerrada123

**Resultado esperado:**
O sistema permanece na tela de login e exibe uma mensagem de erro clara em português informando que as credenciais são inválidas.

---

## CT-03 – Login com campos vazios

**Pré-condição:**
Estar na tela de login, sem sessão ativa.

**Passos:**
1. Acessar https://local-eats-unisenac.vercel.app/static/login.html
2. Deixar os campos E-mail e Senha vazios
3. Clicar no botão "Entrar"

**Dados de entrada:**
- E-mail: (vazio)
- Senha: (vazio)

**Resultado esperado:**
O sistema impede o envio do formulário e exibe validação nos campos obrigatórios, informando que devem ser preenchidos.

---

## CT-04 – Filtro de restaurantes por categoria

**Pré-condição:**
Estar logado e na página principal (index.html) com a lista completa de restaurantes visível.

**Passos:**
1. Na página principal, localizar os botões de filtro (Todos, Italiana, Japonesa, Brasileira, Mexicana)
2. Clicar no botão "Japonesa"
3. Verificar se a lista de restaurantes foi atualizada

**Dados de entrada:**
- Filtro selecionado: Japonesa

**Resultado esperado:**
A lista exibe apenas restaurantes do tipo "Japonesa" (ex.: Restaurante Sabor 1, 2, 11, 13, 14). Restaurantes de outras categorias não devem aparecer.

---

## CT-05 – Busca textual por termo válido

**Pré-condição:**
Estar logado e na página principal com a lista completa de restaurantes visível. Nenhum filtro de categoria ativo (botão "Todos" selecionado).

**Passos:**
1. Digitar "Brasileira" no campo de busca
2. Clicar no botão "Buscar"
3. Verificar os resultados exibidos

**Dados de entrada:**
- Texto de busca: "Brasileira"

**Resultado esperado:**
A lista exibe apenas restaurantes da categoria "Brasileira" (ex.: Restaurante Sabor 5 e Restaurante Sabor 8).

---

## CT-06 – Busca vazia após uso de filtro

**Pré-condição:**
Estar logado e na página principal. Ter utilizado previamente um filtro de categoria (ex.: "Japonesa").

**Passos:**
1. Clicar no filtro "Japonesa" (lista filtra corretamente)
2. Limpar o campo de busca (deixar vazio)
3. Clicar no botão "Buscar"
4. Clicar no botão "Todos"
5. Verificar se a lista completa de restaurantes é restaurada

**Dados de entrada:**
- Busca: (campo vazio)

**Resultado esperado:**
A lista de restaurantes deve ser restaurada exibindo todos os estabelecimentos disponíveis.

---

## CT-07 – Favoritar restaurante e verificar persistência

**Pré-condição:**
Estar logado no sistema.

**Passos:**
1. Na página principal, clicar em um restaurante (ex.: Restaurante Sabor 5)
2. Na página de detalhes, clicar no botão "Favoritar"
3. Verificar se o botão muda para "Favoritado!"
4. Navegar para "Meus Favoritos" pelo menu
5. Verificar se o restaurante aparece na lista de favoritos

**Dados de entrada:**
- Restaurante selecionado: Restaurante Sabor 5

**Resultado esperado:**
O botão muda de "Favoritar" para "Favoritado!". Ao navegar para "Meus Favoritos", o Restaurante Sabor 5 aparece na lista de restaurantes favoritos do usuário.

---

## CT-08 – Visualizar cardápio do restaurante

**Pré-condição:**
Estar logado no sistema.

**Passos:**
1. Na página principal, clicar em um restaurante (ex.: Restaurante Sabor 5)
2. Na página de detalhes, verificar se a aba "Cardápio" está visível
3. Verificar se os pratos são exibidos com nome, descrição e preço
4. Clicar na aba "Avaliações"
5. Verificar se o conteúdo alterna entre Cardápio e Avaliações

**Dados de entrada:**
- Restaurante: Restaurante Sabor 5

**Resultado esperado:**
O cardápio exibe os pratos disponíveis (Prato Especial 0, 1, 2) com preços em reais. Ao clicar em "Avaliações", o cardápio é ocultado e as avaliações são exibidas. As abas devem funcionar como alternância (toggle).

---

## CT-09 – Finalizar pedido e verificar histórico

**Pré-condição:**
Estar logado e na página de detalhes de um restaurante.

**Passos:**
1. Na página de detalhes do Restaurante Sabor 5, clicar em "+ Adicionar" no Prato Especial 0
2. Clicar no botão "Finalizar Pedido"
3. Verificar se o modal de confirmação é exibido
4. Navegar para "Meus Pedidos"
5. Verificar se o pedido aparece no histórico com o nome do restaurante e do prato

**Dados de entrada:**
- Restaurante: Restaurante Sabor 5
- Item: Prato Especial 0 (R$ 87,12)

**Resultado esperado:**
Após clicar "Finalizar Pedido", o sistema exibe modal "Pedido Realizado!" com confirmação. Na página "Meus Pedidos", o pedido aparece no histórico exibindo o nome do restaurante ("Restaurante Sabor 5"), o nome do item ("Prato Especial 0"), o valor (R$ 87,12) e o status.

---

# 3. Execução dos Testes

| ID     | Resultado | Evidência |
|--------|-----------|-----------|
| CT-01  | **Passou** | Após preencher email e senha válidos e clicar "Entrar", o sistema redirecionou para index.html. O cabeçalho exibiu "Olá, Filipe" e a lista de 15 restaurantes foi carregada corretamente. |
| CT-02  | **Passou** (com ressalva) | O sistema permaneceu na tela de login e exibiu a mensagem "Invalid credentials" em um quadro avermelhado. **Ressalva:** a mensagem está em inglês, enquanto todo o restante do sistema está em português. |
| CT-03  | **Passou** | A validação HTML5 impediu o envio do formulário, exibindo o tooltip nativo do navegador "Preencha este campo." no campo de senha. O sistema não permitiu o login com campos vazios. |
| CT-04  | **Passou** | Ao clicar no filtro "Japonesa", a lista foi atualizada exibindo apenas restaurantes japoneses: Sabor 1 (Centro), Sabor 2 (Zona Sul), Sabor 11 (Centro), Sabor 13 (Zona Sul) e Sabor 14 (Zona Sul). Restaurantes de outras categorias foram ocultados corretamente. |
| CT-05  | **Falhou** | Ao digitar "Brasileira" no campo de busca e clicar "Buscar", **nenhum restaurante foi exibido**. A lista ficou completamente vazia, apesar de existirem restaurantes brasileiros no sistema (Sabor 5 – Zona Sul, Sabor 8 – Zona Norte). A busca textual não retornou os resultados esperados. |
| CT-06  | **Falhou** | Após usar o filtro "Japonesa" e em seguida clicar "Buscar" com o campo vazio, a lista de restaurantes ficou **permanentemente vazia**. Clicar no botão "Todos" não restaurou a listagem. Foi necessário recarregar a página (F5) para que os restaurantes voltassem a aparecer. A combinação de filtro + busca corrompeu o estado da listagem. |
| CT-07  | **Passou** | Ao clicar "Favoritar" no Restaurante Sabor 5, o botão mudou para "Favoritado!". Ao navegar para "Meus Favoritos", a página exibiu o perfil do usuário (Filipe Tenedini Domingos) e o Restaurante Sabor 5 listado na seção "Restaurantes Favoritos". |
| CT-08  | **Falhou** | O cardápio foi exibido corretamente com 3 pratos (Prato Especial 0 – R$ 87,12; Prato Especial 1 – R$ 51,25; Prato Especial 2 – R$ 17,49). Porém, ao clicar na aba "Avaliações", **o cardápio não foi ocultado**. Ambas as seções (Cardápio e Avaliações) foram exibidas simultaneamente na página. As abas não funcionam como alternância — não há troca de conteúdo ao clicar. |
| CT-09  | **Falhou** | O pedido foi finalizado com sucesso: o botão mudou para "Processando..." e em seguida o modal "Pedido Realizado! Seu pedido de teste foi enviado com sucesso." foi exibido. Porém, na página "Meus Pedidos", o pedido exibiu **"Restaurante ID: 6"** em vez de "Restaurante Sabor 5" e **"1x Item Id #19"** em vez de "Prato Especial 0". O histórico utiliza IDs internos do sistema em vez de nomes legíveis, tornando a informação incompreensível para o usuário. |

---

# 4. Análise dos Resultados

- **Quantidade de testes executados:** 9
- **Quantidade de testes que passaram:** 5
- **Quantidade de testes que falharam:** 4

## Principais problemas encontrados

- **Busca textual não funciona (CT-05):** digitar um termo no campo de busca e clicar "Buscar" não retorna os resultados esperados. A funcionalidade de busca por texto está defeituosa, mesmo quando existem restaurantes que correspondem ao termo.

- **Filtro + busca corrompe o estado da listagem (CT-06):** após utilizar um filtro de categoria e depois executar uma busca (mesmo com campo vazio), a lista de restaurantes fica permanentemente vazia. O botão "Todos" não consegue restaurar a listagem. Apenas o reload da página resolve o problema. Isso indica um problema de gerenciamento de estado no front-end.

- **Abas Cardápio/Avaliações não alternam (CT-08):** as abas "Cardápio" e "Avaliações" na página de detalhes do restaurante não funcionam como toggle. Ambas as seções são exibidas ao mesmo tempo na página, independentemente de qual aba está selecionada. A alternância de conteúdo não foi implementada corretamente.

- **Histórico de pedidos exibe IDs internos (CT-09):** a tela "Meus Pedidos" exibe identificadores técnicos do banco de dados ("Restaurante ID: 6", "Item Id #19") em vez dos nomes reais ("Restaurante Sabor 5", "Prato Especial 0"). Isso torna a informação ilegível e inútil para o usuário final.

- **Mensagem de erro em inglês (CT-02):** a mensagem de login inválido exibe "Invalid credentials" em vez de uma mensagem em português, inconsistente com o idioma do restante da aplicação.

---

# 5. Reflexão

**O plano de testes ajudou a organizar melhor o processo? Por quê?**

Sim, o plano de testes foi fundamental para estruturar a execução. Sem ele, a tendência seria testar apenas os "caminhos felizes" (happy paths) e negligenciar cenários de erro e combinações entre funcionalidades. O plano forçou a equipe a pensar antecipadamente em quais cenários validar, o que permitiu identificar problemas que provavelmente passariam despercebidos em testes aleatórios — como a corrupção da listagem ao combinar filtro com busca (CT-06), que só foi descoberta por seguir uma sequência planejada de passos.

**Algum problema só foi identificado durante a execução? Explique.**

Sim, três problemas surgiram apenas durante a execução real:

1. **A combinação filtro + busca corrompendo a listagem (CT-06)** não era prevista como cenário de falha. Só percebemos que a lista não se recuperava porque seguimos a sequência de testes e tentamos usar o filtro "Todos" para restaurar os resultados.

2. **Os IDs internos no histórico de pedidos (CT-09)** só foram vistos ao navegar para "Meus Pedidos" após concluir um pedido. Antes da execução, assumíamos que os nomes dos itens e do restaurante seriam exibidos corretamente.

3. **A mensagem "Invalid credentials" em inglês (CT-02)** é um detalhe de internacionalização que só se percebe na execução real, pois o restante do sistema está em português.

**O que o grupo melhoraria no processo de testes?**

- **Automatizar os testes de regressão:** os testes mais críticos (login, busca, pedido) deveriam ser automatizados para execução contínua, evitando que bugs já corrigidos voltem a aparecer em novas versões.
- **Incluir testes de responsividade e cross-browser:** a atividade focou apenas na versão web desktop. Testar em diferentes navegadores e dispositivos aumentaria a cobertura.
- **Definir critérios de aceitação antes da execução:** ter critérios claros e acordados com a equipe de desenvolvimento facilitaria a decisão sobre se um teste passou ou falhou, especialmente em casos limítrofes.
- **Registrar evidências visuais (screenshots):** capturar telas de cada teste executado fortaleceria o relatório e facilitaria a comunicação dos bugs com a equipe de desenvolvimento.

---

## Conclusão

O sistema LocalEats apresenta funcionalidades básicas operacionais — o login, os filtros por categoria, o fluxo de favoritos e a finalização de pedido funcionam em seus cenários mais simples. Entretanto, **4 dos 9 testes executados falharam**, revelando problemas que comprometem a experiência do usuário e a confiabilidade da plataforma:

A busca textual — funcionalidade central de uma plataforma de descoberta de restaurantes — está defeituosa. A interação entre filtros e busca corrompe o estado da aplicação. O histórico de pedidos é ilegível e as abas de navegação interna não funcionam como esperado.

Esses problemas indicam que o sistema foi entregue sem validação adequada dos fluxos de uso e sem testes de integração entre componentes do front-end. **A plataforma não está em condições de oferecer uma experiência confiável ao usuário final**, especialmente considerando que a busca é a funcionalidade mais usada em um sistema de descoberta de restaurantes.

A recomendação é **priorizar a correção imediata da busca textual e do gerenciamento de estado dos filtros**, pois são as funcionalidades que mais impactam a usabilidade e a proposta de valor do produto.

---

# 6. Conclusão Geral

- **Qualidade geral do sistema testado:** insatisfatória — taxa de falha de 44% (4 de 9 testes) indica problemas estruturais no front-end, especialmente no gerenciamento de estado e na comunicação com a API.

- **Principais pontos positivos:**
  - Login e autenticação funcionam corretamente (login válido, rejeição de credenciais inválidas e validação de campos vazios)
  - Filtro por categoria opera como esperado, filtrando os restaurantes corretamente
  - Funcionalidade de favoritos funciona e persiste entre navegações
  - O fluxo de finalização de pedido conclui com sucesso e gera confirmação visual

- **Principais problemas identificados:**
  - Busca textual não retorna resultados, mesmo para termos válidos
  - Combinação de filtro + busca corrompe permanentemente a listagem (necessita reload)
  - Abas Cardápio/Avaliações não alternam o conteúdo — ambas são exibidas simultaneamente
  - Histórico de pedidos exibe IDs internos do banco em vez de nomes legíveis
  - Mensagem de erro de login em inglês em sistema localizado em português

- **Impressão geral do grupo sobre o processo de testes:** o planejamento de testes transformou uma tarefa que poderia ser aleatória e superficial em um processo organizado e revelador. A definição prévia de cenários de sucesso e de erro nos obrigou a pensar em como o sistema deveria se comportar em diversas situações, e a execução real revelou falhas que dificilmente seriam percebidas sem essa estrutura. A atividade reforçou que **testar não é apenas verificar se algo funciona, mas validar sistematicamente se o sistema atende ao que foi prometido ao usuário**.
