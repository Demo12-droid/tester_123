import streamlit as st
from streamlit_chat import message

# Mock API function for demo
def api_calling(prompt):
    message = "R E S P O N S E"
    return message

# Streamlit app title
st.title("ChatGPT ChatBot With Streamlit and OpenAI")

# Initialize session state if not already done
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []

if 'response' not in st.session_state:
    st.session_state['response'] = []

# Function to get user input
def get_text():
    input_text = st.text_input("Write here", key="input")
    return input_text

# Get user input
user_input = get_text()

# Process user input and display output
if user_input:
    output = api_calling(user_input)
    output = output.lstrip("\n")

    # Store user input and response in session state
    st.session_state.response.append(user_input)
    st.session_state.user_input.append(output)

# Display message history
message_history = st.empty()

# Display chat history in reverse order
if st.session_state['user_input']:
    for i in reversed(range(len(st.session_state['user_input']))):
        # Display OpenAI response
        message(st.session_state['response'][i], 
                avatar_style="miniavs", is_user=True,
                key=f"{i}_data_by_user")
        # Display user input
        message(st.session_state["user_input"][i], 
                key=str(i), avatar_style="icons")

# Custom CSS to stick input box to bottom of page
st.markdown(
    """
    <style>
    .sticky-input {
        position: fixed;
        bottom: 0;
        width: 100%;
        padding: 10px;
        background-color: #f0f0f0; /* Adjust background color as needed */
        border-top: 1px solid #ccc; /* Optional: Add border to separate input box */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display input box with sticky style using HTML
st.markdown('<input class="sticky-input" placeholder="Write here" id="input">', unsafe_allow_html=True)
