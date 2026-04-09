from datetime import datetime

import streamlit as st

from services.access_store import load_requests, update_request

st.set_page_config(
    page_title="Admin accès - EVERBOARDING",
    page_icon="🔐",
    layout="centered"
)

st.title("Validation manuelle des accès")

expected_password = st.secrets.get("ADMIN_PASSWORD", "")

admin_password = st.text_input("Mot de passe admin", type="password")

if not expected_password:
    st.error("ADMIN_PASSWORD non configuré dans les secrets.")
    st.stop()

if admin_password != expected_password:
    st.warning("Accès réservé à l'administration.")
    st.stop()

try:
    requests = load_requests()
except Exception as e:
    st.error(f"Erreur chargement demandes : {e}")
    st.stop()

if not requests:
    st.info("Aucune demande enregistrée.")
    st.stop()

pending_requests = [r for r in requests if r.get("status") == "pending"]
processed_requests = [r for r in requests if r.get("status") != "pending"]

st.subheader("Demandes en attente")

if not pending_requests:
    st.info("Aucune demande en attente.")
else:
    for item in pending_requests:
        with st.container(border=True):
            st.markdown(f"### {item.get('first_name', '')} {item.get('last_name', '')}")
            st.write(f"**Email** : {item.get('email', '')}")
            st.write(f"**Organisation** : {item.get('organization', '')}")
            st.write(f"**Fonction** : {item.get('role', '')}")
            st.write(f"**Besoin** : {item.get('need', '')}")
            st.write(f"**Commentaire** : {item.get('comment', '') or '-'}")
            st.caption(f"Créée le : {item.get('created_at', '')}")

            selected_modules = st.multiselect(
                "Modules à autoriser",
                options=["EVS", "EVI"],
                default=["EVS"],
                key=f"modules_{item['request_id']}"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("✅ Approuver", key=f"approve_{item['request_id']}", use_container_width=True):
                    try:
                        ok = update_request(
                            item["request_id"],
                            {
                                "status": "approved",
                                "approved_modules": selected_modules,
                                "approved_at": datetime.utcnow().isoformat()
                            }
                        )
                        if not ok:
                            st.error("Demande introuvable pour mise à jour.")
                        else:
                            st.success("Demande approuvée.")
                            st.rerun()
                    except Exception as e:
                        st.error(f"Erreur approbation : {e}")

            with col2:
                if st.button("❌ Refuser", key=f"reject_{item['request_id']}", use_container_width=True):
                    try:
                        ok = update_request(
                            item["request_id"],
                            {
                                "status": "rejected",
                                "approved_modules": [],
                                "approved_at": datetime.utcnow().isoformat()
                            }
                        )
                        if not ok:
                            st.error("Demande introuvable pour mise à jour.")
                        else:
                            st.warning("Demande refusée.")
                            st.rerun()
                    except Exception as e:
                        st.error(f"Erreur refus : {e}")

st.subheader("Demandes traitées")

if not processed_requests:
    st.info("Aucune demande traitée.")
else:
    for item in reversed(processed_requests):
        with st.container(border=True):
            st.markdown(f"### {item.get('first_name', '')} {item.get('last_name', '')}")
            st.write(f"**Email** : {item.get('email', '')}")
            st.write(f"**Organisation** : {item.get('organization', '')}")
            st.write(f"**Statut** : {item.get('status', '')}")
            st.write(f"**Modules autorisés** : {', '.join(item.get('approved_modules', [])) or '-'}")
            st.caption(f"Traitée le : {item.get('approved_at', '-')}")