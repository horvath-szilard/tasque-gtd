# backend/ui.py

import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Donity – GTD UI", layout="centered")
st.title("📋 Donity – GTD Task Manager")

st.sidebar.title("Navigáció")
page = st.sidebar.radio("Válassz műveletet:", ["📁 Projektek", "🏷️ Kontextusok", "✅ Feladatok"])

def get_projects():
    return requests.get(f"{BASE_URL}/projects/").json()

def get_contexts():
    return requests.get(f"{BASE_URL}/contexts/").json()

def get_tasks():
    return requests.get(f"{BASE_URL}/tasks/").json()

if page == "📁 Projektek":
    st.header("Projektek")
    with st.form("add_project"):
        name = st.text_input("Projekt neve")
        description = st.text_input("Leírás")
        submitted = st.form_submit_button("Hozzáadás")
        if submitted:
            res = requests.post(f"{BASE_URL}/projects/", json={"name": name, "description": description})
            if res.status_code == 200:
                st.success("Projekt hozzáadva!")
            else:
                st.error(f"Hiba: {res.status_code} – {res.text}")

    st.subheader("Projektlista")
    projects = get_projects()
    for p in projects:
        st.write(f"📁 {p['name']} – {p['description']}")

elif page == "🏷️ Kontextusok":
    st.header("Kontextusok")
    with st.form("add_context"):
        name = st.text_input("Kontextus neve")
        submitted = st.form_submit_button("Hozzáadás")
        if submitted:
            res = requests.post(f"{BASE_URL}/contexts/", json={"name": name})
            if res.status_code == 200:
                st.success("Kontextus hozzáadva!")
            else:
                st.error(f"Hiba: {res.status_code} – {res.text}")

    st.subheader("Kontextuslista")
    contexts = get_contexts()
    for c in contexts:
        st.write(f"🏷️ {c['name']}")

elif page == "✅ Feladatok":
    st.header("Feladatok")
    projects = get_projects()
    contexts = get_contexts()

    with st.form("add_task"):
        title = st.text_input("Feladat címe")
        type_ = st.selectbox("Feladat típusa", ["inbox", "next_action", "waiting", "someday"])
        context_id = st.selectbox("Kontextus", ["(Nincs)"] + [f"{c['name']} (id={c['id']})" for c in contexts])
        project_id = st.selectbox("Projekt", ["(Nincs)"] + [f"{p['name']} (id={p['id']})" for p in projects])
        submitted = st.form_submit_button("Felvétel")

        if submitted:
            payload = {"title": title, "type": type_}
            if context_id != "(Nincs)":
                payload["context_id"] = int(context_id.split("id=")[1].rstrip(")"))
            if project_id != "(Nincs)":
                payload["project_id"] = int(project_id.split("id=")[1].rstrip(")"))
            res = requests.post(f"{BASE_URL}/tasks/", json=payload)
            if res.status_code == 200:
                st.success("Feladat rögzítve!")
            else:
                st.error(f"Hiba: {res.status_code} – {res.text}")

    st.subheader("Feladatlista")
    tasks = get_tasks()
    for t in tasks:
        line = f"✅ {t['title']} – `{t['type']}`"
        if t.get("project"):
            line += f" 📁 {t['project']['name']}"
        if t.get("context"):
            line += f" 🏷️ {t['context']['name']}"
        st.write(line)