# Diagnóstico de Qualidade – Startup Local Eats

# 1. Diagnóstico da Situação Atual

## 1.1 Papéis atuais identificados

Liste quais papéis vocês acreditam que existem atualmente na startup.

- Desenvolvedor(es) Full Stack
- Gerente de Produto / Product Owner
- Designer de Interface (UI/UX) — possivelmente acumulando outras funções
- Analista de Sistemas (possivelmente acumulado pelo desenvolvedor ou pelo gerente de produto)

---

## 1.2 Quem é responsável pela qualidade hoje?

Descreva como vocês acreditam que a qualidade está sendo tratada atualmente.

> Atualmente, não existe um profissional ou processo dedicado à qualidade de software na Local Eats. A responsabilidade pela qualidade está diluída de forma informal entre os desenvolvedores, que realizam testes pontuais e manuais antes de enviar o código para produção. Não há papel formal de QA, não há critérios de aceitação documentados e não há um fluxo estruturado de validação. Isso significa que a qualidade depende exclusivamente da atenção individual de cada desenvolvedor, sem padronização ou cobertura sistemática.

---

## 1.3 Problemas identificados

Liste os principais problemas relacionados à falta de organização da qualidade.

- Clientes relatam erros ao finalizar pedidos — funcionalidade crítica chegando com defeitos à produção
- Restaurantes recebem pedidos duplicados — falha de integridade nos dados e no fluxo de processamento
- Funcionalidades chegam à produção com defeitos — ausência de testes e validações antes do deploy
- Não está claro quem é responsável por garantir a qualidade — falta de papéis e processos definidos
- Ausência de registro e acompanhamento de defeitos — bugs não são rastreados de forma organizada
- Falta de critérios de aceitação — funcionalidades são entregues sem validação contra requisitos definidos

---

## 1.4 Impactos desses problemas

Explique quais são as consequências desses problemas para o sistema e para os usuários.

> **Para os clientes:** erros ao finalizar pedidos geram frustração, desconfiança e abandono da plataforma. Um cliente que não consegue concluir um pedido dificilmente retorna.
>
> **Para os restaurantes:** pedidos duplicados causam desperdício de insumos, retrabalho operacional e prejuízo financeiro. Isso abala a confiança dos comerciantes na plataforma e pode levar ao descredenciamento.
>
> **Para o negócio:** a entrega contínua de funcionalidades com defeitos compromete a reputação da startup, aumenta o custo de manutenção corretiva (que é significativamente maior que o custo de prevenção) e desacelera a evolução do produto, pois a equipe gasta tempo corrigindo bugs em vez de desenvolver novas funcionalidades.
>
> **Para a equipe:** sem responsabilidades claras, os desenvolvedores acumulam funções, o que gera sobrecarga, desmotivação e uma cultura reativa em vez de preventiva.

---

## 1.5 A qualidade é responsabilidade de quem?

Explique se a qualidade deve ser responsabilidade de uma pessoa ou de toda a equipe.

> A qualidade de software deve ser entendida como uma **responsabilidade compartilhada por toda a equipe**, e não atribuída exclusivamente a uma única pessoa. Cada membro contribui para a qualidade em diferentes etapas do ciclo de desenvolvimento:
>
> - O **Analista de Sistemas** contribui ao definir requisitos claros e critérios de aceitação
> - O **Desenvolvedor** contribui ao escrever código limpo, realizar testes unitários e participar de revisões de código
> - O **QA** contribui ao planejar e executar testes, identificar riscos e validar funcionalidades
> - O **DevOps** contribui ao garantir ambientes estáveis e pipelines de entrega confiáveis
> - O **Gerente de Produto** contribui ao priorizar a qualidade nas decisões de negócio
>
> No entanto, a existência de um **papel dedicado de QA** é fundamental para orquestrar, sistematizar e promover a cultura de qualidade dentro da equipe. O QA atua como guardião do processo, não como único responsável pelo resultado.

---

