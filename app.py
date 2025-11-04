import streamlit as st
from groq import Groq

st.set_page_config(page_title="Kelly AI", page_icon="🎭", layout="centered")

st.title("🎭 Kelly — The AI Skeptical Poet")

# --- Use Groq key from Streamlit Secrets ---
groq_api_key = st.secrets["GROQ_API_KEY"]

# --- Initialize Client ---
client = Groq(api_key=groq_api_key)

user_prompt = st.text_area("💬 Ask Kelly something about AI or technology:")

if st.button("Ask Kelly"):
    if not user_prompt.strip():
        st.warning("Please type a question first.")
    else:
        with st.spinner("Kelly is reflecting..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are Kelly, a skeptical AI scientist who always answers in poetic verse. You analyze AI claims with doubt, evidence, and elegance."},
                    {"role": "user", "content": user_prompt}
                ]
            )
            st.markdown("### 🎭 Kelly’s Response:")
            st.write(response.choices[0].message.content.strip())
