import streamlit as st

st.subheader("📊 Interactive Sales Dashboard in Power BI")
st.markdown("""
This project showcases a dynamic and visually engaging sales dashboard built using Power BI. The dashboard provides critical insights into total sales, profit, performance by product and category, and supports interactive filtering for deep analysis.

**Project Highlights:**
- Loaded and cleaned a structured sales dataset in Power BI
- Transformed data using Power Query (M language)
- Created calculated columns and DAX measures for profit and % profit
- Designed an intuitive dashboard layout with cards, bar charts, treemaps, and time-series visuals
- Added slicers for filtering by:
  - **Year**
  - **Month**
  - **Sales Type** (Direct, Online, Wholesaler)
  - **Payment Mode** (Cash, Online)
- Highlighted top-performing products and categories using KPI visuals
- Enabled month-wise performance tracking and trend analysis

**Technologies Used:**
- `Power BI Desktop` for data transformation and dashboard design
- `Power Query` for data wrangling
- `DAX` for calculations and aggregations
- `Excel`/CSV for data source

🖼️ Dashboard Snapshot:
""")
st.image("assets/project_visuals/Power BI Desktop 7_7_2025 6_11_54 PM.png", caption="Interactive Power BI Sales Dashboard", use_container_width=True)
st.markdown("---")

st.page_link("app.py", label="⬅️ Back to Home", icon="🏠")
