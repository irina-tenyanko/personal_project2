import streamlit as st
from about_page import show_about_page
from contacts_app.app import show_contacts_page

st.set_page_config(
    page_title="Personal Projekt",
    layout="wide",
    initial_sidebar_state="expanded"
)

page = st.navigation({
    "": [st.Page(show_about_page, title="Про мене", default=True)],
    "Мої Проєкти": [st.Page(show_contacts_page, title="Список контактів")]
},
    position="top")  #sidebar панель збоку "top" - угорі
page.run()