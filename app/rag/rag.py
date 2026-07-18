from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load vector store
db = FAISS.load_local("vectorstore", embeddings)

# Create retriever
retriever = db.as_retriever(search_kwargs={"k": 3})

# LLM
llm = OpenAI(temperature=0)

# RAG chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

def rag_answer(question: str) -> str:
    return qa.run(question)
