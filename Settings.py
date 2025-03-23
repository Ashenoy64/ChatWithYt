import dotenv
from Utils import getEmbeddingModel, getLLM, getChatMemory

# Load environment variables from a .env file if it exists
dotenv.load_dotenv()

# Directory used to store temporary files (will be created if it doesn't exist)
TEMP_DIR = '.temp'

# Whisper model used for audio transcription.
# Note: The model will be downloaded on first use, which may take some time.
# Options: 'tiny', 'base', 'small', 'medium', 'large'
WHISPER_MODEL = 'base'

# Name of the vector database used for storing embeddings
VECTOR_DB_NAME = "vector_store"

# Configuration for splitting text into smaller chunks
DOCUMENT_SPLIT_OPTIONS = {
    'chunk_size': 500,  # Maximum size of each chunk
    'chunk_overlap': 50,  # Overlap between consecutive chunks
    'seperators': ["\n\n", "\n", ". ", " ", ""],  # Priority order of separators for splitting
}

# Set to True to make the chat interface accessible over the internet
SHARE_CHAT_INTERFACE = False

# Default models for embeddings, language model (LLM), and chat memory
# You can override these defaults by modifying the values here or in the Utils module
EMBEDDING_MODEL = getEmbeddingModel()  # Default: OllamaEmbeddings(temperature=0.7, model="nomic-embed-text")
LLM_MODEL = getLLM()  # Default: ChatOllama(temperature=0.7, model='gemma3:4b')
CHAT_MEMORY = getChatMemory()  # Default: ConversationBufferMemory(memory_key="chat_history", return_messages=True)