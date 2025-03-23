import dotenv
from Utils import getEmbeddingModel, getLLM, getChatMemory

dotenv.load_dotenv()

TEMP_DIR = '.temp'
WHISPER_MODEL = 'base'  # Choose from: tiny, base, small, medium, large



VECTOR_DB_NAME = "vector_store"

DOCUMENT_SPLIT_OPTIONS = {
    'chunk_size': 500,
    'chunk_overlap': 50,
    'seperators': ["\n\n", "\n", ". ", " ", ""], 
}

SHARE_CHAT_INTERFACE = False

# User overriding must be possible somehow
EMBEDDING_MODEL = getEmbeddingModel()  # Default: OllamaEmbeddings(temperature=0.7,model="nomic-embed-text")
LLM_MODEL = getLLM() # Default: ChatOllama(temperature=0.7, model='gemma3:4b')
CHAT_MEMORY = getChatMemory() # Default: ConversationBufferMemory(memory_key="chat_history", return_messages=True)