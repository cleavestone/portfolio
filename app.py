import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Cleave's Portfolio",
    page_icon="👨‍💻",
    layout="centered",  # Better for mobile
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass  # Skip if CSS file doesn't exist yet

local_css("style/main.css")


# --- ABOUT ME ---
def about_me():
    st.title("👋 About Me")
    col1, col2 = st.columns([1, 3])

    with col1:
        img_data = get_base64_of_image("assets/cleave_img.jpg")
        st.markdown(f'<div class="circular-img-container"><img src="data:image/jpeg;base64,{img_data}" /></div>', unsafe_allow_html=True)

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
        ("SQL", "sql"),
        ("Machine Learning", "ml"),
        ("Data Analysis", "analysis"),
        ("LLM", "llm"),
        ("Power BI", "powerbi")
    ]

    cols = st.columns(len(categories))

    for idx, (name, page_key) in enumerate(categories):
        with cols[idx]:
            # This will render a div that looks like a button and navigates via query params
            st.markdown(
                f"""
                <a href="?page={page_key}">
                    <div class="project-tile {page_key}">
                        {name}
                    </div>
                </a>
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
        - SQL (PostgreSQL, SQLite, MySQL)  
        - Pandas, NumPy  
        - Scikit-learn, TensorFlow, PyTorch  
        - LangChain, Langgraph, Prompt Engineering  
        - Data Cleaning, Preprocessing, EDA  
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

# --- CONTACT SECTION ---
def contact():
    st.header("📬 Contact")
    st.markdown("""
📞 **Phone:** [+254 703 457 427](tel:+254703457427)  
📧 **Email:** [cleavestone94@gmail.com](mailto:cleavestone94@gmail.com)  
🔗 **LinkedIn:** [cleavestone-adungo](https://www.linkedin.com/in/cleavestone-adungo-b3b7ba124/)
    """)

# --- MAIN APP ---
def main():
   # --- PAGE CONFIG ---
    st.set_page_config(
        page_title="Cleave's Portfolio",
        page_icon="👨‍💻",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- HIDE SIDEBAR ---
    hide_sidebar_style = """
        <style>
            [data-testid="stSidebar"], [data-testid="collapsedControl"] {
                display: none !important;
            }
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)

    query_params = st.query_params
    page = query_params.get("page", "home")
    st.session_state.page = page
    
    def page_navigation(current):
        pages = {
            "home": "🏠 Home",
            "sql": "🗃️ SQL",
            "ml": "🤖 Machine Learning",
            "analysis": "📊 Data Analysis",
            "llm": "🧠 LLM",
            "powerbi": "📈 Power BI"
        }

        nav_buttons = ""
        for key, label in pages.items():
            if key != current:
                nav_buttons += f'<a href="?page={key}" class="nav-button">{label}</a> '

        st.markdown(f"""
            <div class="nav-container">{nav_buttons}</div>
        """, unsafe_allow_html=True)


    if page == "home":
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
        contact()
        st.markdown("---")
    elif page == "sql":
        sql_app()
        page_navigation("sql")
    elif page == "ml":
        ml_app()
        page_navigation("ml")
    elif page == "analysis":
        analysis_app()
        page_navigation("analysis")
    elif page == "llm":
        llm_app()
        page_navigation("llm")
    elif page == "powerbi":
        power_bi_app()
        page_navigation("powerbi")



if __name__ == "__main__":
    main()
