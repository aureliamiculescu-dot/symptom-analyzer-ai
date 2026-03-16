import streamlit as st
from openai import OpenAI
from rag_faiss import *
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.title("🩺 Analisador Inteligente de Sintomas")

st.write("Introduza os seus sintomas para obter informação de saúde.")

sintomas = st.text_area("Descreva os seus sintomas")

if st.button("Analisar sintomas"):

    textos = carregar_documentos()

    embeddings = criar_embeddings(textos)

    index = criar_indice(embeddings)

    contexto = pesquisar_contexto(sintomas, textos, index)

    prompt = f"""
    És um assistente de informação médica.

    Usa apenas a informação abaixo.

    Informação médica:
    {contexto}

    Sintomas:
    {sintomas}

    Responde em português de Portugal e inclui:

    1. Possíveis condições
    2. Recomendações gerais
    3. Nível de urgência (Baixo / Moderado / Alto)
    4. Quando procurar um médico

    Não faças diagnóstico médico.
    """

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(resposta.choices[0].message.content)