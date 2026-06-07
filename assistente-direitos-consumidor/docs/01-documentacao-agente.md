# 01 – Documentação do Agente

## Caso de Uso

**Problema que resolve:**  
Pessoas de baixa e média renda frequentemente não sabem quais direitos têm como consumidores, o que dizer para uma loja, ou quando o CDC (Código de Defesa do Consumidor) se aplica ou não. Isso gera dois problemas: consumidores que ficam no prejuízo por não saberem seus direitos, e conflitos desnecessários por exigir algo que a lei não prevê.

**Para quem serve:**  
- Consumidores que acabaram de ter um problema numa loja física ou online e querem saber o que fazer agora
- Funcionários de comércio que querem entender como agir corretamente para evitar reclamações no Procon ou Reclame Aqui

---

## Persona e Tom de Voz

**Nome:** PROCON Digital  
**Perfil:** Um(a) amigo(a) que entende de lei e fala de forma simples — como um familiar que é advogado e te explica tudo sem complicar.

**Características:**
- Linguagem acessível, sem juridiquês
- Usa analogias do dia a dia para explicar a lei
- Direto ao ponto: primeiro o que fazer, depois o porquê
- Acolhedor, mas prático — a pessoa está estressada
- Usa emojis estrategicamente para facilitar a leitura

---

## Arquitetura

```
Usuário → Interface Streamlit → System Prompt + Base de Conhecimento
                                        ↓
                              API Anthropic (Claude)
                                        ↓
                              Resposta estruturada em 6 etapas
                                        ↓
                              Exibida no chat formatada
```

**Fluxo de dados:**
1. Usuário descreve o problema no chat
2. O sistema monta um prompt com o histórico da conversa + base de conhecimento (CDC JSON + situações CSV)
3. A API da Anthropic retorna resposta estruturada em 6 partes fixas
4. A resposta é exibida no chat com formatação visual

---

## Segurança Anti-Alucinação

**Estratégias implementadas:**

1. **Base de conhecimento injetada no system prompt:** O modelo só responde com base no CDC e nos dados carregados dos arquivos `data/`

2. **Instrução explícita de honestidade:** O system prompt instrui o modelo a declarar claramente quando a lei não se aplica (ex: troca sem defeito em loja física)

3. **Estrutura obrigatória de resposta:** As 6 etapas fixas evitam respostas genéricas ou inventadas

4. **Proibição de especialidades adjacentes:** O modelo é instruído a não dar conselhos médicos, jurídicos formais ou policiais

5. **Orientação para Procon quando houver dúvida:** Em casos ambíguos, o assistente orienta a buscar atendimento presencial no Procon

---

## Limitações Conhecidas

- Não cobre todos os artigos do CDC, apenas os mais comuns no consumo cotidiano
- Não tem acesso a jurisprudência ou casos específicos de tribunais
- Não substitui consulta com advogado ou defensor público para casos complexos
- Não tem memória entre sessões diferentes (cada nova sessão começa do zero)
