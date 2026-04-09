import streamlit as st

st.set_page_config(
    page_title="EVERBOARDING",
    page_icon="📘",
    layout="centered"
)

st.title("EVERBOARDING")
st.subheader("Accédez à votre espace EVERBOARDING")

st.write(
    "Diagnostiquez les acquis post-formation, mettez en place des actions concrètes et suivez leur réalisation dans le temps."
)

st.markdown("### Modules")
st.write("- **EVERINSIGHT** : diagnostic initial (bêta interne)")
st.write("- **EVERSKILLS** : suivi / reporting")

st.divider()

st.markdown("### Accès à la plateforme")
st.write("1. Demandez un accès")
st.write("2. Votre demande est validée manuellement")
st.write("3. Accédez ensuite à votre hub EVERBOARDING")

col1, col2 = st.columns(2)

with col1:
    if st.button("📩 Demander un accès", use_container_width=True):
        st.switch_page("pages/01_Request_Access.py")

with col2:
    if st.button("🚀 Accéder au hub", use_container_width=True):
        st.switch_page("pages/03_Hub.py")