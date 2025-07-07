import streamlit as st

st.subheader("🎬 Semantic Movie Recommender System")
st.markdown("""
This intelligent movie recommender app leverages vector similarity to suggest movies based on user-input descriptions or preferences. Built using LanceDB, Sentence Transformers, and Streamlit, it semantically matches your input to movie metadata for highly relevant recommendations.

**Project Highlights:**
- Loaded movie metadata from an Amazon S3 bucket
- Cleaned and preprocessed movie descriptions
- Generated sentence embeddings using `SentenceTransformers`
- Stored embeddings in a `LanceDB` vector database
- Performed semantic search to retrieve top-k similar movies
- Designed an intuitive Streamlit interface for user interaction
- Deployed on AWS EC2

🔗 [View Full Code & Dataset on GitHub](https://github.com/cleavestone/Movie_Recommender_App)
""")
st.video("assets\project_visuals\Activity _ Cleavestone Adungo _ LinkedIn - Google Chrome 2025-07-07 15-55-05.mp4")
st.markdown("---")

import streamlit as st

st.subheader("🧠 MCQ Generator using LangChain")
st.markdown("""
This interactive MCQ generator allows users to upload PDFs or text files and instantly generate multiple-choice questions powered by LangChain. Designed for educators, learners, and trainers, it leverages the power of Large Language Models to produce high-quality assessment questions.

**Project Highlights:**
- Accepts both PDF and plain text file uploads
- Uses LangChain to generate contextual MCQs from content
- Displays questions with options and highlights correct answers
- Clean, responsive interface built with Streamlit
- Handles exceptions and logs errors for debugging
- Well-structured modular codebase for easy expansion
- Version control with Git and DVC for better collaboration

**Technologies Used:**
- `LangChain` for interfacing with LLMs
- `Streamlit` for the front-end application
- `PyMuPDF` and `pdfplumber` for text extraction from PDFs
- `Python` for backend logic
- `Git + GitHub` for version control and collaboration

📎 [View Full Code on GitHub](https://github.com/cleavestone/MCQ_GEN)
""")
st.video("assets\project_visuals\MCQ_application.mp4")
st.markdown("---")

st.page_link("app.py", label="⬅️ Back to Home", icon="🏠")