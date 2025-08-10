import streamlit as st

st.set_page_config(page_title="Digital Afterlife Engine", layout="centered")
st.title("Digital Afterlife Engine")

st.markdown("""
Welcome to the Digital Afterlife Engine, a space to preserve, simulate, and interact with timeless digital personas.

Choose a module to begin:
""")

st.markdown("### 🧬 Profile Creator")
st.markdown("[Open Profile Creator](profile_creator.py)")

st.markdown("### Memory Vault")
st.markdown("[Open Memory Vault](memory_vault.py)")

st.markdown("### Chat Simulator")
st.markdown("[Open Chat Simulator](chat_simulator.py)")

st.markdown("### Legacy Timeline")
st.markdown("[Open Legacy Timeline](legacy_timeline.py)")

st.markdown("### Voice Synthesizer")
st.markdown("[Open Voice Synthesizer](voice_synthesizer.py)")

st.markdown("---")
st.markdown("Created with 💘 to preserve what matters most.")
