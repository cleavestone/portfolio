import streamlit as st

st.subheader("📊 Glassdoor Data Science Job Market Analysis")
st.markdown("""
This project analyzes data science job postings scraped from Glassdoor to uncover insights on recruitment trends, salary patterns, and required skills.

**Project Highlights:**
- Cleaned and preprocessed 600+ job postings with salary parsing and location splitting
- Extracted in-demand skills like Python, SQL, AWS, and Power BI from job descriptions
- Visualized the most marketable skills and salary distributions across job titles and states
- Identified top-paying roles and companies in the data science field
- Explored correlations between company ratings, job locations, and salary offerings

🔗 [View Full Code](https://github.com/cleavestone/Data-Analytics/blob/main/Data_cleaning_glassdoor_data_science_jobs.ipynb)

""")

# Show a key plot image — replace with your own plot file path
st.image("assets/project_visuals/image112.png", 
         caption="Most Marketable Skills in Data Science Jobs (Extracted from Job Descriptions)",
         use_container_width=True)

st.markdown("---")

st.subheader("💼 Web Scraping Brighter Monday Job Listings")
st.markdown("""
Brighter Monday is one of the most popular job platforms in Kenya. This project involved scraping job listings and analyzing hiring trends, job types, salary ranges, and industries across different locations.

**Project Highlights:**
- Scraped job listings from 80 pages of BrighterMonday using `requests` and `BeautifulSoup`
- Extracted job title, company name, industry, job type, location, and salary range
- Stored HTML pages locally and parsed data into a Pandas DataFrame
- Performed data cleaning by removing duplicates and standardizing locations
- Conducted exploratory data analysis to uncover hiring trends
- Visualized job distributions by location, industry, and remote availability

🔗 [View Full Code on GitHub](https://github.com/cleavestone/Data-Analytics/blob/main/SCRAPING%20BRIGHTER%20MONDAY%20JOB%20LISTINGS.ipynb)
""")

# Display an example plot – replace with your actual path
st.image("assets/project_visuals/image113.png", 
         caption="Distribution of Job Listings by Location", 
         use_container_width=True)

st.markdown("---")
st.page_link("app.py", label="⬅️ Back to Home", icon="🏠")

# Optionally, add more visualizations below
# st.image("path_to_your_industry_distribution_plot.png", caption="Distribution by Industry", use_column_width=True)
# st.image("path_to_your_remote_jobs_plot.png", caption="Remote Work Opportunities by Industry", use_column_width=True)

