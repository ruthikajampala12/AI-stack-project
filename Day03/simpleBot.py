import ollama
while True:
    question = input("Ask the question:")
    if question.lower() == "exit":
        break
    response = ollama.chat(
        model = "llama3.2:3b",
        messages=[
        {
            "role" : "system",
            "content" : "Give answer in 2 lines only."
        },
        {
            "role" : "user",
            "content" : "explain AI"
        }
    ]
)
print(response["messages"]["content"])