from config import  KNOWLEDGE_BASE
from pathlib import Path
import logging
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from vectorstore import vector_store

logger=logging.getLogger("__name__")

    

def load_documents():
    documents=[]
    knowledge_base_directory=Path(KNOWLEDGE_BASE)
    if not knowledge_base_directory.exists():
        return documents

    for file_path in knowledge_base_directory.iterdir():
        logger.info(f"reading file: {file_path}")
        loader=TextLoader(str(file_path))
        contents=loader.load()

        documents.append(contents[0])
    return documents

def split_documents(documents):
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    return splitter.split_documents(documents)

def ingest_file(file_path:str):
    logger.info(f" Started loading file {file_path}")
    loader=TextLoader(str(file_path))
    contents=loader.load()
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200

    )
    chunks=splitter.split_documents(contents)
    ids=[]
    for index, chunk in enumerate(chunks):
        chunk.metadata.update({
            "chunk_index":index,
            "type":"IT"
        })
        ids.append(f"chunk_{index}")
    vs=vector_store()
    vs.add_documents(documents=chunks,ids=ids)
    logger.info('-'*80)
    logger.info(f"ingestion completed")
    

def ingest_all_files():
    documents=load_documents()
    chunks=split_documents(documents)
    

    ids=[]
    for index,chunk in enumerate(chunks):
        chunk.metadata.update({
            "chunk_index":index,
            "type":"IT"
        })
        ids.append(f"chunk_{index}")

    vs=vector_store()

    vs.add_documents(documents=chunks,ids=ids)
    logger.info('-'*80)
    logger.info(f"ingestion completed")

if __name__ =='__main__':
    ingest_all_files()

