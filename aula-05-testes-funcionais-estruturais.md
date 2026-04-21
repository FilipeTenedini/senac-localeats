# Testes Funcionais vs Estruturais – LocalEats

> Disciplina: Qualidade de Software
> Aula 5 – Testes Funcionais vs Estruturais
> Equipe: [Nome da equipe]
> Integrantes: [Nome 1, Nome 2, Nome 3...]

---

## 1. Funcionalidade Escolhida: Busca de Restaurantes

### O que a funcionalidade faz

A busca de restaurantes é o principal ponto de entrada da plataforma LocalEats. Ela permite que o usuário encontre restaurantes aplicando filtros por tipo de culinária (italiana, japonesa, brasileira etc.), localização (bairro, proximidade) e faixa de preço (barato, moderado, caro). O sistema processa esses filtros e retorna uma lista de restaurantes que atendem aos critérios, exibindo nome, avaliação média, distância e faixa de preço.

### O que o usuário espera dela

- Digitar um termo ou selecionar filtros e receber resultados **corretos e relevantes**
- Resultados atualizados em tempo hábil, mesmo em horários de pico
- Comportamento consistente entre a versão web e a versão mobile
- Mensagens claras quando nenhum resultado for encontrado
- Que a combinação de múltiplos filtros funcione de forma coerente (ex.: "japonesa + centro + até R$60" retorne apenas restaurantes que atendam a todos os critérios simultaneamente)

---

## 2. Testes Caixa-Preta (Visão do Usuário)

Nesta abordagem, testamos a funcionalidade **sem conhecer o código interno**, analisando apenas entradas e saídas esperadas — como um usuário real faria.

### Entradas possíveis

| Tipo de entrada | Exemplos |
|---|---|
| Busca textual válida | "pizzaria", "sushi", "churrasco" |
| Filtro de culinária | Selecionar "Italiana" no menu de filtros |
| Filtro de localização | Selecionar bairro "Centro" ou usar geolocalização |
| Filtro de faixa de preço | Selecionar "Até R$30", "R$30–R$60", "Acima de R$60" |
| Combinação de filtros | "Japonesa" + "Centro" + "Até R$60" |
| Busca vazia | Não digitar nada e clicar em buscar |
| Texto sem correspondência | "xyzabc123" — termo que não existe no catálogo |
| Caracteres especiais | "@#$%!", emojis, scripts maliciosos |
| Texto muito longo | String com centenas de caracteres |
| Apenas espaços em branco | "     " |

### Comportamentos esperados

- Busca válida com resultados: exibir lista ordenada de restaurantes que correspondem aos critérios
- Busca sem resultados: exibir mensagem amigável ("Nenhum restaurante encontrado para os filtros selecionados")
- Combinação de filtros: retornar apenas restaurantes que satisfaçam **todos** os filtros aplicados (operação AND)
- Busca vazia: exibir todos os restaurantes ou solicitar que o usuário insira um critério
- Entrada inválida/especial: tratar a entrada sem quebrar a interface, sem exibir erros técnicos e sem executar código injetado
- Texto longo: limitar o campo ou tratar a entrada sem degradar o desempenho

### Situações de erro que podem ser encontradas

- **Resultados incorretos:** buscar "japonesa" e receber restaurantes italianos — problema já relatado pelos usuários do LocalEats
- **Filtros que não combinam corretamente:** aplicar dois filtros e o sistema ignorar um deles, retornando resultados parciais
- **Erro ao buscar sem filtros:** o sistema quebra ou retorna uma página em branco
- **Caracteres especiais causam falha:** a tela exibe erro técnico ou o sistema fica vulnerável a injeção de código (XSS)
- **Inconsistência web/mobile:** mesma busca retorna resultados diferentes dependendo da plataforma — outro problema já observado
- **Lentidão:** busca demora vários segundos em horários de pico, sem feedback visual ao usuário

---

