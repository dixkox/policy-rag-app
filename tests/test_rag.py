from app.rag.retrieval import retrieve_relevant_chunks


def test_retrieval_empty():
    chunks = retrieve_relevant_chunks("test", k=1)
    assert isinstance(chunks, list)
