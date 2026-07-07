# 🧩 Atividade PBL – Aula 15
## Modelos de Maturidade – LocalEats

> Disciplina: Qualidade de Software  
> Prof.: Luciano Zanuz  
> Integrante: Filipe Tenedini Domingos  
> Sistema: [LocalEats](https://local-eats-unisenac.vercel.app/)

---

## 👥 Integrantes

- Filipe Tenedini Domingos

---

## 📌 Contexto da avaliação

Este diagnóstico avalia a **maturidade do processo de qualidade de software** utilizado pela equipe para analisar, testar e documentar o LocalEats ao longo da disciplina (Aulas 3–14). Quando relevante, também referencia o **processo interno da startup LocalEats** (diagnosticado na Aula 3), que apresenta maturidade significativamente inferior.

**Referências de modelos:**
- **CMMI** (Capability Maturity Model Integration) — níveis 1 a 5
- **MPS.BR** (Melhoria de Processo do Software Brasileiro) — níveis G a A

---

## 🔹 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|---|---|---|---|
| Os requisitos são documentados? | | **X** | |
| Existe controle de mudanças? | | **X** | |
| Há atividades de teste definidas? | **X** | | |
| Os defeitos são registrados? | | **X** | |
| O processo de desenvolvimento é conhecido por toda a equipe? | | **X** | |
| As tarefas são planejadas e acompanhadas regularmente? | | **X** | |
| Existe padronização para implementação de funcionalidades? | | **X** | |
| Os testes são executados antes da entrega das funcionalidades? | **X** | | |
| Há revisão de código ou validação por outro integrante da equipe? | | | **X** |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | **X** | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | **X** | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | **X** | |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | **X** | |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | **X** | |

### Evidências por critério

| Critério | Justificativa |
|---|---|
| Requisitos documentados | Enunciados PBL, casos de teste (CT-01 a CT-09), cenários Gherkin e estratégia de testes existem, mas não há documento único de requisitos (SRS) do LocalEats |
| Controle de mudanças | Git versiona artefatos, porém sem fluxo formal de aprovação, changelog ou gestão de impacto de mudanças |
| Atividades de teste definidas | Estratégia (Aula 4), plano com 9 CTs (Aula 6), TDD (Aula 9), E2E (Aula 10) e BDD (Aula 12) — processo claro e repetível |
| Defeitos registrados | 4 defeitos documentados na Aula 6 (busca, filtro+busca, abas, histórico), mas sem ferramenta de bug tracking (Jira, GitHub Issues) |
| Processo conhecido | Mapeado na Aula 14, porém ainda não formalizado como playbook único; equipe acadêmica reduzida |
| Tarefas planejadas | Cada aula PBL tem escopo definido; plano de testes da Aula 6 estrutura execução, mas sem sprint/kanban formal |
| Padronização | Estrutura consistente (`features/`, `pages/`, `tests/`, `.md`); POM e pytest-bdd padronizados a partir da Aula 10 |
| Testes antes da entrega | `pytest` executado antes de cada entrega automatizada; evidências de log obrigatórias (Aulas 9, 10, 12) |
| Revisão de código | Não há peer review formal; validação é individual antes do commit |
| Ferramentas de gestão | GitHub (versionamento), Pytest, Playwright, pytest-bdd — sem Jira, Trello ou similar |
| Artefatos organizados | Repositório estruturado por aula (`aula-09/` a `aula-12/`, docs na raiz), commits no Git |
| Rastreabilidade | CTs ligados a funcionalidades; BDD liga comportamento a automação; falta matriz formal requisito ↔ teste ↔ código |
| Retrospectivas | Seções de reflexão em todas as aulas; Aula 14 propõe melhoria contínua — sem reunião formal periódica |
| Métricas | Taxa de falha 44% (Aula 6), contagem pass/fail nos logs — sem dashboard ou indicadores contínuos |

---

### Nível de maturidade estimado

| Modelo | Nível | Equivalente |
|---|---|---|
| **CMMI** | **Nível 2 — Gerenciado** | Processos planejados e executados de forma repetível no nível do projeto |
| **MPS.BR** | **Nível E — Gerenciado** | Processos básicos de gestão e qualidade estabelecidos e executados |

> **Referência — processo interno do LocalEats (startup):** **CMMI Nível 1 (Inicial) / MPS.BR Nível G** — processo ad hoc, sem QA formal, qualidade diluída entre desenvolvedores (Aula 3).

---

### Justificativa da classificação

A equipe evoluiu de um diagnóstico inicial de processo caótico (Aula 3) para um fluxo **planejado e repetível** dentro do escopo acadêmico: estratégia de testes, plano formal, automação unitária/E2E/BDD e documentação versionada no GitHub. Isso caracteriza o **nível Gerenciado** — práticas existem e são aplicadas de forma consistente **no projeto**, mas ainda não atingem o nível **Definido** (CMMI 3 / MPS.BR D), pois faltam padronização organizacional, revisão por pares, rastreabilidade formal e métricas sistemáticas. A presença de 10 critérios "Parcial" e apenas 1 "Não" indica maturidade intermediária com caminho claro de evolução. O produto LocalEats em si permanece no nível Inicial, evidenciando que maturidade de processo da equipe de QA acadêmica ainda não se reflete no processo de desenvolvimento da startup analisada.

---

## 🔹 2. Identificação de Lacunas

| # | Lacuna | Impacto |
|---|---|---|
| 1 | **Ausência de revisão de código / validação por pares** | Defeitos de lógica e inconsistências (ex.: IDs no histórico de pedidos — CT-09) podem passar despercebidos; concentra conhecimento em um único integrante |
| 2 | **Falta de ferramenta formal de registro de defeitos** | Bugs documentados apenas em relatórios Markdown (Aula 6); dificulta rastreamento, priorização, reabertura e comunicação com desenvolvimento |
| 3 | **Métricas de qualidade não sistematizadas** | Taxa de falha (44%) e pass/fail existem pontualmente, mas sem indicadores contínuos (cobertura, densidade de defeitos, tempo de correção) — impede gestão quantitativa |
| 4 | **Rastreabilidade incompleta entre requisitos e testes** | Cenários BDD e CTs existem, mas sem matriz que ligue requisito → caso de teste → automação → resultado; dificulta auditoria e impacto de mudanças |
| 5 | **Processo do LocalEats (startup) permanece no nível Inicial** | Mesmo com QA acadêmico estruturado, o sistema em produção continua com 44% de falha nos testes manuais — gap entre diagnóstico e correção efetiva |

---

## 🔹 3. Propostas de Melhoria

| # | Melhoria | Benefício | Nível CMMI alvo |
|---|---|---|---|
| 1 | **Implementar GitHub Issues como bug tracker** — registrar cada defeito (CT-05, CT-06, CT-08, CT-09) com severidade, status e responsável | Rastreabilidade de defeitos, comunicação estruturada, histórico de correções | Gerenciado → Definido |
| 2 | **Estabelecer Definition of Done (DoD) com checklist obrigatório** — testes passando, revisão por par, documentação atualizada, evidências anexadas | Padroniza entregas, reduz variação entre integrantes, eleva qualidade antes do deploy | Definido |
| 3 | **Integrar testes automatizados ao CI/CD (GitHub Actions)** — pipeline executando `pytest` (unitário + E2E + BDD) a cada push | Detecção precoce de regressões (ex.: login, filtro); testes deixam de ser manuais/ad hoc | Definido |
| 4 | **Criar matriz de rastreabilidade requisito ↔ teste** — ligar funcionalidades do LocalEats aos CTs, cenários Gherkin e scripts automatizados | Visibilidade de cobertura, impacto de mudanças mensurável, auditoria facilitada | Definido |
| 5 | **Definir métricas básicas de qualidade** — taxa de pass/fail por sprint, quantidade de defeitos abertos/fechados, cobertura de automação | Permite gestão quantitativa; base para evoluir a CMMI 4 / MPS.BR C | Quantitativamente Gerenciado |
| 6 | **Instituir retrospectivas quinzenais** — revisar processo, métricas e lições aprendidas (modelo da Aula 14) | Melhoria contínua sistemática; cultura de aprendizado organizacional | Otimização |

---

## 📊 Comparativo de evolução

```text
                    LocalEats (startup)          Equipe QA (disciplina)
                    ───────────────────          ──────────────────────
Aula 3              ■ Nível 1 — Inicial          ■ Nível 1 — Inicial
Aula 6              ■ Nível 1 — Inicial          ■ Nível 2 — Gerenciado (parcial)
Aula 9–12           ■ Nível 1 — Inicial          ■ Nível 2 — Gerenciado
Aula 14–15          ■ Nível 1 — Inicial          ■ Nível 2 — Gerenciado (consolidado)
Próximo passo       DoD + CI/CD + bug tracker    ■ Nível 3 — Definido
```

---

## 💡 Conclusão

O processo da equipe de Qualidade de Software encontra-se no **nível Gerenciado (CMMI 2 / MPS.BR E)**: práticas de teste, automação e documentação são **planejadas, executadas e repetíveis** dentro do projeto acadêmico. Entretanto, lacunas em revisão por pares, métricas sistemáticas e rastreabilidade formal impedem a classificação no nível **Definido**.

Paradoxalmente, o **produto LocalEats** permanece no **nível Inicial** — comprovado pelos 44% de falha nos testes manuais (Aula 6) e pela ausência de QA na startup (Aula 3). Isso demonstra que **maturidade de processo da equipe de QA não se transfere automaticamente ao produto**; é necessário que as melhorias propostas sejam adotadas também pelo processo de desenvolvimento do LocalEats.

A evolução natural do processo — via CI/CD, bug tracking, DoD e métricas — posicionaria a equipe no **nível Definido (CMMI 3 / MPS.BR D)**, alinhando prática acadêmica com o que organizações maduras executam em projetos reais de software.