## 3. Testes Caixa-Branca (Visão do Sistema)

Nesta abordagem, testamos com **acesso ao código interno**, analisando a lógica, os fluxos de decisão e as regras implementadas.

### Como a funcionalidade poderia estar implementada

Imaginamos que a busca de restaurantes possui, internamente, a seguinte estrutura lógica:

```
função buscarRestaurantes(texto, filtros):

    // Validação de entrada
    SE texto contém caracteres perigosos ENTÃO
        sanitizar entrada
    SE texto está vazio E nenhum filtro selecionado ENTÃO
        retornar lista padrão OU exibir mensagem

    // Construção da query
    query = construirConsulta(texto)

    SE filtros.culinaria está definido ENTÃO
        query = adicionarFiltroCulinaria(query, filtros.culinaria)
    SE filtros.localizacao está definido ENTÃO
        query = adicionarFiltroLocalizacao(query, filtros.localizacao)
    SE filtros.preco está definido ENTÃO
        query = adicionarFiltroPreco(query, filtros.preco)

    // Execução da consulta
    resultados = executarConsulta(query)

    // Ordenação
    SE resultados não está vazio ENTÃO
        resultados = ordenarPorRelevancia(resultados)
        retornar resultados
    SENÃO
        retornar mensagem "nenhum resultado"
```

### Possíveis estruturas lógicas e decisões internas

- **Validação de entrada:** `if` que verifica se o texto contém caracteres especiais ou é vazio — se essa validação for incompleta, pode permitir injeção de código ou causar erros na query ao banco de dados
- **Combinação de filtros:** cada filtro adiciona uma condição à consulta. Se a lógica usar `OR` em vez de `AND` para combinar filtros, os resultados serão incorretos (ex.: retornar restaurantes que são japoneses **ou** no centro, em vez de japoneses **e** no centro)
- **Cálculo de localização:** lógica que calcula a distância entre o usuário e os restaurantes. Se o cálculo de coordenadas tiver erro de precisão ou não tratar corretamente fusos/projeções, restaurantes distantes podem aparecer como próximos
- **Faixas de preço:** condição que compara o preço médio do restaurante com a faixa selecionada. Erros nos limites das faixas (ex.: um restaurante de R$30 aparece na faixa "até R$30" ou na faixa "R$30–R$60"?) podem causar resultados inconsistentes
- **Ordenação por relevância:** algoritmo que pontua e ordena os resultados. Se o cálculo de pontuação não considerar todos os critérios ou tiver peso desproporcional para algum fator, a ordem dos resultados pode não refletir a relevância real
- **Tratamento de erro do banco:** se a consulta ao banco falhar (timeout, conexão perdida), a função precisa tratar esse erro sem expor detalhes técnicos ao usuário

### Situações que precisam ser testadas no código

- Verificar se **todos os caminhos de decisão** (if/else) são percorridos: com filtro, sem filtro, com texto, sem texto, com resultado, sem resultado
- Testar os **valores de limite** nas faixas de preço: o que acontece exatamente no valor R$30? E no R$60?
- Verificar se a **sanitização de entrada** cobre todos os vetores de ataque conhecidos (SQL injection, XSS)
- Testar se a **construção da query** gera consultas corretas quando nenhum, um, dois ou todos os filtros são aplicados
- Verificar se o **tratamento de exceções** do banco de dados funciona corretamente sob falha de conexão ou timeout
- Testar se a **lógica de combinação de filtros** usa AND e não OR na construção da consulta

---

## 4. Comparação entre as Abordagens

### Principal diferença

| Aspecto | Caixa-Preta (Funcional) | Caixa-Branca (Estrutural) |
|---|---|---|
| **Perspectiva** | Visão do usuário — testa o *que* o sistema faz | Visão do desenvolvedor — testa *como* o sistema faz |
| **Conhecimento do código** | Nenhum — apenas entrada e saída | Total — acesso à lógica interna |
| **Base dos testes** | Requisitos e comportamento esperado | Código-fonte, estruturas e fluxos lógicos |
| **Foco** | Comportamento externo e experiência do usuário | Cobertura de caminhos, condições e regras internas |

