import os
import numpy as np
import faiss
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def carregar_documentos():

    textos = []
    pasta = "documentos_medicos"

    for ficheiro in os.listdir(pasta):
        with open(os.path.join(pasta, ficheiro), "r", encoding="utf-8") as f:
            textos.append(f.read())

    return textos


def criar_embeddings(textos):

    embeddings = []

    for t in textos:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=t
        )

        embeddings.append(response.data[0].embedding)

    return np.array(embeddings)


def criar_indice(embeddings):

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index


def pesquisar_contexto(pergunta, textos, index):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=pergunta
    )

    query = np.array([response.data[0].embedding])

    distancias, indices = index.search(query, k=2)

    contexto = ""

    for i in indices[0]:
        contexto += textos[i] + "\n"

    return contexto