# 2. Papéis da Equipe Propostos

Definam quais papéis deveriam existir na equipe da Local Eats.

---

## 2.1 Lista de papéis

- Desenvolvedor Full Stack
- QA / Analista de Qualidade
- Analista de Sistemas
- DevOps
- Gerente de Produto (Product Owner)

---

## 2.2 Descrição dos papéis

Preencha a tabela abaixo:

| Papel | Responsabilidades principais | Relação com a qualidade |
|------|------|------|
| Desenvolvedor Full Stack | Implementar funcionalidades, corrigir bugs, escrever testes unitários e de integração, participar de code reviews | Garante a qualidade no nível do código através de boas práticas de desenvolvimento, testes automatizados e revisão por pares. É o primeiro filtro de qualidade antes que o código chegue ao QA. |
| QA / Analista de Qualidade | Planejar e executar testes funcionais, exploratórios e de regressão; registrar e acompanhar defeitos; definir critérios de aceitação junto ao analista; validar funcionalidades antes do deploy | Papel central na garantia de qualidade. Atua como guardião do processo de testes, identifica riscos e assegura que funcionalidades atendam aos requisitos antes de chegarem à produção. |
| Analista de Sistemas | Levantar e documentar requisitos; elaborar critérios de aceitação; validar regras de negócio; mediar comunicação entre PO e equipe técnica | Contribui para a qualidade ao garantir que os requisitos estejam claros, completos e testáveis. Requisitos mal definidos são uma das maiores fontes de defeitos. |
| DevOps | Gerenciar infraestrutura e ambientes; configurar pipelines de CI/CD; monitorar a saúde da aplicação em produção; gerenciar deploys | Garante a qualidade do ambiente e do processo de entrega. Pipelines automatizados com etapas de teste impedem que código defeituoso chegue à produção. |
| Gerente de Produto (PO) | Definir prioridades do backlog; alinhar expectativas dos stakeholders; validar entregas do ponto de vista de negócio; priorizar correção de defeitos críticos | Influencia a qualidade ao priorizar a correção de defeitos e ao garantir que o time tenha tempo adequado para testes e validações, evitando entregas apressadas. |

---

# 3. Práticas de QA Sugeridas

Sugira práticas que a startup pode adotar para melhorar a qualidade.

---

## 3.1 Lista de práticas

- Testes manuais das funcionalidades principais antes de cada entrega
- Registro e acompanhamento de bugs em ferramenta de gestão
- Testes exploratórios regulares
- Revisão de funcionalidades (Definition of Done) antes da entrega
- Code Review obrigatório entre desenvolvedores

---

## 3.2 Explicação das práticas

### Prática 1: Testes manuais das funcionalidades principais
> Descrição: Antes de cada deploy, o QA deve executar um conjunto de testes manuais cobrindo os fluxos críticos do sistema (finalizar pedido, busca de restaurantes, envio de pedido ao restaurante). Isso cria uma barreira de proteção contra defeitos nos caminhos mais importantes da aplicação, evitando que erros como pedidos duplicados ou falhas na finalização cheguem aos usuários.

### Prática 2: Registro e acompanhamento de bugs
> Descrição: Todos os defeitos encontrados devem ser registrados em uma ferramenta de gestão (como Jira, Linear ou GitHub Issues) com informações padronizadas: descrição, passos para reproduzir, severidade e responsável. Isso permite rastrear o ciclo de vida de cada bug, medir a taxa de defeitos e identificar áreas do sistema que precisam de mais atenção.

### Prática 3: Testes exploratórios regulares
> Descrição: Além dos testes planejados, o QA deve realizar sessões de testes exploratórios para investigar comportamentos inesperados e cenários que não foram previstos nos requisitos. Essa prática é especialmente eficaz para encontrar defeitos em fluxos alternativos e situações de borda que testes roteirizados não cobrem.

