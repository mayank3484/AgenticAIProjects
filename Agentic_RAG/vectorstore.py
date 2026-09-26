from langchain_chroma import Chroma
from config import EMBEDDING_MODEL,CHROMA_DB,CHROMA_COLLECTION
from langchain_ollama import OllamaEmbeddings

embedding_model=OllamaEmbeddings(model=EMBEDDING_MODEL)

def vector_store():
    vs=Chroma(
        persist_directory=CHROMA_DB,
        collection_name=CHROMA_COLLECTION,
        embedding_function=embedding_model
    )
    return vs