import streamlit as st
import streamlit.components.v1 as components
import os

html_file = os.path.join(os.path.dirname(__file__), 'index.html')

with open(html_file, 'r', encoding = 'utf-8') as f:
    html_content = f.read()

    components.html(html_content, height = 800, scrolling=True)