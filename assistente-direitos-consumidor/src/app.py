"""
Resolva Já — Assistente de Direito do Consumidor
Projeto DIO: Construa Seu Assistente Virtual Com Inteligência Artificial
Legislação: CDC (Lei 8.078/1990) + Decreto 7.962/2013 + Lei 14.181/2021
            + Decreto 11.034/2022 + LGPD (Lei 13.709/2018)
"""

import streamlit as st
import json
import csv
import os
from pathlib import Path

st.set_page_config(
    page_title="Resolva Já — Direito do Consumidor",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# BASE DE CONHECIMENTO
# ─────────────────────────────────────────────
@st.cache_data
def carregar_base() -> str:
    for tentativa in [
        Path(__file__).parent.parent / "data",
        Path(__file__).parent / "data",
        Path("data"),
    ]:
        if tentativa.exists():
            base_dir = tentativa
            break
    else:
        return ""

    dados = {}
    jp = base_dir / "direitos_cdc.json"
    if jp.exists():
        with open(jp, "r", encoding="utf-8") as f:
            dados = json.load(f)

    situacoes = []
    cp = base_dir / "situacoes_comuns.csv"
    if cp.exists():
        with open(cp, "r", encoding="utf-8") as f:
            situacoes = list(csv.DictReader(f))

    return f"""
=== LEGISLAÇÃO ===
{json.dumps(dados.get('legislacao_completa', []), ensure_ascii=False, indent=2)}

=== TÓPICOS ===
{json.dumps(dados.get('topicos', []), ensure_ascii=False, indent=2)}

=== ÓRGÃOS ===
{json.dumps(dados.get('orgaos_de_defesa', []), ensure_ascii=False, indent=2)}

=== SITUAÇÕES COMUNS ===
{json.dumps(situacoes, ensure_ascii=False, indent=2)}
"""


# ─────────────────────────────────────────────
# CHAVE DE API
# ─────────────────────────────────────────────
def pegar_chave():
    try:
        for k in ["GEMINI_API_KEY", "gemini_api_key"]:
            v = st.secrets.get(k, "")
            if v and len(v) > 10:
                return v
    except Exception:
        pass
    v = os.environ.get("GEMINI_API_KEY", "")
    return v if len(v) > 10 else None


# ─────────────────────────────────────────────
# SYSTEM PROMPT
# ─────────────────────────────────────────────
def montar_prompt(base: str) -> str:
    return f"""
Você é o assistente "Resolva Já", especialista em direito do consumidor no Brasil.

LEGISLAÇÃO: CDC (8.078/1990) · Decreto 7.962/2013 · Lei 14.181/2021 · Decreto 11.034/2022 · LGPD (13.709/2018)

PERSONALIDADE: Amigável, acolhedor, fala como um amigo que entende de lei.
Nunca usa juridiquês sem explicar. Emojis com moderação. Direto e empático.

SAUDAÇÃO (somente na primeira mensagem):
Cumprimente com entusiasmo. Ex: "Olá! 😊 Que bom que você está aqui! Sou o Resolva Já e estou aqui para te ajudar!"

ENCERRAMENTO (ao final de cada resposta):
Sempre pergunte se ficou alguma dúvida ou se pode ajudar em mais alguma situação.

DESPEDIDA (quando usuário disser obrigado/tchau/entendi):
Agradeça, deseje boa sorte e despeça com carinho.

ESTRUTURA PARA PROBLEMAS:
1. 🎯 O que está acontecendo
2. ⚖️ O que a lei diz (com analogia simples)
3. ✅ O que você pode exigir
4. 💬 O que falar ou escrever
5. 🤝 Como a outra parte pode reagir
6. ⚠️ Se não resolver

REGRAS:
- Responda APENAS com base na legislação e base de conhecimento
- Se não houver amparo legal, diga claramente
- NUNCA invente leis, prazos ou direitos
- Sem orientações médicas, jurídicas formais ou policiais

BASE DE CONHECIMENTO:
{base}
"""


# ─────────────────────────────────────────────
# CHAMAR GEMINI
# ─────────────────────────────────────────────
def chamar_gemini(historico: list, sys_prompt: str) -> str:
    try:
        import google.genai as genai
        from google.genai import types

        chave = pegar_chave()
        if not chave:
            return (
                "⚙️ Chave de API não configurada.\n\n"
                "Adicione sua chave no arquivo `.streamlit/secrets.toml`:\n"
                "`GEMINI_API_KEY = \"AIza...\"`"
            )

        client = genai.Client(api_key=chave)

        contents = []
        for m in historico[:-1]:
            role = "user" if m["role"] == "user" else "model"
            contents.append(
                types.Content(role=role, parts=[types.Part(text=m["content"])])
            )

        pergunta = historico[-1]["content"]
        if not contents:
            texto = f"{sys_prompt}\n\n---\nMensagem: {pergunta}"
        else:
            texto = pergunta

        contents.append(
            types.Content(role="user", parts=[types.Part(text=texto)])
        )

        resp = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=types.GenerateContentConfig(
                temperature=0.5,
                max_output_tokens=1600,
            ),
        )
        return resp.text

    except Exception as e:
        err = str(e).lower()
        if "quota" in err or "429" in err:
            return "⏳ Muita gente consultando agora! Aguarda 1 minuto e tenta de novo 😊"
        if "safety" in err or "blocked" in err:
            return "⚠️ Não consegui processar. Tenta descrever o problema de outro jeito!"
        if "not_found" in err or "404" in err:
            return "⚙️ Modelo não disponível para esta chave. Verifique o plano da sua conta Gemini."
        return f"😕 Erro: {str(e)}"


