from dotenv import load_dotenv
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
load_dotenv()
# prepare the configuration
LLM_MODEL = os.getenv('LLM_MODEL')
EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL')
CHROMA_DB = os.getenv('CHROMA_DB')
CHROMA_COLLECTION = os.getenv('CHROMA_COLLECTION')
KNOWLEDGE_BASE = os.getenv('KNOWLEDGE_BASE')