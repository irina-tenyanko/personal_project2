import streamlit as st
from pathlib import Path
from .place import Place




SCRIPT_DIR = Path(__file__).resolve().parent
CSS_FILE = SCRIPT_DIR / 'style.css'

PLACES = [
    Place(name="Львів",
          country="Україна",
          description=("Місто старовинної архітектури, затишних вулиць і ароматної кави."),
          image_url="",
          visited=True),
    Place(
        name="Рим",
        country=

    )
]

def load_styles():
        styles = f.read()
    return styles


def show_places_page():
    css = load_styles()
    styles = f"<style>{css}</style>"

    places_html