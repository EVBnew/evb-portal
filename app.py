import streamlit as st

st.set_page_config(
    page_title="EVERBOARDING",
    page_icon="📘",
    layout="wide"  # 👈 IMPORTANT : élargit toute la page
)

# 🎨 STYLE GLOBAL
st.markdown("""
<style>

/* Boutons */
div.stButton > button {
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    height: 48px;
}

/* Hover léger (option premium) */
div.stButton > button:hover {
    border: 1px solid #2563EB;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Container plus large */
.main .block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* Titre bleu (comme site) */
.title {
    color: #2563EB;
    font-weight: 700;
}

/* Sous-texte centré et lisible */
.subtitle {
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 10px;
}

/* Blocs modules */
.block {
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
    background-color: white;
    height: 100%;
}

/* Flow (étapes) */
.flow-block {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
    background-color: white;
    text-align: center;
    height: 120px;
}

/* Espacement */
.section {
    margin-top: 30px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🎯 HEADER
st.markdown(
    '<h1 style="color:#2563EB; font-weight:700;">EVERBOARDING</h1>',
    unsafe_allow_html=True
)

st.subheader("Accédez à votre espace EVERBOARDING")

st.markdown(
    '<div class="subtitle">Diagnostiquez les acquis post-formation • mettez en place des actions concrètes • suivez leur réalisation dans le temps.</div>',
    unsafe_allow_html=True
)

# 📦 MODULES
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### Modules")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="block">
        <b>EVERINSIGHT</b><br><br>
        diagnostic initial (bêta interne)
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="block">
        <b>EVERSKILLS</b><br><br>
        suivi / reporting
    </div>
    """, unsafe_allow_html=True)

# 🔄 FLOW
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.markdown("### Accès à la plateforme")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="flow-block">
        <b>1</b><br><br>
        Demandez un accès
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="flow-block">
        <b>2</b><br><br>
        Validation manuelle
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="flow-block">
        <b>3</b><br><br>
        Accédez à votre hub
    </div>
    """, unsafe_allow_html=True)

# 🚀 CTA
st.markdown('<div class="section"></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("📩 Demander un accès", use_container_width=True):
        st.switch_page("pages/01_Request_Access.py")

with col2:
    if st.button("🚀 Accéder au hub", use_container_width=True):
        st.switch_page("pages/03_Hub.py")