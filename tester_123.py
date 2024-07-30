import streamlit as st
import requests
import json
import base64
from io import BytesIO
from PIL import Image
# from chatbot_backend.chat.main import run_code
import pandas as pd
import time
from streamlit_folium import folium_static
from streamlit_float import *

float_init(theme=True, include_unstable_primary=False)

def get_response(user_input,show_plot,toggle_option):
       return "RESPONSE", "RESPONSE", "RESPONSE", None, time_taken
    
def display_plot(plot_base64):
    st.write(plot_base64)

# Streamlit app
st.title("Chanakya")

user_input = st.chat_input("Ask a question...")

st.sidebar.title("Options")

st.sidebar.header("Database options")
toggle_option = st.sidebar.selectbox(
    'Choose a Database:',
    ['congestion', 'toll_plaza_data']
)

st.sidebar.header("Display Options")
show_plot = st.sidebar.checkbox("Plot",value=True)




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
