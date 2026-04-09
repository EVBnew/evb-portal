import streamlit as st


def get_evs_url() -> str:
    return st.secrets.get("EVS_URL", "https://everskill.streamlit.app")


def is_evi_enabled() -> bool:
    return bool(st.secrets.get("EVI_ENABLED", False))


def get_evi_url() -> str:
    return st.secrets.get("EVI_URL", "")