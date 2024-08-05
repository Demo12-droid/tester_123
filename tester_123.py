import streamlit as st
import requests
import json
from streamlit_float import * 
import time

x="""<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;\n&lt;html&gt;\n&lt;head&gt;\n    \n    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;\n    \n        &lt;script&gt;\n            L_NO_TOUCH = false;\n            L_DISABLE_3D = false;\n        &lt;/script&gt;\n    \n    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;\n    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;\n    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;\n    &lt;script src=&quot;https://code.jquery.com/jquery-3.7.1.min.js&quot;&gt;&lt;/script&gt;\n    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;\n    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;\n    \n            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,\n                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;\n            &lt;style&gt;\n                #map_dcbc28429513f220009e4db9deb5f3b8 {\n                    position: relative;\n                    width: 100.0%;\n                    height: 100.0%;\n                    left: 0.0%;\n                    top: 0.0%;\n                }\n                .leaflet-container { font-size: 1rem; }\n            &lt;/style&gt;\n        \n    &lt;script src=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium@main/folium/templates/leaflet_heat.min.js&quot;&gt;&lt;/script&gt;\n&lt;/head&gt;\n&lt;body&gt;\n    \n    \n            &lt;div class=&quot;folium-map&quot; id=&quot;map_dcbc28429513f220009e4db9deb5f3b8&quot; &gt;&lt;/div&gt;\n        \n&lt;/body&gt;\n&lt;script&gt;\n    \n    \n            var map_dcbc28429513f220009e4db9deb5f3b8 = L.map(\n                &quot;map_dcbc28429513f220009e4db9deb5f3b8&quot;,\n                {\n                    center: [12.7833631, 78.16822086666667],\n                    crs: L.CRS.EPSG3857,\n                    zoom: 10,\n                    zoomControl: true,\n                    preferCanvas: false,\n                }\n            );\n\n            \n\n        \n    \n            var tile_layer_51e8bfa97351862474735e53fba93028 = L.tileLayer(\n                &quot;https://tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,\n                {&quot;attribution&quot;: &quot;\\u0026copy; \\u003ca href=\\&quot;https://www.openstreetmap.org/copyright\\&quot;\\u003eOpenStreetMap\\u003c/a\\u003e contributors&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 19, &quot;maxZoom&quot;: 19, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}\n            );\n        \n    \n            tile_layer_51e8bfa97351862474735e53fba93028.addTo(map_dcbc28429513f220009e4db9deb5f3b8);\n        \n    \n            var heat_map_062479f9808cc6acd63cb77074a67fe7 = L.heatLayer(\n                [[12.9715987, 77.5945627], [13.0826802, 80.2707184], [12.2958104, 76.6393815]],\n                {&quot;blur&quot;: 15, &quot;maxZoom&quot;: 18, &quot;minOpacity&quot;: 0.5, &quot;radius&quot;: 15}\n            );\n        \n    \n            heat_map_062479f9808cc6acd63cb77074a67fe7.addTo(map_dcbc28429513f220009e4db9deb5f3b8);\n        \n&lt;/script&gt;\n&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>'"""
components.html(x,height=390,scrolling=True)


float_init(theme=True, include_unstable_primary=False)

def get_response(user_input,show_plot,toggle_option):
       return "RESPONSE", "RESPONSE", "RESPONSE", None, "RESPONSE"

def get_history(username,session_id):
    url = 'http://molly-grateful-hippo.ngrok-free.app/chat/session_info/'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'username': username,
        'session_id': session_id,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
       data = response.json().get('data', {})
       return data.get('data', 'No_recent_session_history')
    else:
       return None

def save_session_id(username,session_id):
    url = 'http://molly-grateful-hippo.ngrok-free.app/chat/save_session_id/'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'username': username,
        'session_id': session_id,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    
    if response.status_code == 200:
       return "Sucessful"
    else:
       return "error saving session credentials"
	
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
    url = 'http://molly-grateful-hippo.ngrok-free.app/chat/get_session_ids/'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "username": username,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
       data = response.json().get('data', {})
       return data
    else:
       return None

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
if 'show_message_for_saved_credentials' not in st.session_state:
	st.session_state.show_message_for_saved_credentials = True
	
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
		array = session_ids + ["Create New Session"] 
		session_option = st.sidebar.radio("Pick a session:",array)
		
		if session_option == "Create New Session":
			if st.sidebar.button("Generate New Session ID"):
				
				new_session_id = generate_new_session_id(st.session_state.username)
				st.session_state.session_id = new_session_id
				st.write(f"New Session ID: {new_session_id}")
				message=save_session_id(st.session_state.username,st.session_state.session_id)
				st.write(message)
				st.session_state.show_message_for_saved_credentials = False
				st.rerun()
		else:
			if session_option in session_ids:
				st.session_state.session_id = session_option
	else:
		if st.session_state.show_message:
			st.write("No previous sessions found. Creating a new session...")
			new_session_id = generate_new_session_id(st.session_state.username)
			st.session_state.session_id = new_session_id
			st.write(f"New Session ID: {new_session_id}")
			message=save_session_id(st.session_state.username,st.session_state.session_id)
			st.write(message)
			st.session_state.show_message_for_saved_credentials = False
			st.rerun()
			# Hide the message after displaying
			st.session_state.show_message = False
			
	st.sidebar.header("Database options")
	toggle_option = st.sidebar.selectbox('Choose a Database:', ['congestion', 'toll_plaza_data'])
	
	st.sidebar.header("Display Options")
	show_plot = st.sidebar.checkbox("Plot", value=True)
	
	if st.sidebar.button("Logout"):
		logout()
		st.rerun()
    
	user_input = st.chat_input("Ask a question...")
	
	st.session_state.messages = get_history(st.session_state.username,st.session_state.session_id)
	# st.write(st.session_state.messages)
	
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
						st.write(df)
					if text_summary:
						st.write(text_summary)
					if plot:
						try:
							display_plot(plot)
						except:
							components.html(plot,height=390,scrolling=True)
					st.write(f"<b>Time taken: {time_taken} seconds</b>", unsafe_allow_html=True)
