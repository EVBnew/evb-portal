import streamlit as st


def get_user_email() -> str | None:
    return st.session_state.get("user_email")


def set_user_email(email: str) -> None:
    st.session_state["user_email"] = email


def clear_user_email() -> None:
    if "user_email" in st.session_state:
        del st.session_state["user_email"]