import streamlit as st
import streamlit.components.v1 as components
import os
 
 
st.set_page_config(layout="wide")
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {
            margin: 0;
            padding: 0;
        }
        .block-container {
            padding: 0;
            max-width: 100%;
        }
        [data-testid="stToolbar"] {
            display: none;
        }
        .stDeployButton {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
 
current_dir = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(current_dir, "styles.css")
js_path = os.path.join(current_dir, "script.js")
html_path = os.path.join(current_dir, "index.html")
 
 
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()
 
 
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()
 
 
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()
 
 
final_html = f"""
<style>{css_content}</style>
{html_content}
<script>{js_content}</script>
"""
 
 
 
components.html(final_html, height=700, scrolling=True)