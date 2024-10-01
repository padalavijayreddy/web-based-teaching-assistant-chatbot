# src/web_app.py
import gradio as gr
from langchain_integration import query_documents

def chatbot_interface(user_input):
    # Use the LangChain-based function to get an answer
    return query_documents(user_input)

# Create Gradio interface
iface = gr.Interface(
    fn=chatbot_interface,
    inputs="text",
    outputs="text",
    title="AI Teaching Assistant",
    description="Ask questions about AI lecture notes!"
)

# Launch the interface
if __name__ == "__main__":
    iface.launch()