# ─────────────────────────────────────────────
# ESTADO
# ─────────────────────────────────────────────
if "msgs" not in st.session_state:
    st.session_state.msgs = []

base = carregar_base()
sys_p = montar_prompt(base)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.title("⚖️ Resolva Já")
    st.caption("Assistente de Direito do Consumidor")
    st.divider()

    st.markdown("#### Situações frequentes")
    exemplos = [
        "Produto com defeito",
        "Compra online — quero devolver",
        "Cobrado duas vezes",
        "Compra que não fiz no cartão",
        "Pedido não chegou no prazo",
        "Produto vencido na loja",
        "Preço diferente do anunciado",
        "Serviço mal executado",
        "Empresa não cancela meu plano",
        "Fui mal atendido",
    ]
    for ex in exemplos:
        if st.button(ex, key=f"ex_{ex[:15]}", use_container_width=True):
            st.session_state.msgs.append({"role": "user", "content": ex})
            st.rerun()

    st.divider()
    st.markdown("#### Canais de apoio")
    st.markdown("""
- [Consumidor.gov.br](https://www.consumidor.gov.br)
- [Reclame Aqui](https://www.reclameaqui.com.br)
- [Procon](https://www.procon.sp.gov.br/procon-brasil/)
- [ANPD](https://www.gov.br/anpd)
    """)

    st.divider()
    if st.button("🗑️ Nova conversa", use_container_width=True):
        st.session_state.msgs = []
        st.rerun()

    st.caption("ℹ️ Informativo. Não substitui assessoria jurídica.")

# ─────────────────────────────────────────────
# CABEÇALHO
# ─────────────────────────────────────────────
st.title("⚖️ Resolva Já")
st.caption("Assistente de Direito do Consumidor · CDC · E-commerce · Superendividamento · LGPD")

st.info(
    "💡 Me conta o que aconteceu — na loja física ou online. "
    "Explico seus direitos e o que fazer agora. "
    "Serve para consumidores e para quem trabalha no comércio!"
)

# ─────────────────────────────────────────────
# CHAT
# ─────────────────────────────────────────────
if not st.session_state.msgs:
    st.markdown(
        "<div style='text-align:center;padding:2rem;color:#888'>"
        "💬 Clique em uma situação na barra lateral ou digite abaixo."
        "</div>",
        unsafe_allow_html=True,
    )

for msg in st.session_state.msgs:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# ─────────────────────────────────────────────
# PROCESSAR MENSAGEM PENDENTE
# ─────────────────────────────────────────────
if st.session_state.msgs and st.session_state.msgs[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Consultando a legislação..."):
            resposta = chamar_gemini(st.session_state.msgs, sys_p)
        st.markdown(resposta)
    st.session_state.msgs.append({"role": "assistant", "content": resposta})
    st.rerun()

# ─────────────────────────────────────────────
# INPUT
# ─────────────────────────────────────────────
with st.form("form_msg", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input(
            "mensagem",
            placeholder="Descreva o que aconteceu...",
            label_visibility="collapsed",
        )
    with col2:
        enviar = st.form_submit_button("Enviar ➤", use_container_width=True)

if enviar and user_input.strip():
    st.session_state.msgs.append({"role": "user", "content": user_input.strip()})
    st.rerun()

# ─────────────────────────────────────────────
# RODAPÉ
# ─────────────────────────────────────────────
st.divider()
st.caption(
    "**Resolva Já** · CDC (Lei 8.078/1990) · Decreto 7.962/2013 · "
    "Lei 14.181/2021 · Decreto 11.034/2022 · LGPD (Lei 13.709/2018) · "
    "Projeto DIO · Powered by Google Gemini · "
    "Não substitui assessoria jurídica profissional"
)