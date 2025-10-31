# app.py
import streamlit as st
from agriculture_bot import AgricultureAIAssistant

# Page configuration
st.set_page_config(
    page_title="Agriculture AI Assistant",
    page_icon="🌾",
    layout="wide"
)

# Initialize chatbot
@st.cache_resource
def load_chatbot():
    return AgricultureAIAssistant()

chatbot = load_chatbot()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "🌾 Hello! I'm your FREE Agriculture AI Assistant. I can help with:\n• Crop information & growing tips\n• Pest & disease management\n• Fertilizer recommendations\n• Organic farming methods\n\nWhat would you like to know about farming?"}
    ]

# UI Layout
st.title("🌾 Agriculture AI Assistant")


# Sidebar with quick info
with st.sidebar:
    st.header("🌱 Quick Access")
    st.write("**Ask me about:**")
    st.write("• Crop growing conditions")
    st.write("• Pest & disease control")
    st.write("• Fertilizer recommendations")
    st.write("• Organic farming methods")
    st.write("• Water management")
    
    st.header("🚜 Available Crops")
    available_crops = chatbot.database.get_all_crops()
    if available_crops:
        for crop in available_crops:
            if st.button(f"🌱 {crop}"):
                st.session_state.messages.append({"role": "user", "content": f"Tell me about {crop} farming"})
                response = chatbot.get_response(f"Tell me about {crop} farming")
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()

# Main chat area
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask about agriculture..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("🌱 Researching..."):
            response = chatbot.get_response(prompt)
            st.write(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Chat cleared! How can I help with agriculture today?"}
    ]
    chatbot.clear_history()
    st.rerun()