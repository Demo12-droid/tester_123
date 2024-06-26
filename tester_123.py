import streamlit as st
from streamlit_chat import message

def api_calling(prompt):
	
	message = "R E S P O N S E"
	return message

st.title("ChatGPT ChatBot With Streamlit and OpenAI")
if 'user_input' not in st.session_state:
	st.session_state['user_input'] = []

if 'response' not in st.session_state:
	st.session_state['response'] = []

def get_text():
	input_text = st.text_input("write here", key="input")
	return input_text

user_input = get_text()

if user_input:
	output = api_calling(user_input)
	output = output.lstrip("\n")

	# Store the output
	st.session_state.response.append(user_input)
	st.session_state.user_input.append(output)

message_history = st.empty()

if st.session_state['user_input']:
	for i in range(0 , len(st.session_state['user_input']) - 1, 1):
		# This function displays OpenAI response
		message(st.session_state['response'][i], 
				avatar_style="miniavs",is_user=True,
				key=str(i) + 'data_by_user')
		# This function displays user input
		message(st.session_state["user_input"][i], 
				key=str(i),avatar_style="icons")
