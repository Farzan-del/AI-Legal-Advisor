# App/agent4_rag.py
from App.llm_config import get_gemini_llm
from App.vector_store import get_vector_store
from langchain.chains import RetrievalQA

def answer_question_with_rag(query: str) -> str:
    retriever = get_vector_store().as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=get_gemini_llm(),
        retriever=retriever,
        return_source_documents=False
    )
    result = qa_chain.run(query)
    return result
