import streamlit as st

from services.access_store import find_request_by_email
from services.session import get_user_email, set_user_email, clear_user_email
from services.urls import get_evs_url, get_evi_url, is_evi_enabled

st.set_page_config(
    page_title="Hub - EVERBOARDING",
    page_icon="🚀",
    layout="centered"
)

EVS_URL = get_evs_url()
EVI_URL = get_evi_url()
EVI_ENABLED = is_evi_enabled()

st.title("Hub EVERBOARDING")
st.write("Saisissez votre email professionnel pour accéder à vos modules.")

current_email = get_user_email()

with st.form("hub_access_form"):
    email = st.text_input("Email professionnel", value=current_email or "")
    submitted = st.form_submit_button("Accéder au hub", use_container_width=True)

if submitted:
    if not email.strip():
        st.error("Merci de renseigner votre email professionnel.")
        st.stop()

    set_user_email(email.strip().lower())
    st.rerun()

current_email = get_user_email()

if not current_email:
    st.info("Aucun email renseigné pour le moment.")
    st.stop()

st.divider()

col_a, col_b = st.columns([4, 1])
with col_a:
    st.caption(f"Email connecté : {current_email}")
with col_b:
    if st.button("Déconnexion", use_container_width=True):
        clear_user_email()
        st.rerun()

request_item = find_request_by_email(current_email)

if not request_item:
    st.warning("Aucune demande d'accès trouvée pour cet email.")
    st.info("Merci d'utiliser le formulaire de demande d'accès.")
    st.stop()

status = request_item.get("status", "pending")
approved_modules = request_item.get("approved_modules", [])

if status == "pending":
    st.warning("Votre demande est en attente de validation manuelle.")
    st.stop()

if status == "rejected":
    st.error("Votre demande d'accès a été refusée.")
    st.stop()

st.success("Votre accès EVERBOARDING est actif.")

st.markdown("### Vos modules")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### EVERINSIGHT")
    st.write("Diagnostic initial")

    if "EVI" in approved_modules and EVI_ENABLED and EVI_URL:
        st.caption("Accès accordé")
        st.link_button("Ouvrir EVERINSIGHT", EVI_URL, use_container_width=True)
    elif "EVI" in approved_modules:
        st.caption("Accès accordé - ouverture publique à venir")
        st.button("Bêta interne", disabled=True, use_container_width=True)
    else:
        st.caption("Non activé pour le moment")
        st.button("Non activé", disabled=True, use_container_width=True)

with col2:
    st.markdown("### EVERSKILLS")
    st.write("Suivi / reporting")

    if "EVS" in approved_modules:
        st.caption("Accès accordé")
        st.link_button("Ouvrir EVERSKILLS", EVS_URL, use_container_width=True)
    else:
        st.caption("Non activé pour le moment")
        st.button("Non activé", disabled=True, use_container_width=True)