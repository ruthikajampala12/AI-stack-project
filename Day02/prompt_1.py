import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"Name only types of AI in 4 lines"
        }
    ]
)
print(response["messages"]["content"])