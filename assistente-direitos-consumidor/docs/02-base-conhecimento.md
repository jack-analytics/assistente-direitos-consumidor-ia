# 02 – Base de Conhecimento

## Estratégia de Dados

A base de conhecimento foi estruturada em dois arquivos na pasta `data/`:

---

## Arquivo 1: `direitos_cdc.json`

**Formato:** JSON  
**Conteúdo:** Artigos do CDC organizados por tópico, com linguagem simplificada  

**Estrutura de cada tópico:**
```json
{
  "id": "garantia_legal",
  "titulo": "Garantia Legal",
  "artigos": ["Art. 18", "Art. 26"],
  "resumo": "Explicação simples do direito",
  "prazos": {...},
  "analogia": "Comparação do dia a dia para entender a lei",
  "o_que_pode_exigir": ["lista de direitos"],
  "como_exigir": "Script do que falar ou escrever",
  "como_loja_pode_negociar": ["formas legais de resposta da loja"],
  "atencao": "Pontos importantes a não esquecer"
}
```

**Tópicos cobertos:**
- Garantia Legal (Art. 18/26)
- Direito de Arrependimento — compras online (Art. 49)
- Entrega de Produto (Art. 35)
- Cobrança Indevida (Art. 42)
- Propaganda Enganosa (Art. 30/31/37)
- Produto Vencido (Art. 18/64)
- Discriminação e Recusa de Atendimento (Art. 39)
- Troca sem defeito em loja física (sem cobertura legal — declarado explicitamente)
- Serviços com Defeito (Art. 20/26)

**Fontes:**
- Lei nº 8.078/1990 (CDC) — texto público no planalto.gov.br
- Procon-SP (materiais educativos públicos)

---

## Arquivo 2: `situacoes_comuns.csv`

**Formato:** CSV  
**Conteúdo:** 12 situações mapeadas com direitos, como agir e como a loja pode reagir  

**Colunas:**
| Campo | Descrição |
|---|---|
| `situacao` | Descrição do problema comum |
| `categoria` | Tipo de proteção legal |
| `artigo_cdc` | Artigo(s) do CDC aplicável(is) |
| `prazo_reclamacao` | Prazo legal para reclamar |
| `direito_principal` | O principal direito do consumidor |
| `como_agir_consumidor` | Orientação prática de ação |
| `como_loja_pode_agir` | Como o comércio pode responder legalmente |
| `orgao_reclamacao` | Canal de denúncia recomendado |

---

## Como Expandir a Base

Para adicionar novos tópicos:

1. No `direitos_cdc.json`, adicione um novo objeto no array `topicos` seguindo a estrutura existente
2. No `situacoes_comuns.csv`, adicione uma nova linha com os campos preenchidos
3. O system prompt em `src/app.py` é carregado dinamicamente, então as novas informações são incluídas automaticamente na próxima sessão

**Fontes recomendadas para expansão:**
- [Planalto - CDC completo](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm)
- [Procon-SP - Cartilhas](https://www.procon.sp.gov.br)
- [Senacon - Publicações](https://www.gov.br/senacon)
