from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import shutil
from langchain_chroma import Chroma

def load_documents( documents ):
    loaded_documents = []
    for file in documents:
        loader = TextLoader(file)
        loaded_documents.extend(loader.load())
    return loaded_documents


def split_documents( documents, **kwargs ):
    chunk_size = kwargs.get("chunk_size", 500)
    chunck_overlap = kwargs.get("chunck_overlap", 50)
    seperators = kwargs.get("seperators", ["\n\n", "\n", ". ", " ", ""])
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chuck_overlap=chunck_overlap,
        length_function=len,
        separators=seperators
    )

    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks


def create_vectorstore(chunks, embeddings, db_name):
    if os.path.exists(db_name):
        shutil.rmtree(db_name)
    vectorstore = Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=db_name
    )
    print(f"Vectorstore created with {vectorstore._collection.count()} documents")
    return vectorstore

def build_vectorstore(documents, embeddings, db_name, **kwargs):
    loaded_documents = load_documents(documents)
    chunks = split_documents(loaded_documents, **kwargs)
    vectorstore = create_vectorstore(chunks, embeddings, db_name)
    return vectorstore


if __name__ == "__main__":
    documents = [".temp/1.txt", ".temp/2.txt"]
    embeddings = None #OllamaEmbeddings(temperature=0.7,model="nomic-embed-text")
    db_name = "vector_store"
    build_vectorstore(documents, embeddings, db_name)