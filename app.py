import streamlit as st
from utils.audio_to_text import transcribe_audio
from utils.text_analysis import analyze_text
from utils.summarization import summarize_interview, generate_feedback

st.set_page_config(page_title="AI Interview Analyzer", layout="wide")
st.title("AI Interview Analyzer – Your Personal AI Mentor")

# Input Selection
st.sidebar.header("Upload Input")
input_type = st.sidebar.radio("Choose Input Type:", ["Audio File", "Text Transcript"])

if input_type == "Audio File":
    audio_file = st.file_uploader("Upload Audio File", type=["mp3","wav"])
    if audio_file:
        with open("temp_audio.mp3","wb") as f:
            f.write(audio_file.getbuffer())
        st.info("Transcribing Audio...")
        transcript = transcribe_audio("temp_audio.mp3")
        st.subheader("Transcript")
        st.write(transcript)

elif input_type == "Text Transcript":
    transcript = st.text_area("Paste text transcript here:")

if st.button("Analyze"):
    if transcript:
        analysis = analyze_text(transcript)
        summary = summarize_interview(transcript)
        feedback = generate_feedback(analysis)
        
        st.subheader("Interview Analysis")
        st.json(analysis)
        
        st.subheader("Summary")
        st.write(summary)
        
        st.subheader("Suggested Improvements")
        for item in feedback:
            st.write(f"- {item}")
