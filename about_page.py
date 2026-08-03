import streamlit as st

EMAIL = ""
GITHUB_URL = "https://github.com/irina-tenyanko/my-first-repository"
 

def show_about_page():
    st.image(
        "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80",
        width=180,
    )
    st.title("Irina")

    st.subheader("Мої проєкти")

    with st.container(border=True):
        st.subheader("Список контактів")
        st.write(
            "Застосунок для збереження контактів. Користувач може додавати, видаляти, шукати і фільтрувати контакти."
        )
        st.write("Технології: Python, Streamlit, JSON, pandas")
    with st.container(border=True):
        st.subheader("Мої улюблені місця")
        st.write(
            "Застосунок для перегляду добірки пам'ятних місць і цікавих локацій. Зберігає спогади про подорожі і "
            "допомагає планувати майбутні пригоди."
        )
        st.write("Технології: Python, Streamlit, HTML, CSS")

    st.subheader("Мої контакти")
    with st.container(border=True):
        st.write(f"Email: {EMAIL}")
        st.write(f"Github: {GITHUB_URL}")