A principal diferença é o **ponto de observação**: caixa-preta verifica se o sistema entrega o resultado correto ao usuário, sem se importar com o mecanismo interno; caixa-branca investiga se a lógica interna está correta, cobrindo todos os caminhos de decisão possíveis.

### Que tipo de problema cada abordagem ajuda a encontrar

| Abordagem | Tipos de problema detectados |
|---|---|
| **Caixa-Preta** | Funcionalidades ausentes ou incompletas; resultados incorretos; comportamentos inesperados para o usuário; problemas de usabilidade; falhas em cenários de entrada inválida; inconsistências entre plataformas |
| **Caixa-Branca** | Caminhos lógicos não percorridos (código morto); erros em condições de contorno (limites de faixa de preço); falhas na combinação de condições (AND vs OR nos filtros); tratamento inadequado de exceções; vulnerabilidades de segurança na sanitização de entrada; problemas de desempenho em algoritmos internos |

**Exemplo concreto no LocalEats:** o problema de "resultados incorretos nas buscas" poderia ser detectado por caixa-preta (o usuário busca "japonesa" e recebe "italiana"), mas a **causa raiz** — por exemplo, a query usar OR em vez de AND nos filtros — só seria identificada com caixa-branca, analisando a lógica de construção da consulta.

---

## 5. Reflexão no Contexto do LocalEats

### Qual abordagem parece mais útil para os problemas atuais?

Para a situação atual do LocalEats, **testes caixa-preta são a prioridade imediata**. A razão é prática: os problemas já estão visíveis para os usuários (resultados incorretos, inconsistências entre plataformas, falhas em smartphones específicos) e precisam ser identificados e catalogados rapidamente. Testes caixa-preta permitem mapear os sintomas — quais entradas geram saídas erradas, em quais dispositivos as falhas ocorrem, onde há inconsistências entre web e mobile — sem depender de acesso ou compreensão profunda do código, que foi escrito às pressas.

No entanto, **após identificar os sintomas, testes caixa-branca são indispensáveis** para encontrar as causas raiz. O problema de "resultados incorretos nas buscas", por exemplo, pode ter origens diversas no código: erro na lógica de filtros, falha no cálculo de geolocalização ou problema na query ao banco de dados. Sem analisar o código, a equipe corrigiria os efeitos sem eliminar as causas.

### Apenas uma abordagem seria suficiente?

**Não.** Nenhuma das abordagens sozinha é suficiente para garantir a qualidade do LocalEats. Elas são **complementares**, não concorrentes:

- **Caixa-preta sem caixa-branca:** a equipe consegue detectar que a busca retorna resultados errados, mas não sabe se o problema está no filtro, no banco ou no algoritmo de ordenação. Correções seriam feitas por tentativa e erro.
- **Caixa-branca sem caixa-preta:** a equipe pode garantir 100% de cobertura de código e mesmo assim não encontrar o problema, porque o defeito pode estar em um requisito mal interpretado ou em uma regra de negócio implementada corretamente no código mas incorreta do ponto de vista do usuário.

No cenário do LocalEats, a combinação é especialmente necessária porque o sistema foi desenvolvido às pressas. Isso significa que provavelmente existem tanto **defeitos visíveis ao usuário** (detectáveis por caixa-preta) quanto **defeitos ocultos na lógica interna** (detectáveis apenas por caixa-branca), como caminhos de código não testados, tratamento de exceções ausente e condições de contorno ignoradas. A estratégia ideal é usar caixa-preta para priorizar o que está afetando os usuários agora, e caixa-branca para prevenir que novos defeitos surjam nas correções e nas próximas entregas.
