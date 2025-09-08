import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import re
import nltk
import requests
from PIL import Image
from io import BytesIO

# Download NLTK punkt tokenizer
nltk.download("punkt")

# ------------------- App Config -------------------
st.set_page_config(
    page_title="Briefly (YouTube Video Summarizer)",
    layout="wide",
    page_icon="📹"
)

st.title("📹 YouTube Video Summarizer")
st.write("Enter a YouTube video URL to get a summarized version of its transcript.")

# ---------------- Helper Functions ----------------
def get_video_id(url):
    """Extract YouTube video ID from URL."""
    patterns = [r"v=([a-zA-Z0-9_-]{11})", r"youtu\.be/([a-zA-Z0-9_-]{11})"]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def fetch_transcript(video_id):
    """Fetch English transcript. Return None if unavailable."""
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        for transcript in transcript_list:
            if transcript.language_code == 'en':
                transcript_text = transcript.fetch()
                return " ".join([t['text'] for t in transcript_text])
        return None
    except (TranscriptsDisabled, NoTranscriptFound):
        return None
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred: {e}")
        return None

def summarize_text(text, sentence_count=5):
    """Summarize the transcript using LexRank algorithm."""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join([str(sentence) for sentence in summary])

def get_video_thumbnail(video_id):
    """Return the YouTube video thumbnail URL."""
    return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

# ---------------- Main App ----------------
video_url = st.text_input("YouTube Video URL:")

if video_url:
    video_id = get_video_id(video_url)
    if video_id:
        # Display medium video thumbnail
        thumbnail_url = get_video_thumbnail(video_id)
        response = requests.get(thumbnail_url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="Video Thumbnail", width=400)  # medium thumbnail

        transcript = fetch_transcript(video_id)
        if transcript:
            # Use columns: transcript on left, summary on right
            col1, col2 = st.columns([2, 1])  # transcript wider than summary

            with col1:
                with st.expander("📝 Full Transcript"):
                    st.write(transcript)
                    st.button("📋 Copy Transcript", key="copy_transcript")

            with col2:
                summary = summarize_text(transcript, sentence_count=5)  # fixed 5 sentences
                with st.expander("🗒 Video Summary"):
                    st.write(summary)
                    st.button("📋 Copy Summary", key="copy_summary")

        else:
            st.warning("⚠️ Transcript not available for this video.")
    else:
        st.error("❌ Invalid YouTube URL.")
