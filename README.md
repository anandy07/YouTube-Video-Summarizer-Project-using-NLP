# 📽️ YouTube Video Summarizer

YouTube Video Summarizer is an AI-powered web app that automatically generates concise summaries of YouTube videos. It extracts subtitles using the YouTubeTranscriptApi and uses advanced NLP models (like BART from Hugging Face) to summarize the content. Built with Python and Streamlit, the app helps users quickly understand long videos without watching them in full.
---

## 🚀 Features

- ✅ **Transcript Extraction** using `YouTubeTranscriptApi`  
- ✅ **Summarization** using Hugging Face Transformers (BART / T5 / Pegasus)  
- ✅ **Streamlit Web App** with clean and simple interface  
- ✅ **Chunked Summarization** for long videos  
- ✅ **Graceful Handling** of missing subtitles or unsupported videos

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **NLP Models**: Hugging Face Transformers  
- **Transcript API**: `youtube-transcript-api`  
- **Libraries**: Transformers, Requests, Streamlit, NLTK, Regex  

---

## 🧠 How It Works

### 📓 Jupyter Notebook (`YouTube_Video_Summarizer_Project_using_NLP.ipynb`)

- Loads the video ID from a YouTube URL  
- Uses `YouTubeTranscriptApi` to fetch the transcript  
- Chunks long transcripts into manageable pieces  
- Feeds chunks to a summarization model (BART by default)  
- Combines and displays the final summarized text  


---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/youtube-video-summarizer.git
cd youtube-video-summarizer
## 📌 Usage

To run the Streamlit app:

```bash
streamlit run app.py
```

> You'll see a web interface where you can select a YouTube video and get a summarized version of its content.

---

## 📁 File Structure

```
.
├── app.py                              # Streamlit frontend
├── YouTube_Video_Summarizer_Project_using_NLP.ipynb  # Jupyter Notebook for data prep
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

---

## ✨ Future Ideas

* Add speech-to-text fallback if subtitles are not available  
* Allow model selection (BART, T5, Pegasus) directly from UI  
* Display both transcript and summary side-by-side  
* Save/download summary as .txt or PDF  
* Add summary language translation support  
* Deploy on Hugging Face or Streamlit Cloud with login support  

---

## 🧑‍💻 Author

Developed by **Anand Yadav**  
GitHub: [@anandy07](https://github.com/anandy07)  
Live App: *Coming soon...*

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Contribute & Support

If you liked this project, consider giving it a **⭐ star** on GitHub!  
Pull requests, issues, and suggestions are always welcome.
