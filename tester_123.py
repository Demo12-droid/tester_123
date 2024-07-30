import streamlit as st
import requests
import json
from streamlit_float import *
import time 

float_init(theme=True, include_unstable_primary=False)

def get_response(user_input,show_plot,toggle_option):
       return "RESPONSE", "RESPONSE", "RESPONSE", None, time_taken
    
def display_plot(plot_base64):
    st.write(plot_base64)

users_db = {
    "user1": {"password": "pass1", "session_ids": ["session1", "session2"]},
    "user2": {"password": "pass2", "session_ids": []},
}

def authenticate(username, password):
	user = users_db.get(username)
	if user and user["password"] == password:
		return True
	return False

# Function to retrieve session IDs
def get_session_ids(username):
	return users_db.get(username, {}).get("session_ids", [])

# Function to generate a new session ID
def generate_new_session_id(username):
	new_session_id = str(uuid.uuid4())
	user = users_db.get(username)
	user["session_ids"].append(new_session_id)
	return new_session_id

def logout():
	st.session_state.logged_in = False
	st.session_state.selected_option = None

if 'logged_in' not in st.session_state:
	st.session_state.logged_in = False
if 'username' not in st.session_state:
	st.session_state.username = ""
if 'show_message' not in st.session_state:
	st.session_state.show_message = True

# UI for login
if not st.session_state.logged_in:
	st.title("Login")
	username = st.text_input("Username")
	password = st.text_input("Password", type="password")
	if st.button("Login"):	
		if authenticate(username, password):
			if st.session_state.show_message == True:
				st.session_state.logged_in = True
				st.session_state.username = username
				st.session_state.show_message = False  # Ensure the message is hidden after login
				st.rerun()
		else:
			st.error("Invalid username or password")


if st.session_state.logged_in:
	st.title("Chanakya")
	
	# Sidebar
	st.sidebar.title("Options")
	
	# Retrieve previous session IDs
	session_ids = get_session_ids(st.session_state.username)
    
	if session_ids:
		st.sidebar.header("Select Session")
		array = ["Create New Session"] + session_ids
		session_option = st.sidebar.radio("Choose an option", array)
		
		if session_option == "Create New Session":
			if st.sidebar.button("Generate New Session ID"):
				new_session_id = generate_new_session_id(st.session_state.username)
				st.session_state.session_id = new_session_id
				st.write(f"New Session ID: {new_session_id}")
		else:
			if session_option in session_ids:
				st.session_state.session_id = session_option
				st.write(f"Selected Session ID: {session_option}")
	else:
		if st.session_state.show_message:
			st.write("No previous sessions found. Creating a new session...")
			new_session_id = generate_new_session_id(st.session_state.username)
			st.session_state.session_id = new_session_id
			st.write(f"New Session ID: {new_session_id}")
			# Hide the message after displaying
			st.session_state.show_message = False
			
	st.sidebar.header("Database options")
	toggle_option = st.sidebar.selectbox('Choose a Database:', ['congestion', 'toll_plaza_data'])
	
	st.sidebar.header("Display Options")
	show_plot = st.sidebar.checkbox("Plot", value=True)
	
	if st.sidebar.button("Logout"):
		logout()
    
	user_input = st.chat_input("Ask a question...")
	
	if 'messages' not in st.session_state:
	    st.session_state.messages = []
	
	if user_input:
	    st.session_state.messages.append({"role": "user", "content": user_input})
	    sql, df, text_summary, plot, time_taken = get_response(user_input,show_plot,toggle_option)
	
	    # df = df.to_dict(orient='records') if isinstance(df, pd.DataFrame) else df
	    st.session_state.messages.append({
		"role": "assistant",
		"content": {
		    "user_input": user_input,
		    "sql": sql,
		    "df": df,
		    "text_summary": text_summary,
		    "plot": plot,
		    "time_taken": time_taken 
		}
	    })
	
	for entry in st.session_state.messages:
		role = entry.get('role', 'unknown role')
		content = entry.get('content', {})
		
		if role == 'user':
			with st.chat_message("User"):
				st.write(content)
		elif role == 'assistant':
			sql_query = content.get('sql', None)
			text_summary = content.get('text_summary', None)
			plot = content.get('plot', None)
			df = content.get('df', None) 
			time_taken = content.get('time_taken')
	
		if sql_query is not None and df is None:
			with st.chat_message("assistant"):
				st.write("No data is available for the given question.If data is available, please retry")
		else:            
			with st.chat_message("assistant"):
				if df:
					st.dataframe(df)
				if text_summary:
					st.write(text_summary)
				if plot:
					try:
						display_plot(plot)
					except:
						components.html(plot,height=390,scrolling=True)
				st.write(f"<b>Time taken: {time_taken:.4f} seconds</b>", unsafe_allow_html=True)
