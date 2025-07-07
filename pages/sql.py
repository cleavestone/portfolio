import streamlit as st

st.set_page_config(page_title="SQL Projects", page_icon="🧠")

st.title("🧠 SQL Project")
st.markdown("Welcome to a hands-on SQL project with realistic, randomly generated datasets.")

# --- Project Overview ---
st.header("📌 Project Overview")
st.markdown("""
This SQL project helps reinforce core SQL concepts through practical, structured exercises.

You'll work with **3 synthetic tables** — `customers`, `products`, and `orders` — populated using Python and Faker.

You’ll write queries involving:
- JOINs and Aggregations
- Subqueries and Window Functions
- Views and Stored Procedures
""")

# --- Sample Query ---
st.header("📊 Sample Query & Output")

st.markdown("**🧠 Task:** *Find the top 5 customers who have spent the most money on orders.*")

with st.expander("💡 View SQL Query"):
    st.code("""
SELECT
    c.customer_name,
    c.email,
    SUM(o.quantity * p.price) AS total_spent
FROM customers AS c
JOIN orders AS o ON c.customer_id = o.customer_id
JOIN products AS p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name, c.email
ORDER BY total_spent DESC
LIMIT 5;
""", language="sql")

# Sample Output Table
st.markdown("**📌 Example Output:**")

st.dataframe({
    "customer_name": ["Alex Jenkins", "Thomas Barry", "James Allen", "Megan Delacruz", "Judith Allen"],
    "email": [
        "zjames@martinez.com",
        "raymondferguson@kirby-price.com",
        "nicholerasmussen@guzman.com",
        "karen58@hotmail.com",
        "rebekahsparks@moore.com"
    ],
    "total_spent": [24745.24, 22559.63, 19875.42, 19677.49, 19537.91]
})

# --- Project Structure ---
st.header("📂 Project Structure")

st.markdown("""
- `customers.csv` — Customer data with names, emails, and signup dates  
- `products.csv` — Product catalog with names and prices  
- `orders.csv` — Orders including quantity and order date  
- `create_tables.sql` — Table definitions  
- `insert_data.sql` — Populates the tables  
- `queries.sql` — Practice problems + solutions  
- `views_and_stored_procedures.sql` — Advanced SQL concepts
""")

# --- Database Schema ---
st.header("🧱 Database Schema")

with st.expander("📄 View Schema Details"):
    st.markdown("### `customers`")
    st.code("""customer_id INT (PK)
customer_name VARCHAR
email VARCHAR
signup_date DATE""")

    st.markdown("### `products`")
    st.code("""product_id INT (PK)
product_name VARCHAR
price DECIMAL""")

    st.markdown("### `orders`")
    st.code("""order_id INT (PK)
customer_id INT (FK)
product_id INT (FK)
order_date DATE
quantity INT""")

# --- Concepts Practiced ---
st.header("✅ SQL Concepts Practiced")

cols = st.columns(2)
with cols[0]:
    st.markdown("""
- 🔗 JOINs (INNER, LEFT)
- 📊 GROUP BY & Aggregations
- 📆 Filtering with WHERE & dates
- 🔍 Subqueries
- 🧩 CASE statements
- 🧵 Pattern matching (LIKE)
    """)
with cols[1]:
    st.markdown("""
- 📐 Window Functions (ROW_NUMBER, RANK)
- 🧱 CTEs with `WITH`
- ♻️ Set operations (UNION, INTERSECT)
- 👁️ Views
- ⚙️ Stored Procedures
    """)

# --- Getting Started ---
st.header("🚀 Getting Started")

st.markdown("""
1. Run `create_tables.sql` to set up tables  
2. Load data using either:
   - `LOAD DATA INFILE` (CSV-based)
   - Manual `INSERT` from `insert_data.sql`  
3. Run queries from `queries.sql` or write your own  
4. Track your learning and build on top of this!
""")

# --- Footer ---
st.markdown("---")
st.page_link("app.py", label="⬅️ Back to Home", icon="🏠")
st.markdown("🔗 [View Full Project on GitHub](https://github.com/cleavestone/DATA-ANALYSIS-SQL)")

