from openai import OpenAI

client = OpenAI(api_key="sk-None-RtRv9h2YNzoaOuZRnM1TT3BlbkFJjMWUnSJfMMki1DHg5x5t")


try:
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is AI?"}
    ])
    print(response.choices[0].message.content)
except Exception as e:
    print("Error:", e)
