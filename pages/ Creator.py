import streamlit as st
import json
import os

profile_path = "saved_profiles.json"

def save_profile(profile_data):
    if os.path.exists(profile_path):
        with open(profile_path, "r") as f:
            data = json.load(f)
    else:
        data = {}
    data[profile_data["name"]] = profile_data
    with open(profile_path, "w") as f:
        json.dump(data, f)

def load_profile(name):
    if os.path.exists(profile_path):
        with open(profile_path, "r") as f:
            data = json.load(f)
        return data.get(name, None)
    return None

st.title("Profile Creator")

name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)

traits = st.multiselect("Personality Traits", ["Empathetic", "Witty", "Wise", "Curious", "Calm", "Playful", "Serious", "Warm"])
phrases = st.text_area("Favorite Phrases (comma separated)", "Stay curious, I love you more than words")
lessons = st.text_area("Life Lessons or Philosophies", "Always choose kindness over being right.")
tone = st.radio("Emotional Tone", ["Reflective", "Playful", "Serious", "Warm"])

profile = {
    "name": name,
    "age": age,
    "traits": traits,
    "phrases": [p.strip() for p in phrases.split(",") if p.strip()],
    "lessons": lessons,
    "tone": tone
}

if st.button("Save Profile"):
    if name:
        save_profile(profile)
        st.success(f"Profile '{name}' saved.")
    else:
        st.error("Please enter a name before saving.")

load_name = st.text_input("Load Profile by Name")
if st.button("Load Profile"):
    loaded = load_profile(load_name)
    if loaded:
        st.subheader(f"Loaded Profile: {load_name}")
        st.json(loaded)
    else:
        st.error(f"No profile found with name '{load_name}'.")
