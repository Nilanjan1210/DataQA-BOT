import os
import streamlit as st

from dotenv import load_dotenv


load_dotenv()

# ----------------------------
# Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Data Q&A Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ----------------------------
# UI Layout
# ----------------------------
st.title("Advanced AI Data Q&A Assistant")
st.caption("Your AI partner for exploring data, files, and ideas.")

# Input + Send
user_input = st.text_input("Your message:", key="user_input_box")

if st.button("Send", key="send_btn") and user_input:
    try:
        with st.spinner("Thinking..."):
            response = model().invoke(user_input)
            st.markdown("### Response")
            st.write(response.content)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# ----------------------------
# Sidebar Controls
# ----------------------------
with st.sidebar:
    st.header("Settings")
    
    # Handle file upload and management
    uploaded_file = handle_file_upload()
    
    if st.button("🧹 Clear Chat", key="clear_btn"):
        # Clear session state
        st.session_state.clear()
        st.success("Chat cleared.")
        st.rerun()