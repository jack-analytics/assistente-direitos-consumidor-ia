# ⚖️ Resolva Já — Assistente de Direito do Consumidor

> Projeto desenvolvido para o Lab **"Construa Seu Assistente Virtual Com Inteligência Artificial"** da [DIO](https://dio.me)
> Baseado no repositório de referência: [digitalinnovationone/dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)

---

## 📋 Sobre o Projeto

O **Resolva Já** é um assistente virtual que ajuda qualquer pessoa — consumidor, lojista ou funcionário — a entender direitos e deveres nas relações de compra e venda no Brasil, com linguagem simples, analogias do cotidiano e orientação prática.

O assistente foi pensado para ser usado **no exato momento em que o problema acontece** — dentro da loja, em casa após receber um produto errado, ou ao identificar uma cobrança indevida no cartão.

**Serve para dois públicos:**
- **Consumidores:** Saiba exatamente o que exigir, como agir e o que falar
- **Lojistas e funcionários:** Entenda como responder corretamente e evite reclamações no Procon e Reclame Aqui

---

## 🎯 O Que o Assistente Faz

Para cada situação descrita, responde em **6 etapas estruturadas**:

| Etapa | Conteúdo |
|---|---|
| 🎯 O que está acontecendo | Identifica o problema com clareza |
| ⚖️ O que a lei diz | Explica a lei com analogia simples do cotidiano |
| ✅ O que você pode exigir | Lista clara e objetiva dos direitos |
| 💬 O que falar ou escrever | Script exato para usar na hora |
| 🤝 Como a outra parte pode reagir | Formas legais de negociação para evitar conflito |
| ⚠️ Se não resolver | Procon, Reclame Aqui, consumidor.gov.br, ANPD |

---

## 📚 Legislação de Referência

| Lei | Descrição |
|---|---|
| **CDC — Lei nº 8.078/1990** | Código de Defesa do Consumidor — lei base |
| **Decreto nº 7.962/2013** | Regulamenta o CDC para compras online (e-commerce) |
| **Lei nº 14.181/2021** | Superendividamento e proteção contra fraude em cartão |
| **Decreto nº 11.034/2022** | Obrigações do SAC — atendimento ao consumidor |
| **LGPD — Lei nº 13.709/2018** | Proteção de dados pessoais em compras digitais |

---

## 🏗️ Estrutura do Repositório

```
📁 assistente-direitos-consumidor/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 📁 data/
│   ├── direitos_cdc.json          # Base de conhecimento: artigos e tópicos do CDC
│   └── situacoes_comuns.csv       # 12 situações mapeadas com direitos e ações
│
├── 📁 docs/
│   ├── 01-documentacao-agente.md  # Caso de uso, persona e arquitetura
│   ├── 02-base-conhecimento.md    # Estratégia de dados e fontes
│   ├── 03-prompts.md              # System prompt e exemplos de interação
│   ├── 04-metricas.md             # Avaliação e resultados dos testes
│   └── 05-pitch.md                # Roteiro do pitch de 3 minutos
│
├── 📁 src/
│   └── app.py                     # Aplicação Streamlit com integração Google Gemini
│
└── 📁 .streamlit/
    └── secrets.toml               # ⚠️ NÃO suba este arquivo! (está no .gitignore)
```

---

## 🚀 Como Rodar o Projeto Localmente

### Pré-requisitos
- Python 3.10 ou superior
- Conta no [Google AI Studio](https://aistudio.google.com) para obter a chave de API gratuita do Gemini

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/SEU_USUARIO/resolva-ja.git
cd resolva-ja
```

**2. Crie e ative um ambiente virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure a chave de API**

Crie o arquivo `.streamlit/secrets.toml` com o conteúdo:
```toml
GEMINI_API_KEY = "AIza-sua-chave-aqui"
```

> ⚠️ **IMPORTANTE:** Nunca suba este arquivo para o GitHub! Ele já está no `.gitignore`.
> Chave gratuita disponível em: [aistudio.google.com](https://aistudio.google.com) → Get API Key

**5. Execute o app**
```bash
python -m streamlit run src/app.py
```

O app abrirá automaticamente em `http://localhost:8501`

---

## 🧪 Situações que o Assistente Cobre

| Situação | Legislação |
|---|---|
| Produto com defeito (loja física ou online) | Art. 18/26 CDC |
| Direito de arrependimento — compras online | Art. 49 CDC + Decreto 7.962/2013 |
| Obrigações das lojas online | Decreto 7.962/2013 |
| Produto não entregue no prazo | Art. 35 CDC |
| Cobrança indevida / cobrado duas vezes | Art. 42 CDC |
| Propaganda enganosa / preço diferente | Art. 30/37 CDC |
| Produto vencido ou impróprio | Art. 18/64 CDC |
| Serviço mal prestado (oficinas, salões) | Art. 20 CDC |
| Recusa ou discriminação no atendimento | Art. 39 CDC |
| Fraude em cartão de crédito | Lei 14.181/2021 |
| Empresa dificulta cancelamento (SAC) | Decreto 11.034/2022 |
| Dados pessoais usados sem permissão | LGPD — Lei 13.709/2018 |
| Troca sem defeito em loja física | ⚠️ Sem cobertura — declarado com honestidade |

---

## 🛡️ Princípios Anti-Alucinação

O assistente foi projetado para:
- Responder **apenas com base na legislação** e nos dados da pasta `data/`
- **Declarar claramente** quando a lei não se aplica ao caso
- **Nunca inventar** artigos, prazos ou direitos inexistentes
- **Orientar ao Procon** em casos ambíguos ou muito complexos

---

## 🏛️ Canais Oficiais de Apoio ao Consumidor

| Canal | Quando usar | Acesso |
|---|---|---|
| Consumidor.gov.br | Mediação oficial com grandes empresas | [consumidor.gov.br](https://www.consumidor.gov.br) |
| Reclame Aqui | Pressão pública e reputação da empresa | [reclameaqui.com.br](https://www.reclameaqui.com.br) |
| Procon | Processo formal após falha na negociação | [procon.sp.gov.br](https://www.procon.sp.gov.br/procon-brasil/) |
| ANPD | Proteção de dados pessoais | [gov.br/anpd](https://www.gov.br/anpd) |

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| [Python 3.10+](https://python.org) | Linguagem principal |
| [Streamlit](https://streamlit.io) | Interface do chatbot |
| [Google Gemini API](https://aistudio.google.com) | Modelo de linguagem (gratuito) |
| [google-genai](https://pypi.org/project/google-genai/) | SDK oficial do Google Gemini |
| JSON + CSV | Base de conhecimento estruturada |

---

## 📝 Aviso Legal

> Este assistente é **informativo e educacional**. Não substitui consultoria jurídica profissional.
> Para casos complexos envolvendo processos judiciais, procure um advogado ou a Defensoria Pública do seu estado.

---

## 👩‍💻 Autora

**Jackelinne Rodrigues**
Desenvolvido como projeto do Lab DIO — *"Construa Seu Assistente Virtual Com Inteligência Artificial"*

---

*Baseado no repositório de referência: [dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)*
