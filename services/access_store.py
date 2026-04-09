import requests
import streamlit as st


def _get_webapp_url() -> str:
    url = st.secrets.get("ACCESS_WEBAPP_URL", "").strip()
    if not url:
        raise RuntimeError("ACCESS_WEBAPP_URL manquant dans les secrets.")
    return url


def load_requests() -> list:
    url = _get_webapp_url()
    response = requests.get(url, timeout=20)
    response.raise_for_status()

    data = response.json()
    if not isinstance(data, list):
        raise RuntimeError("Réponse inattendue de l'Apps Script.")
    return data


def add_request(item: dict) -> None:
    url = _get_webapp_url()
    response = requests.post(url, json=item, timeout=20)
    response.raise_for_status()

    data = response.json()
    if not data.get("ok"):
        raise RuntimeError(data.get("error", "Échec lors de l'enregistrement de la demande."))


def update_request(request_id: str, updates: dict) -> bool:
    url = _get_webapp_url()

    payload = {
        "action": "update_request",
        "request_id": request_id,
        "updates": updates,
    }

    response = requests.post(url, json=payload, timeout=20)
    response.raise_for_status()

    data = response.json()
    if not data.get("ok"):
        raise RuntimeError(data.get("error", "Échec lors de la mise à jour de la demande."))

    return True


def find_request_by_email(email: str) -> dict | None:
    normalized_email = email.strip().lower()
    items = load_requests()

    matches = [
        item for item in items
        if str(item.get("email", "")).strip().lower() == normalized_email
    ]

def find_existing_request(email: str) -> dict | None:
    normalized_email = email.strip().lower()
    items = load_requests()

    matches = [
        item for item in items
        if str(item.get("email", "")).strip().lower() == normalized_email
    ]

    if not matches:
        return None

    return matches[-1]