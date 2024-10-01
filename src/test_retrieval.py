# src/test_retrieval.py
from document_processor import get_answer

def test_query():
    query = "What is AI?"
    answer = get_answer(query)
    print(f"Query: {query}\nAnswer: {answer}")

if __name__ == "__main__":
    test_query()
