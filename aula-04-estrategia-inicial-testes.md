# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades

- Busca de restaurantes (por culinária, localização e faixa de preço)
- Visualização de cardápios, fotos e avaliações
- Finalização de pedidos
- Salvamento de locais favoritos
- Recomendações personalizadas
- Compartilhamento de experiências (avaliações e comentários)

---

## 2. Níveis de Teste

### Funcionalidade: Busca de restaurantes

- **Unitário:** validar os filtros individualmente (tipo de culinária, geolocalização, faixa de preço), garantindo que cada parâmetro retorna o conjunto correto de dados
- **Integração:** verificar a comunicação entre o módulo de busca, o serviço de geolocalização e o banco de dados de restaurantes
- **Sistema:** usuário aplica múltiplos filtros simultaneamente e obtém a lista de restaurantes correspondente, ordenada por relevância
- **Aceitação:** usuário busca "comida italiana até R$50 no centro" e visualiza apenas restaurantes que atendem a todos os critérios, sem resultados incorretos

### Funcionalidade: Visualização de cardápios, fotos e avaliações

- **Unitário:** validar a formatação de preços, carregamento de URLs de imagem e cálculo da média de avaliações
- **Integração:** verificar a comunicação entre o front-end e as APIs de cardápio, armazenamento de imagens e serviço de avaliações
- **Sistema:** usuário acessa a página de um restaurante e visualiza cardápio completo, galeria de fotos e lista de avaliações carregados corretamente
- **Aceitação:** usuário consegue navegar pelo cardápio, ampliar fotos e ler avaliações de forma fluida, sem erros de carregamento ou dados ausentes

### Funcionalidade: Finalização de pedidos

- **Unitário:** validar cálculo do valor total do pedido, aplicação de taxas, verificação de campos obrigatórios (endereço, forma de pagamento)
- **Integração:** verificar a comunicação entre o módulo de pedidos, o gateway de pagamento, o sistema de notificação ao restaurante e o banco de dados
- **Sistema:** usuário monta o pedido, insere dados de pagamento e finaliza; o restaurante recebe exatamente um pedido com os itens corretos
- **Aceitação:** usuário conclui um pedido do início ao fim sem erros, recebe confirmação e o restaurante é notificado corretamente — sem duplicação

### Funcionalidade: Salvamento de locais favoritos

- **Unitário:** validar as operações de adicionar e remover favoritos, garantindo a persistência correta do estado (favoritado/não favoritado)
- **Integração:** verificar a comunicação entre o componente de favoritos no front-end e a API de perfil do usuário no back-end
- **Sistema:** usuário favorita um restaurante, navega para outras telas, retorna e o restaurante permanece na lista de favoritos
- **Aceitação:** usuário consegue salvar e acessar seus restaurantes favoritos de forma rápida e consistente entre sessões

### Funcionalidade: Recomendações personalizadas

- **Unitário:** validar o algoritmo de recomendação isoladamente — dado um perfil com histórico de buscas e favoritos, verificar se os restaurantes sugeridos são coerentes
- **Integração:** verificar a comunicação entre o serviço de recomendações, o histórico de navegação do usuário e o catálogo de restaurantes
- **Sistema:** usuário com histórico de buscas por "comida japonesa" recebe recomendações de restaurantes japoneses ao acessar a tela inicial
- **Aceitação:** usuário percebe que as recomendações são relevantes e condizentes com seus interesses, sem sugestões desconexas

### Funcionalidade: Compartilhamento de experiências (avaliações e comentários)

- **Unitário:** validar campos obrigatórios da avaliação (nota, texto), limite de caracteres e sanitização de entrada contra conteúdo malicioso
- **Integração:** verificar a comunicação entre o formulário de avaliação, a API de avaliações e o banco de dados, garantindo persistência correta
- **Sistema:** usuário escreve uma avaliação, submete, atualiza a página e a avaliação permanece visível com os dados corretos
- **Aceitação:** usuário publica uma avaliação e ela aparece na página do restaurante de forma imediata e persistente — sem desaparecer após atualização

---

## 3. Prioridades e Riscos

**Alta prioridade:**

- **Finalização de pedidos** → é a funcionalidade central do negócio. Erros aqui causam impacto financeiro direto (cobranças indevidas, pedidos duplicados aos restaurantes, perda de receita). Sem pedidos funcionando, a plataforma não gera valor.
- **Busca de restaurantes** → é o ponto de entrada da experiência do usuário. Resultados incorretos fazem o usuário não encontrar o que procura, gerando frustração imediata e abandono. É um dos problemas já relatados em produção.
- **Compartilhamento de experiências** → avaliações que desaparecem já foram reportadas pelos usuários. Perda de conteúdo gerado pelo usuário destrói a confiança na plataforma e desestimula a participação da comunidade.

