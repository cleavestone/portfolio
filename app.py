import streamlit as st
import base64

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Cleave's Portfolio",
    page_icon="👨‍💻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- LOAD EXTERNAL CSS ---
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

local_css("style/main.css")

# --- HELPER FUNCTIONS ---
def get_base64_of_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def get_base64_of_pdf(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- ABOUT ME ---
def about_me():
    st.title("👋 About Me")
    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown(
            f'<img src="data:image/jpeg;base64,{get_base64_of_image("assets/cleave_img.jpg")}" class="circular-image">',
            unsafe_allow_html=True
        )

    with col2:
        st.write("""
        I'm **Cleave Adungo**, a self-driven Data Scientist with a solid foundation in Mathematics.

        With over 3 years of experience as an Accounts Clerk managing Accounts Payable and Receivable, I've developed strong analytical and data-handling capabilities. I also contributed as a Data Annotator at Turing, specializing in image and text labeling for AI training datasets.

        My professional approach centers on hands-on, project-based learning, continuously advancing my skills through real-world applications. I actively participate in Zindi competitions to maintain cutting-edge expertise and demonstrate practical problem-solving abilities.

        I'm seeking opportunities in Data Analysis, Data Science, and AI where I can deliver impactful, data-driven solutions that create measurable business value.
        """)

        # Resume download button
        pdf_base64 = get_base64_of_pdf("assets/cleave_resume.pdf")
        href = f'''
        <div style="text-align:center;">
            <a href="data:application/pdf;base64,{pdf_base64}" download="Cleave_Resume.pdf" class="download-button">📄 Download Resume</a>
        </div>
        '''
        st.markdown(href, unsafe_allow_html=True)



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
