# src/test_chatbot.py
from chatbot import get_answer

def test_chatbot():
    query = "What is Artificial Intelligence?"
    answer = get_answer(query)
    print(f"Question: {query}\n")
    print(f"Answer: {answer}\n")

if __name__ == "__main__":
    test_chatbot()
