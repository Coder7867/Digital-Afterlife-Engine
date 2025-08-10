import streamlit as st
import json
import os
import random

profile_path = "saved_profiles.json"
vault_path = "saved_memories.json"

def load_profile(name):
    if os.path.exists(profile_path):
        with open(profile_path, "r") as f:
            data = json.load(f)
        return data.get(name, None)
    return None

def load_memories(name):
    if os.path.exists(vault_path):
        with open(vault_path, "r") as f:
            data = json.load(f)
        return data.get(name, [])
    return []

def simulate_response(profile, memories, user_input):
    traits = ", ".join(profile.get("traits", []))
    tone = profile.get("tone", "Reflective")
    phrases = profile.get("phrases", [])
    lessons = profile.get("lessons", "")
    memory_snippet = random.choice(memories)["content"] if memories else ""

    response = f"{random.choice(phrases) if phrases else ''}\n\n"
    response += f"As someone who is {traits} and tends to be {tone.lower()}, here's what I'd say:\n"
    response += f"{memory_snippet}\n\n"
    response += f"Also remember: {lessons}"
    return response

st.title("Chat Simulator")

profile_name = st.text_input("Profile Name")
user_input = st.text_area("Your Message")

if st.button("Talk to Digital Persona"):
    profile = load_profile(profile_name)
    memories = load_memories(profile_name)
    if profile:
        reply = simulate_response(profile, memories, user_input)
        st.subheader(f"Response from {profile_name}")
        st.write(reply)
    else:
        st.error(f"No profile found with name '{profile_name}'.")
