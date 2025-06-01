import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.title("📊 Portfolio Menu")

        # Theme-Auswahl hinzufügen
        theme = st.radio("🌗 Theme", ["Light", "Dark"], index=0)
        st.session_state["theme"] = theme

        menu = st.radio("Navigation", [
            "📁 Upload CSV",
            "📈 Portfolio Overview",
            "📉 Performance & Risk Analytics"
        ])
        return menu
