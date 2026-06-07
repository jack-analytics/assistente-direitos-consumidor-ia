# 04 – Avaliação e Métricas

## Metodologia de Avaliação

O assistente foi avaliado com base em 10 cenários de teste divididos em 3 categorias.

---

## Critérios de Avaliação

| Critério | Peso | Descrição |
|---|---|---|
| **Precisão legal** | 30% | O artigo do CDC citado está correto? |
| **Anti-alucinação** | 25% | Em casos sem cobertura, declarou corretamente? |
| **Clareza da linguagem** | 20% | Linguagem simples e acessível? |
| **Completude da resposta** | 15% | As 6 etapas obrigatórias foram cobertas? |
| **Orientação prática** | 10% | O "como exigir" foi específico e útil? |

---

## Resultados dos Testes

### Categoria A — Situações com direito claro

| Teste | Precisão legal | Anti-aluc. | Clareza | Completude | Resultado |
|---|---|---|---|---|---|
| Produto com defeito (90 dias) | ✅ | ✅ | ✅ | ✅ | ✅ Aprovado |
| Compra online — arrependimento | ✅ | ✅ | ✅ | ✅ | ✅ Aprovado |
| Cobrança indevida em dobro | ✅ | ✅ | ✅ | ✅ | ✅ Aprovado |
| Produto vencido em supermercado | ✅ | ✅ | ✅ | ✅ | ✅ Aprovado |
| Propaganda enganosa preço diferente | ✅ | ✅ | ✅ | ✅ | ✅ Aprovado |

### Categoria B — Situações sem cobertura legal (teste anti-alucinação)

| Teste | Declarou sem cobertura? | Orientação alternativa? | Resultado |
|---|---|---|---|
| Troca sem defeito — loja física | ✅ Sim | ✅ Sim | ✅ Aprovado |
| Produto digital já utilizado | ✅ Sim | ✅ Sim | ✅ Aprovado |
| Compra fora do prazo (> 90 dias) | ✅ Sim | ✅ Sim | ✅ Aprovado |

### Categoria C — Perspectiva do funcionário/loja

| Teste | Entendeu o contexto? | Orientação correta? | Resultado |
|---|---|---|---|
| Funcionário — cliente exigindo troca indevida | ✅ Sim | ✅ Sim | ✅ Aprovado |
| Gerente — cliente com produto vencido | ✅ Sim | ✅ Sim | ✅ Aprovado |

---

## Taxa de Conformidade Geral

| Métrica | Resultado |
|---|---|
| Respostas com artigo correto | 9/9 casos aplicáveis (100%) |
| Casos sem cobertura declarados corretamente | 3/3 (100%) |
| Respostas com as 6 etapas completas | 9/10 (90%) |
| Linguagem avaliada como acessível (simulação) | 10/10 (100%) |

---

## Limitações Identificadas

1. **Casos ambíguos de prazo:** Quando o usuário não informa a data exata da compra, o assistente precisa perguntar — isso foi identificado como ponto de melhoria
2. **Jargão técnico residual:** Em casos de cobrança indevida, "devolução em dobro" gerou dúvida — foi ajustado para incluir o exemplo em reais no prompt
3. **Profundidade jurídica:** Para casos envolvendo dano moral, o assistente orienta corretamente ao Juizado mas não aprofunda — intencional para não ultrapassar o escopo

---

## Próximas Melhorias

- [ ] Adicionar mais artigos do CDC (planos de saúde, serviços bancários)
- [ ] Implementar seleção de categoria antes da pergunta para melhor contextualização
- [ ] Adicionar calculadora de prazos integrada
- [ ] Incluir links dinâmicos para Procon por estado
