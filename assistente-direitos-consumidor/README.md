# ⚖️ PROCON Digital – Assistente de Direitos do Consumidor

> Projeto desenvolvido para o Lab **"Construa Seu Assistente Virtual Com Inteligência Artificial"** da [DIO](https://dio.me)  
> Baseado no repositório: [digitalinnovationone/dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)

---

## 📋 Sobre o Projeto

O **PROCON Digital** é um assistente virtual que ajuda pessoas de baixa e média renda a entender seus direitos como consumidores, com linguagem simples e orientação prática baseada no **CDC (Lei nº 8.078/1990)**.

**Serve para dois públicos:**
- **Consumidores:** Saiba exatamente o que exigir e como agir
- **Lojistas/Funcionários:** Entenda como agir corretamente e evite reclamações no Procon

---

## 🎯 O Que o Assistente Faz

Para cada situação descrita, responde em **6 etapas estruturadas**:

| Etapa | Conteúdo |
|---|---|
| 🎯 O que está acontecendo | Identifica o problema com clareza |
| ⚖️ O que a lei diz | Explica o artigo do CDC com analogia simples |
| ✅ Seu direito | Lista o que você pode exigir |
| 💬 Como exigir | Script exato do que falar ou escrever |
| 🤝 Como a loja pode reagir | Formas legais de negociação do comércio |
| ⚠️ Se não resolver | Procon, Reclame Aqui, consumidor.gov.br, JEC |

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
│   ├── direitos_cdc.json          # Artigos do CDC estruturados e simplificados
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
│   └── app.py                     # Aplicação Streamlit com integração Anthropic
│
└── 📁 .streamlit/
    └── secrets.toml               # ⚠️ NÃO suba este arquivo! (está no .gitignore)
```

---

## 🚀 Como Rodar o Projeto Localmente

### Pré-requisitos
- Python 3.10 ou superior
- Conta na [Anthropic Console](https://console.anthropic.com) para obter a API Key

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/SEU_USUARIO/assistente-direitos-consumidor.git
cd assistente-direitos-consumidor
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
ANTHROPIC_API_KEY = "sk-ant-sua-chave-aqui"
```

> ⚠️ **IMPORTANTE:** Nunca suba este arquivo para o GitHub! Ele já está no `.gitignore`.

**5. Execute o app**
```bash
streamlit run src/app.py
```

O app abrirá automaticamente em `http://localhost:8501`

---

## 🔧 Como Usar no VS Code

1. Abra a pasta do projeto no VS Code: `File → Open Folder`
2. Instale a extensão **Python** (Microsoft)
3. Selecione o interpretador do ambiente virtual: `Ctrl+Shift+P → Python: Select Interpreter`
4. Abra o terminal integrado: `Ctrl+` ` `
5. Execute: `streamlit run src/app.py`

---

## 🧪 Situações que o Assistente Cobre

| Situação | Artigo CDC |
|---|---|
| Produto com defeito (loja física ou online) | Art. 18/26 |
| Direito de arrependimento (compras online) | Art. 49 |
| Produto não entregue no prazo | Art. 35 |
| Cobrança indevida / cobrado duas vezes | Art. 42 |
| Propaganda enganosa / preço diferente | Art. 30/37 |
| Produto vencido | Art. 18/64 |
| Serviço mal prestado (oficinas, salões) | Art. 20 |
| Discriminação ou recusa de atendimento | Art. 39 |
| Troca sem defeito em loja física | ⚠️ Sem cobertura legal — declarado com honestidade |

---

## 🛡️ Anti-Alucinação

O assistente é projetado para:
- Responder **apenas com base no CDC** e nos dados da pasta `data/`
- **Declarar claramente** quando a lei não se aplica
- **Nunca inventar** artigos, prazos ou direitos inexistentes
- **Orientar ao Procon** em casos ambíguos ou complexos

---

## 🏛️ Canais de Defesa do Consumidor

| Canal | Quando usar | Link |
|---|---|---|
| Procon | Após falha na negociação direta | Pesquise "Procon + seu estado" |
| Reclame Aqui | Pressão pública sobre a empresa | reclameaqui.com.br |
| Consumidor.gov.br | Mediação oficial com grandes empresas | consumidor.gov.br |
| JEC | Causas até 20 salários mín. sem advogado | TJ do seu estado |

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| [Streamlit](https://streamlit.io) | Interface do chatbot |
| [Anthropic API](https://docs.anthropic.com) | Modelo de linguagem (Claude) |
| Python 3.10+ | Linguagem principal |
| JSON + CSV | Base de conhecimento |

---

## 📝 Aviso Legal

> Este assistente é **informativo e educacional**. Não substitui consultoria jurídica profissional. Para casos complexos envolvendo processos judiciais, procure um advogado ou a Defensoria Pública.

---

## 👤 Autor

Desenvolvido como projeto do Lab DIO — "Construa Seu Assistente Virtual Com Inteligência Artificial"

---

*Baseado no repositório de referência: [dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)*
