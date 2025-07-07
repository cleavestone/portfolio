```
streamlit_portfolio/
│
├── app.py                        # 🌐 Main Streamlit app
├── projects.json                 # 📦 Static summaries of your projects
├── chatbot.py                    # 🤖 LLM chatbot (static knowledge base)
│
├── assets/                       # 📸 Images, logos, icons
│   ├── cleave_img.jpg
│   └── project_visuals/
│       ├── medical_chatbot.png
│       └── pothole_detection.png
│
├── style/                        # 🎨 Custom CSS for styling (optional)
│   └── main.css
│
├── utils/                        # ⚙️ Helper functions
│   └── layout.py                 # Layout helpers like card display, etc.
│
├── requirements.txt              # 📦 Python dependencies
└── README.md                     # 📝 Project overview for GitHub
```

```
🔍 File Purpose Overview
File/Folders	Purpose
app.py	Main Streamlit app that loads everything, handles UI, navigation, chatbot UI
projects.json	Contains structured project summaries and links
chatbot.py	Handles static chatbot logic with summaries loaded from projects.json
assets/	Holds profile picture, project images
style/main.css	Optional custom styles to enhance UI
utils/layout.py	Python functions to render buttons, cards, section titles etc.
requirements.txt	All required packages like streamlit, openai, langchain, etc.
README.md	GitHub info (your current portfolio readme)
```