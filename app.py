import streamlit as st
import base64

# --- ABOUT ME ---
def about_me():
    st.title("👋 About Me")
    col1, col2 = st.columns([1, 3])

    with col1:
        # Create circular image with CSS styling
        st.markdown("""
<style>
.circular-image {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #f0f0f0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>
""", unsafe_allow_html=True)

        
        st.markdown(f'<img src="data:image/jpeg;base64,{get_base64_of_image("assets/cleave_img.jpg")}" class="circular-image">', unsafe_allow_html=True)

    with col2:
        st.write("""
        I'm **Cleave Adungo**, a self-driven Data Scientist with a solid foundation in Mathematics.

        With over 3 years of experience as an Accounts Clerk managing Accounts Payable and Receivable, I've developed strong analytical and data-handling capabilities. I also contributed as a Data Annotator at Turing, specializing in image and text labeling for AI training datasets.

        My professional approach centers on hands-on, project-based learning, continuously advancing my skills through real-world applications. I actively participate in Zindi competitions to maintain cutting-edge expertise and demonstrate practical problem-solving abilities.

        I'm seeking opportunities in Data Analysis, Data Science, and AI where I can deliver impactful, data-driven solutions that create measurable business value.
        """)

# Helper function to convert image to base64
import base64
def get_base64_of_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- ACADEMIC QUALIFICATIONS ---
def academic_qualifications():
    st.header("🎓 Academic Qualifications")
    st.markdown("""
    - **Bachelor of Science in Mathematics**, Moi University  
      Focused on core areas including Linear Algebra, Calculus, and Statistics.

    - **Certificate in LLM Engineering**, Udemy  
      Gained practical skills in building and working with Large Language Models (LLMs), including prompt engineering, vector databases, and LangChain.
    """)


# --- WORK EXPERIENCE ---
def work_experience():
    st.header("💼 Work Experience")
    st.markdown("""
- **Data Annotator** — *Turing (Remote)*  
  *Oct 2024 – April 2025*  
  Labeled and validated image and text data for AI model training using tools like **Label Studio**, **SuperAnnotate**, and internal annotation platforms.  
  Gained experience in working remotely with an **international team**, meeting quality standards and deadlines in a fast-paced AI development environment.

- **Accounts Clerk** — *Signature Healthcare Ltd*  
  *June 2021 – Oct 2024*  
  Managed **data entry**, **petty cash**, **debtors**, and **account reconciliations** using **Google Sheets**, **Excel**, and accounting software.  
  Developed strong attention to detail, data organization skills, and hands-on experience working with real-world financial datasets.
    """)


# --- PROJECTS SECTION ---
def projects_section():
    st.header("🚀 Projects")
    st.write("Select a category to explore projects:")

    categories = [
        ("SQL", "pages/sql.py", "sql"),
        ("Machine Learning", "pages/machine_learning.py", "ml"),
        ("Data Analysis", "pages/data_analysis.py", "analysis"),
        ("LLM", "pages/ai.py", "llm"),
        ("Power BI", "pages/power_bi.py", "powerbi")
    ]

    cols = st.columns(5)

    for idx, (name, path, css_class) in enumerate(categories):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="project-tile {css_class}">
                    <a href="/{name.lower().replace(' ', '_')}" target="_self" style="text-decoration: none; color: white;">
                        {name}
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
# --- SKILLS AND TOOLS ---

def skills_and_tools():
    st.header("🛠️ Skills & Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔧 Skills")
        st.markdown("""
        - Python  
        - SQL  (PostgreSQL, SQLite, MySQL)
        - Pandas, NumPy  
        - Scikit-learn, TensorFlow, PyTorch  
        - LangChain,Langgraph, Prompt Engineering  
        - Data Cleaning, Data Preprocessing & EDA  
        - Data Visualization
        - Machine Learning & Deep Learning
        - LLMs & Vector Databases
        - Data Annotation & Labeling
        - Data Entry
        - Web Scraping
        """)

    with col2:
        st.subheader("🧰 Tools & Platforms")
        st.markdown("""
        - Google Sheets, Excel  
        - Power BI  
        - Label Studio, Roboflow  
        - Jupyter, VS Code, Colab  
        - Git, Kaggle  
        - Streamlit

        """)





# --- MAIN APP ---
def main():
    about_me()
    st.markdown("---")
    projects_section()
    st.markdown("---")
    skills_and_tools()
    st.markdown("---")
    academic_qualifications()
    st.markdown("---")
    work_experience()
    st.markdown("---")
    #projects_section()

st.markdown("---")
st.header("📬 Contact")

st.markdown("""
📞 **Phone:** [+254 703 457 427](tel:+254703457427)  
📧 **Email:** [cleavestone94@gmail.com](mailto:cleavestone94@gmail.com)  
🔗 **LinkedIn:** [cleavestone-adungo](https://www.linkedin.com/in/cleavestone-adungo-b3b7ba124/)
""")

st.markdown("---")



if __name__ == "__main__":
    main()
