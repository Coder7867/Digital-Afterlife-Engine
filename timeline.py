import streamlit as st
import json
import os

vault_path = "saved_memories.json"

def load_memories(name):
    if os.path.exists(vault_path):
        with open(vault_path, "r") as f:
            data = json.load(f)
        return data.get(name, [])
    return []

st.title("Legacy Timeline")

profile_name = st.text_input("Profile Name")

if st.button("Show Timeline"):
    memories = load_memories(profile_name)
    if memories:
        st.subheader(f"Timeline for {profile_name}")
        for i, m in enumerate(memories):
            st.markdown(f"### {i+1}. {m['title']} ({m['type']})")
            st.write(m["content"])
            st.markdown("---")
    else:
        st.warning(f"No memories found for '{profile_name}'.")
