import streamlit as st


def show_places_page():
    styles = """<style>
        .places-card {
            width: 290px;
            border: 1px solid #e2e8f0;
            border-radius: 18px;
            

    </style>
    """

    html = """
    <article class="places-card">
         <img class="places-image" src="" alt="London image" />
        
          <div class="place-content">
            <p class="country">United Kingdom</p>
            <h2>London</h2>
            <p class="description">A historic city with famous landmarks, museums, and beautiful parks</p>
            <span>Already visited</span>
          </div>
    </article>
    """

    st.html(styles + html)