import gradio as gr

def chat( question, history, conversation_chain ):
    result = conversation_chain.invoke( { "question": question } )
    return result[ "answer" ]

def create_chat_interface( rag_chain ):
    def wrapper( question, history ):
        return chat( question, history, rag_chain )
    
    interface =  gr.ChatInterface(
        wrapper,
        title=f"ChatWithYT",
        description="Ask questions about the youtube videos",
        type="messages",
    )
    return interface


