import streamlit as st
import json
import os

vault_path = "saved_memories.json"

def save_memory(profile_name, memory_data):
    if os.path.exists(vault_path):
        with open(vault_path, "r") as f:
            data = json.load(f)
    else:
        data = {}
    if profile_name not in data:
        data[profile_name] = []
    data[profile_name].append(memory_data)
    with open(vault_path, "w") as f:
        json.dump(data, f)

def load_memories(profile_name):
    if os.path.exists(vault_path):
        with open(vault_path, "r") as f:
            data = json.load(f)
        return data.get(profile_name, [])
    return []

st.title("Memory Vault")

profile_name = st.text_input("Profile Name")
memory_title = st.text_input("Memory Title")
memory_type = st.selectbox("Memory Type", ["Advice", "Story", "Reflection", "Milestone"])
memory_content = st.text_area("Memory Content")

if st.button("Save Memory"):
    if profile_name and memory_content:
        memory = {
            "title": memory_title,
            "type": memory_type,
            "content": memory_content
}
        save_memory(profile_name, memory)
        st.success(f"Memory saved for '{profile_name}'.")
    else:
        st.error("Please enter profile name and memory content.")

if st.button("Load Memories"):
    if profile_name:
        memories = load_memories(profile_name)
        if memories:
            st.subheader(f"Memories for {profile_name}")
            for m in memories:
                st.markdown(f" *{m['title']}* ({m['type']})")
                st.write(m["content"])
                st.markdown("---")
        else:
            st.warning(f"No memories found for '{profile_name}'.")
    else:
        st.error("Please enter profile name to load memories.")
