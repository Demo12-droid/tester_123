import streamlit as st
from streamlit_float import *

# Initialize float layout
float_init(theme=True, include_unstable_primary=False)

# Mock API function for demo
def api_calling(prompt):
    return "R E S P O N S E"  # Replace with actual API call

# Function to handle chat input submission
def chat_content(content):
    user_input = content
    openai_response = api_calling(user_input)

    # Append user input and OpenAI response to session state
    st.session_state['user_input'].append(user_input)
    st.session_state['openai_response'].append(openai_response)

# Initialize session state if not already done
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []
    st.session_state['openai_response'] = []

# Layout setup using columns
col1, col2 = st.columns([1, 2, 3])

# Left column setup
with col1:
    st.title("ChatGPT ChatBot With Streamlit and OpenAI")
    st.write("Hello Streamlit!")

# Right column setup
with col2:
    with st.sidebar:
        st.title("Chat History:")
        if st.session_state['user_input']:
            for i in reversed(range(len(st.session_state['user_input']))):
                # Display user input
                st.text(f"User: {st.session_state['user_input'][i]}")
                # Display OpenAI response
                st.text(f"ChatBot: {st.session_state['openai_response'][i]}")

    # Chat input section
    st.write("Chat Input:")
    content = st.chat_input(key='content', on_submit=chat_content)

    # Floating button setup
    button_b_pos = "1rem"
    button_css = float_css_helper(width="3rem", bottom=button_b_pos, right="1rem", transition=0.2)
    float_parent(css=button_css)

