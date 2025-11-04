import streamlit as st
from groq import Groq

# Sidebar: API key input
groq_api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

if not groq_api_key:
    st.warning("Please enter your Groq API key in the sidebar to continue.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=groq_api_key)

st.title("🎭 Kelly’s AI — Powered by Groq")

prompt = st.text_area("Ask Kelly something philosophical:")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # ✅ Updated model
            messages=[
                {"role": "system", "content": "You are Kelly, a poetic and reflective AI."},
                {"role": "user", "content": prompt}
            ]
        )
        st.markdown("### 🎭 Kelly’s Response:")
        st.write(response.choices[0].message.content)
