import streamlit as st

st.title("Voice Synthesizer")

uploaded_file = st.file_uploader("Upload voice sample (MP3 or WAV)", type=["mp3", "wav"])

if uploaded_file:
    st.audio(uploaded_file, format="audio/mp3")
    st.success("Voice sample uploaded successfully.")
else:
    st.info("No voice sample uploaded yet.")

st.subheader("Simulated Voice Response")
simulated_text = st.text_area("Enter response text to simulate voice")

if st.button("Generate Voice"):
    if simulated_text:
        st.markdown(" _Simulated voice would play here using external API._ ")
        st.write(simulated_text)
    else:
        st.error("Please enter text to simulate voice.")
