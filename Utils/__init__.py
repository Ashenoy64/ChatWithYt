import os
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.memory import ConversationBufferMemory
import shutil

def getEmbeddingModel():
    return OllamaEmbeddings( temperature=0.7, model="nomic-embed-text" )

def getLLM():
    return ChatOllama( temperature=0.7, model='gemma3:4b' )

def getChatMemory():
    return ConversationBufferMemory( memory_key="chat_history", return_messages=True )

class Config:
    def __init__( self, **kwargs ):
        self.temp_dir = kwargs.get( 'temp_dir', '.temp' )
        self.whisper_model = kwargs.get( 'whisper_model', 'base' )
        self.embedding_model = kwargs.get( 'embedding_model', getEmbeddingModel() )
        self.vector_db_name = kwargs.get( 'vector_db_name', 'vector_store' )
        self.document_split_options = kwargs.get( 'document_split_options', {
            'chunk_size': 500,
            'chunck_overlap': 50,
            'seperators': ["\n\n", "\n", ". ", " ", ""]
        } )
        self.llm_model = kwargs.get( 'llm_model', getLLM() )
        self.chat_memory = kwargs.get( 'chat_memory', getChatMemory() )
        self.share_chat_interface = kwargs.get( 'share_chat_interface', False )
        self.init()

    def init( self ):
        os.makedirs( self.temp_dir, exist_ok=True )
        return self

    def close( self ):
        if os.path.exists( self.temp_dir ):
            shutil.rmtree( self.temp_dir )
        return None

