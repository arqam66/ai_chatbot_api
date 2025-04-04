import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# ✅ Load .env file
load_dotenv()

# ✅ Get API key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# ✅ API Key Validation
if not api_key:
    st.error("⚠️ API key is missing! Please set GOOGLE_API_KEY in environment variables.")
    st.stop()

# ✅ Google Gemini AI Configuration
genai.configure(api_key=api_key)

# ✅ Streamlit UI Setup
st.set_page_config(page_title="Gemini AI Chatbot", layout="centered")

# ✅ Display Chatbot Header
st.title(" Arqam AI Chatbot")
st.write("Ask anything To Chatbot")

# ✅ User Profile Info
st.sidebar.header("👨‍💻 About ME")

st.sidebar.info(
    """
👨‍💻 **Arqam Hussain** — Creative Full-Stack Developer  

🚀 **Tech Stack:** React.js | Next.js | TypeScript | Tailwind CSS | Custom CSS | Sanity | Node.js  

🎨 **Focus Areas:** Sleek UI/UX Design | Scalable Web Apps | E-Commerce Solutions  

🤖 **Currently Exploring:** Full-Stack E-Commerce Platforms & AI-Powered Chatbots  

"""
)

# ✅ Maintain Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ Chat Input Box
user_input = st.chat_input("Ask something...")
if user_input:
    # ✅ Show User Message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # ✅ AI Response with Typing Indicator
    with st.spinner("🤖 Typing..."):
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(user_input)
        bot_reply = response.text

    # ✅ Show AI Response
    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
