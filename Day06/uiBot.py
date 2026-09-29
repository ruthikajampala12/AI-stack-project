import ollama
import streamlit as st
st.markdown("# Welcome to my ChatBot App!!!🌻")
with st.sidebar:
    st.header(":blue[Chat Setting ⚙]")
    if st.button("Clear Chat 🗑"):
        st.session_state.messages=[]
        st.success("Chat Cleared sucessfully ✔")
    personalities={
        "Kid 🧒" : "Anser the question like you are explaning to a 5 year old kid in 2 lines only." ,
        "Friend 👧" : "Answer the questions in a friendly and casual manner.Give answers in 2 lines only. "
    }
    personality=st.selectbox("Select a personality",personalities.keys())
    uploaded_file = st.file_uploader("Upload a text file...")
    try:
        if uploaded_file:
            content = uploaded_file.read().decode("utf-8")
            st.sucess("File uploaded sucessfully 📩 ")
            if st.button("Display"):
                st.text(content)
                st.ballons()
    except: 
        
        st.error("It's not a text file 🙄")
if "messages" not in st.session_state: 
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question =st.chat_input("You:")
if question:
    st.session_state.messages.append(
        {"role": "user",
         "content":question}
    )
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("🟣Thinking..."):
        response = ollama.chat(
            model = "llama3.2:3b",
            messages= [
                {"role" : "sysytem","content" : personalities[personality]}]            
                + st.session_state.messages)
    st.session_state.messages.append(
            {"role": "assistant",
            "content":response["message"]["content"]}
        )
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])