### Prática 4: Revisão de funcionalidades (Definition of Done)
> Descrição: Estabelecer critérios claros e documentados que uma funcionalidade deve atender antes de ser considerada "pronta" (ex.: código revisado, testes executados, documentação atualizada, aprovação do QA). Isso evita que funcionalidades incompletas ou com defeitos conhecidos cheguem à produção.

### Prática 5: Code Review obrigatório
> Descrição: Todo código deve ser revisado por pelo menos um outro desenvolvedor antes de ser integrado à branch principal. A revisão de código identifica defeitos lógicos, problemas de segurança e violações de padrões antes mesmo da fase de testes, reduzindo o volume de bugs que o QA precisa encontrar.

---

# 4. Anúncios de Contratação

A startup decidiu contratar novos profissionais. Crie anúncios de vagas.

> Mínimo: 2 vagas

---

## 4.1 Vaga 1 – Analista de Qualidade de Software (QA)

### Descrição da vaga
> A Local Eats está buscando um(a) Analista de Qualidade de Software (QA) para integrar a equipe de desenvolvimento e estruturar os processos de garantia de qualidade da plataforma de pedidos online. A pessoa atuará de forma colaborativa com desenvolvedores, analistas e o gerente de produto para identificar riscos, planejar e executar testes, e garantir que as funcionalidades entregues atendam aos requisitos de qualidade. Empresa: Local Eats | Local: Porto Alegre – RS | Modelo: Híbrido

### Responsabilidades
- Planejar e executar testes funcionais, exploratórios e de regressão
- Identificar, registrar e acompanhar defeitos em ferramenta de gestão
- Colaborar com analistas de sistemas na definição de critérios de aceitação
- Realizar testes exploratórios em funcionalidades novas e existentes
- Validar funcionalidades antes da entrega em produção
- Apoiar a equipe de desenvolvimento na melhoria contínua da qualidade
- Contribuir para a criação e manutenção de documentação de testes

### Requisitos obrigatórios
- Conhecimento em técnicas e fundamentos de testes de software
- Capacidade de identificar, documentar e comunicar defeitos de forma clara
- Conhecimento básico de desenvolvimento de sistemas (lógica, APIs, banco de dados)
- Boa comunicação, pensamento analítico e trabalho em equipe
- Experiência ou conhecimento em testes de aplicações web e mobile

### Requisitos desejáveis
- Experiência com ferramentas de gestão de defeitos (Jira, Linear, GitHub Issues)
- Noções de automação de testes (Selenium, Cypress, Playwright)
- Conhecimento de versionamento com Git
- Experiência com metodologias ágeis (Scrum, Kanban)
- Familiaridade com testes de API (Postman, Insomnia)

### Certificações desejáveis
- ISTQB – CTFL (Certified Tester Foundation Level)
- CTFL-AT (Agile Tester)

---

## 4.2 Vaga 2 – Engenheiro(a) DevOps

### Descrição da vaga
> A Local Eats busca um(a) Engenheiro(a) DevOps para estruturar e manter a infraestrutura da plataforma, implementar pipelines de integração e entrega contínua (CI/CD), e garantir a estabilidade e confiabilidade dos ambientes de desenvolvimento, homologação e produção. Empresa: Local Eats | Local: Porto Alegre – RS | Modelo: Híbrido

### Responsabilidades
- Projetar e manter pipelines de CI/CD com etapas automatizadas de testes e deploy
- Gerenciar infraestrutura em nuvem (provisionamento, escalabilidade, monitoramento)
- Configurar e manter ambientes de desenvolvimento, staging e produção
- Implementar monitoramento e alertas para identificação proativa de falhas
- Automatizar processos de build, testes e deploy
- Colaborar com o time de QA para integrar testes automatizados ao pipeline
- Garantir práticas de segurança na infraestrutura e no processo de entrega

