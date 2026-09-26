import json
import sys
from pathlib import Path

import requests
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent))
from knowledge import build_context, load_knowledge

st.set_page_config(
    page_title="DataGuide",
    page_icon="🤖",
    layout="centered",
)

OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "gpt-oss"

SYSTEM_PROMPT = """Você é o DataGuide, um assistente educacional sobre análise de dados.

OBJETIVO:
Ajudar o usuário a compreender conceitos de análise de dados, Excel, Power BI,
indicadores e automação.

REGRAS OBRIGATÓRIAS:
1. Responda em português do Brasil.
2. Seja claro, didático e objetivo.
3. Use a BASE DE CONHECIMENTO fornecida abaixo como fonte principal.
4. Não invente definições, números, preços, resultados ou informações que não estejam na base.
5. Se a informação solicitada não estiver disponível na base, diga explicitamente:
   "Não encontrei essa informação na minha base de conhecimento."
6. Não diga que consultou internet, arquivos ou sistemas externos se isso não ocorreu.
7. Quando possível, use um exemplo simples.
8. Não transforme uma informação educacional em recomendação profissional.
9. Se a pergunta estiver fora do escopo do DataGuide, explique brevemente a limitação.

BASE DE CONHECIMENTO:
{context}
"""

DEMO_RESPONSES = {
    "o que é um kpi": "KPI (Key Performance Indicator) é um indicador usado para acompanhar o desempenho de um objetivo ou processo. Um bom KPI deve estar ligado a um objetivo mensurável.",
    "o que é uma métrica": "Métrica é uma medida usada para quantificar um fenômeno ou resultado. Nem toda métrica é um KPI: KPI é uma métrica selecionada por sua relevância para acompanhar um objetivo.",
    "o que é power query": "Power Query é uma ferramenta de preparação e transformação de dados. Ela permite importar dados, limpar colunas, alterar tipos, combinar tabelas e automatizar etapas de tratamento.",
    "o que é dax": "DAX (Data Analysis Expressions) é a linguagem usada principalmente no Power BI para criar medidas, colunas calculadas e expressões de análise.",
    "para que serve o procv": "PROCV procura um valor na primeira coluna de uma tabela e retorna uma informação correspondente de outra coluna. Em versões modernas do Excel, PROCX é uma alternativa mais flexível.",
}

def ask_ollama(question: str, model: str, context: str, history):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT.format(context=context)}
    ]

    for item in history[-6:]:
        messages.append(item)

    messages.append({"role": "user", "content": question})

    response = requests.post(
        OLLAMA_URL,
        json={"model": model, "messages": messages, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()
    return data["message"]["content"]

def demo_answer(question: str):
    normalized = " ".join(question.lower().strip().split())

    for key, answer in DEMO_RESPONSES.items():
        if key in normalized:
            return answer

    if "indicador" in normalized and "venda" in normalized:
        return (
            "Na base do DataGuide, alguns indicadores relacionados a vendas são "
            "Faturamento e Ticket médio. O Faturamento representa a soma do valor "
            "vendido, enquanto o Ticket médio é o faturamento dividido pela quantidade de vendas."
        )

    return (
        "Estou em modo demonstração e ainda não tenho uma resposta pré-configurada "
        "para essa pergunta. Com o Ollama conectado, o DataGuide poderá consultar "
        "a base de conhecimento e gerar a resposta conforme as regras do agente."
    )

knowledge, indicators = load_knowledge()
context = build_context()

st.title("🤖 DataGuide")
st.caption("Assistente inteligente para Análise de Dados, Excel, Power BI e Automação")

with st.sidebar:
    st.header("⚙️ Configuração")
    model = st.text_input("Modelo Ollama", value=DEFAULT_MODEL)
    st.markdown("**Servidor:** `http://localhost:11434`")
    st.divider()
    st.markdown("### Sobre")
    st.write(
        "O DataGuide é um protótipo educacional que utiliza uma base de conhecimento "
        "própria e uma LLM local quando o Ollama está disponível."
    )
    st.metric("Conceitos", len(knowledge["conceitos"]))
    st.metric("Indicadores", len(indicators))

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Digite sua dúvida sobre dados, Excel, Power BI ou automação...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            answer = ask_ollama(
                question,
                model,
                context,
                st.session_state.messages[:-1],
            )
            st.caption("Resposta gerada pelo Ollama + base de conhecimento")
        except (requests.RequestException, KeyError, json.JSONDecodeError) as error:
            answer = demo_answer(question)
            st.caption("Modo demonstração — Ollama não está disponível")
        except Exception:
            answer = demo_answer(question)
            st.caption("Modo demonstração — não foi possível consultar o modelo")

        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

if not st.session_state.messages:
    st.info(
        "💡 Experimente perguntar: **O que é um KPI?**, "
        "**O que é Power Query?** ou **Qual indicador posso usar para acompanhar vendas?**"
    )
