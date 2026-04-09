import uuid
from datetime import datetime

import streamlit as st

from services.access_store import add_request, find_existing_request

st.set_page_config(
    page_title="Demande d'accès - EVERBOARDING",
    page_icon="📩",
    layout="centered"
)

st.title("Demande d'accès")
st.write("Remplissez ce formulaire pour demander un accès à la plateforme EVERBOARDING.")

with st.form("request_access_form"):
    first_name = st.text_input("Prénom")
    last_name = st.text_input("Nom")
    email = st.text_input("Email professionnel")
    organization = st.text_input("Organisation")
    role = st.text_input("Fonction")

    need = st.selectbox(
        "Votre besoin principal",
        [
            "Découvrir la plateforme",
            "Utiliser EVERSKILLS",
            "Préparer l'usage d'EVERINSIGHT",
            "Structurer le suivi d'une formation",
            "Autre"
        ]
    )

    comment = st.text_area(
        "Commentaire",
        placeholder="Expliquez en quelques lignes votre besoin.",
        height=120
    )

    submitted = st.form_submit_button("Envoyer la demande", use_container_width=True)

if submitted:
    missing_fields = []

    if not first_name.strip():
        missing_fields.append("Prénom")
    if not last_name.strip():
        missing_fields.append("Nom")
    if not email.strip():
        missing_fields.append("Email professionnel")
    if not organization.strip():
        missing_fields.append("Organisation")

    if missing_fields:
        st.error("Merci de renseigner les champs obligatoires : " + ", ".join(missing_fields))
    else:
        # 🔒 ANTI-DOUBLON ICI
        existing = find_existing_request(email)

        if existing:
            status = existing.get("status", "pending")

            if status == "pending":
                st.warning("Une demande est déjà en cours de validation pour cet email.")
            elif status == "approved":
                st.success("Un accès a déjà été validé pour cet email. Vous pouvez accéder au hub.")
            elif status == "rejected":
                st.warning("Une demande précédente a été refusée. Contactez l'administrateur si besoin.")

            st.stop()

        # 👉 création normale si pas de doublon
        item = {
            "request_id": str(uuid.uuid4()),
            "created_at": datetime.utcnow().isoformat(),
            "first_name": first_name.strip(),
            "last_name": last_name.strip(),
            "email": email.strip().lower(),
            "organization": organization.strip(),
            "role": role.strip(),
            "need": need,
            "comment": comment.strip(),
            "status": "pending",
            "approved_modules": []
        }

        add_request(item)

        st.success("Votre demande a bien été enregistrée. Elle sera traitée manuellement.")
        st.info("Vous pouvez revenir à l'accueil ou fermer cette page.")