**Justificativa:**
Falhas nessas funcionalidades comprometem diretamente a operação da plataforma, causam prejuízo financeiro aos comerciantes e destroem a confiança dos usuários. São problemas já observados em produção, o que eleva ainda mais a urgência.

**Média prioridade:**

- **Visualização de cardápios, fotos e avaliações** → problemas de carregamento prejudicam a decisão de compra, mas não impedem o uso da plataforma.
- **Recomendações personalizadas** → recomendações ruins reduzem o engajamento, mas o usuário ainda pode buscar restaurantes manualmente.

**Justificativa:**
Afetam a qualidade da experiência e o engajamento, mas o usuário consegue contornar os problemas usando outras funcionalidades.

**Baixa prioridade:**

- **Salvamento de locais favoritos** → é uma funcionalidade de conveniência. Falhas aqui não impedem o uso do sistema nem causam impacto financeiro.

**Justificativa:**
Não bloqueia nenhum fluxo crítico. O usuário pode buscar novamente o restaurante desejado caso o favorito não funcione.

---

## 4. Pirâmide de Testes

- **Maior foco (base da pirâmide): Testes unitários** — devem cobrir a maior parte do sistema, especialmente validações de dados, cálculos (valor de pedido, média de avaliações), filtros de busca e regras de negócio. São rápidos, baratos de manter e fornecem feedback imediato ao desenvolvedor. Permitem detectar a maioria dos defeitos antes mesmo da integração.

- **Médio foco (meio da pirâmide): Testes de integração** — devem cobrir os pontos de conexão entre componentes: comunicação com banco de dados, chamadas a APIs externas (pagamento, geolocalização), sincronização entre versão web e mobile. Muitos dos problemas relatados (pedidos duplicados, inconsistências web/mobile) indicam falhas justamente nessa camada.

- **Menor foco (topo da pirâmide): Testes de sistema e aceitação (E2E)** — devem cobrir os fluxos críticos completos (finalizar pedido, busca com filtros, publicar avaliação). São os mais lentos e caros de manter, por isso devem ser usados com parcimônia, focando nos caminhos de maior risco e valor de negócio.

**Justificativa:**
A pirâmide de testes distribui o esforço de forma eficiente: a base larga de testes unitários garante cobertura ampla com baixo custo; a camada intermediária de integração captura defeitos nas fronteiras entre componentes (onde muitos dos problemas atuais se manifestam); e o topo reduzido de testes E2E valida a experiência real do usuário nos fluxos mais importantes. Essa estratégia maximiza a detecção de defeitos com o menor custo total de manutenção. No contexto da LocalEats, a camada de integração merece atenção especial, pois a maioria dos defeitos relatados (duplicação de pedidos, inconsistências entre plataformas, perda de avaliações) aponta para falhas na comunicação entre componentes.

---

## 5. Testes em Produção

- **Uso de monitoramento sintético (smoke tests):** execução periódica e automatizada de verificações nos fluxos críticos (busca, pedido, avaliação) para detectar falhas antes que os usuários as reportem.
- **Uso de feature flags:** liberar funcionalidades novas gradualmente para um percentual reduzido de usuários, monitorando métricas de erro e desempenho antes da liberação completa.
- **Uso de observabilidade e alertas:** monitorar tempo de resposta, taxa de erros e volume de pedidos em tempo real, com alertas automáticos quando os indicadores ultrapassarem limiares aceitáveis — especialmente em horários de pico.
- **Aplicar em:** fluxo de finalização de pedidos (por ser a funcionalidade mais crítica e já apresentar falhas), tempo de resposta geral do sistema (lentidão em horários de pico já foi reportada) e persistência de avaliações (desaparecimento já ocorre em produção).

**Justificativa:**
O sistema já está em produção e apresenta defeitos ativos. Testes em produção não substituem os testes das camadas anteriores, mas são essenciais para detectar problemas que só se manifestam no ambiente real — como degradação de desempenho sob carga real, falhas em dispositivos específicos e comportamentos dependentes de dados reais. No caso da LocalEats, onde a lentidão em horários de pico e a perda de avaliações já ocorrem, monitoramento em produção é indispensável para medir a saúde do sistema continuamente e reagir rapidamente a regressões. Feature flags permitem reduzir o risco de novas entregas, evitando que o problema de "funcionalidades com defeitos em produção" se repita.