### Requisitos obrigatórios
- Experiência com ferramentas de CI/CD (GitHub Actions, GitLab CI, Jenkins)
- Conhecimento em containerização (Docker) e orquestração (Kubernetes)
- Experiência com serviços de nuvem (AWS, GCP ou Azure)
- Conhecimento em Linux e scripting (Bash, Python)
- Experiência com versionamento Git e estratégias de branching
- Boa comunicação e capacidade de colaboração com equipes de desenvolvimento

### Requisitos desejáveis
- Experiência com Infrastructure as Code (Terraform, Ansible)
- Conhecimento em observabilidade (Prometheus, Grafana, Datadog)
- Familiaridade com práticas de segurança em DevOps (DevSecOps)
- Experiência com bancos de dados relacionais e NoSQL
- Vivência em ambientes ágeis

### Certificações desejáveis
- AWS Certified Solutions Architect ou equivalente em GCP/Azure
- Certified Kubernetes Administrator (CKA)
- HashiCorp Terraform Associate

---

## 4.3 Vaga 3 – Desenvolvedor(a) Full Stack

### Descrição da vaga
> A Local Eats está contratando um(a) Desenvolvedor(a) Full Stack para atuar no desenvolvimento e manutenção da plataforma web e mobile. A pessoa será responsável por implementar novas funcionalidades, corrigir defeitos e contribuir ativamente para a qualidade do código através de testes automatizados e revisões de código. Empresa: Local Eats | Local: Porto Alegre – RS | Modelo: Híbrido

### Responsabilidades
- Desenvolver e manter funcionalidades front-end e back-end da plataforma
- Escrever testes unitários e de integração para o código produzido
- Participar de code reviews e contribuir para a melhoria da base de código
- Corrigir defeitos identificados pelo QA e pelos usuários
- Colaborar com analistas de sistemas na compreensão de requisitos técnicos
- Seguir padrões de código e boas práticas definidos pela equipe
- Participar de cerimônias ágeis e contribuir para a melhoria contínua do processo

### Requisitos obrigatórios
- Experiência com desenvolvimento front-end (React, Vue.js ou Angular)
- Experiência com desenvolvimento back-end (Node.js, Python ou Java)
- Conhecimento em banco de dados relacionais (PostgreSQL, MySQL) e NoSQL (MongoDB)
- Experiência com APIs RESTful
- Conhecimento em versionamento com Git
- Prática com testes unitários e de integração
- Boa comunicação e trabalho em equipe

### Requisitos desejáveis
- Experiência com desenvolvimento mobile (React Native, Flutter)
- Conhecimento em TypeScript
- Familiaridade com Docker e ambientes containerizados
- Experiência com metodologias ágeis (Scrum, Kanban)
- Conhecimento em arquitetura de microsserviços

### Certificações desejáveis
- AWS Certified Developer Associate
- Meta Front-End Developer Certificate
- Certificações em frameworks específicos (React, Node.js)

---

# 5. Conclusão da Equipe

Descreva brevemente:

- O que a equipe aprendeu com a atividade
- Principais dificuldades encontradas
- Principais melhorias propostas para a startup

> A atividade evidenciou que a qualidade de software não é apenas uma etapa final de testes, mas um processo contínuo que permeia todo o ciclo de desenvolvimento. Aprendemos que a ausência de papéis definidos e processos estruturados de QA é uma das principais causas de defeitos em produção, e que o custo de corrigir defeitos cresce exponencialmente conforme avançam no ciclo de vida do software.
>
> As principais dificuldades identificadas na startup foram a falta de um profissional de QA dedicado, a ausência de processos de validação antes do deploy e a indefinição de responsabilidades sobre a qualidade.
>
> As melhorias propostas incluem: contratação de profissionais de QA e DevOps, implementação de práticas básicas de garantia de qualidade (testes manuais, registro de bugs, Definition of Done), adoção de code review obrigatório e estruturação de um pipeline de CI/CD com etapas de testes automatizados. Essas ações, mesmo sendo simples, podem reduzir significativamente a quantidade de defeitos que chegam à produção e restaurar a confiança dos usuários e restaurantes na plataforma.
