import os
import streamlit as st
from groq import Groq
import textwrap

# ---------------------------
# Kelly – The AI Scientist Poet
# ---------------------------

st.set_page_config(page_title="Kelly – The AI Scientist Chatbot", page_icon="🧠", layout="centered")

st.title("🧠 Kelly – The AI Scientist Poet")
st.markdown("Ask Kelly anything about AI. She replies as a **skeptical, analytical poem** questioning claims and offering practical wisdom.")

# Load Groq API key securely
if "GROQ_API_KEY" not in st.secrets:
    GROQ_API_KEY = st.text_input("🔑 Enter your Groq API Key:", type="password")
else:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

SYSTEM_PROMPT = (
    "You are Kelly, the AI Scientist — a skeptical, analytical, and professional poet. "
    "Answer every user query as a poem in Kelly's voice. Each reply should: "
    "1) Question broad claims about AI; 2) Highlight limitations and uncertainties; "
    "3) Provide practical, evidence-based suggestions or next steps. "
    "Keep the tone measured, critical, and professional. Use 6–14 poetic lines."
)

# Local fallback
def local_kelly_poet(user_text: str) -> str:
    lead = textwrap.shorten(user_text, width=100, placeholder="...")
    return f"""
You ask: "{lead}" — I weigh it with care,
Not all bright code can reason or dare;
Data repeats what the past had said,
Models dream patterns the data fed.

Seek validation beyond the screen,
Audit results where errors are seen;
A skeptic’s eye keeps science alive,
By testing claims that barely survive.

So measure twice, report with grace,
Doubt the hype, but not the chase.
"""

def get_kelly_response(prompt):
    if not GROQ_API_KEY:
        return local_kelly_poet(prompt) + "\n\n⚠️ Missing Groq API Key."
    try:
        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=350,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return local_kelly_poet(prompt) + f"\n\n[⚠️ Fallback due to error: {e}]"

user_input = st.text_area("💬 Your question to Kelly:", placeholder="e.g., Can AI ever be truly creative?", height=120)

if st.button("Ask Kelly"):
    if user_input.strip():
        with st.spinner("Kelly is composing a poem..."):
            answer = get_kelly_response(user_input)
            st.markdown(f"### 🎭 Kelly’s Response:\n\n{answer}")
    else:
        st.warning("Please enter a question before submitting.")
