from .chat import create_chat_interface

def launch_chat_interface( rag_chain, config ):
    interface = create_chat_interface( rag_chain )
    interface.launch( inbrowser=True, share=config.share_chat_interface )
    return interface