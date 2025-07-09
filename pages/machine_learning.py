import streamlit as st

def app():
    st.set_page_config(page_title="Machine Learning Projects", page_icon="🧠")
    
    st.title("🧠 Machine Learning Projects")
    st.markdown("Explore a collection of machine learning projects across supervised, unsupervised, and time-series techniques.")
    
    # -- Project 1: California House Price Prediction --
    st.subheader("🏠 California Housing Price Prediction")
    st.markdown("""
    A regression project using the **California housing dataset** to predict median house prices across districts using features such as income, total rooms, ocean proximity, and more.

    **Project Highlights:**
    - 📊 Performed detailed EDA to uncover data patterns and outliers
    - 🧪 Engineered new features, including geographic clusters using KMeans
    - 🧹 Preprocessed data with pipelines (scaling + encoding)
    - 🤖 Trained multiple models including Random Forest, KNN, and **XGBoost**
    - 📈 Achieved **R² = 0.748** and **RMSE ≈ 58,575** on the test set
    - 💻 Built a **Streamlit app** to allow interactive predictions (locally hosted)

    🔗 [View Project on GitHub](https://github.com/cleavestone/CARLIFORNIA-HOUSE-PREDICTION)
    """)
    
    st.markdown("---")
    
    # -- Project 2: RFM Customer Segmentation --
    st.subheader("🧪 RFM Analysis (Customer Segmentation)")
    st.markdown("""
    Applied **RFM (Recency, Frequency, Monetary)** analysis and clustering (KMeans) to segment customers from e-commerce transactional data.

    **Highlights:**
    - Cleaned and preprocessed large transactional dataset with null handling and type conversions
    - Engineered key features: Recency, Frequency, Monetary value per customer
    - Used StandardScaler for feature scaling before clustering
    - Determined optimal clusters using Elbow method and evaluated with Silhouette score (~0.60)
    - Clustered customers into 3 actionable segments with clear profiles
    - Visualized clusters in 2D space using PCA for dimensionality reduction

    🔗 [View Project on GitHub](https://github.com/cleavestone/Customer-Segmentation)
    """)
    
    st.image("assets/project_visuals/image11.png", caption="PCA Visualization of Customer Clusters", use_container_width=True)
    
    st.markdown("---")
    
    # -- Project 3: PM2.5 Air Pollution Forecasting with LSTM --
    st.subheader("🌫️ Air Pollution PM2.5 Forecasting")
    st.markdown("""
    Air pollution poses significant health risks worldwide. This project uses deep learning (LSTM) to forecast PM2.5 concentrations based on environmental factors such as temperature, humidity, pressure, wind speed, and wind direction.

    **Project Highlights:**
    - Explored and preprocessed a 6-year hourly air quality dataset
    - Handled missing data and engineered datetime features
    - Visualized trends and seasonality with decomposition analysis
    - One-hot encoded categorical wind direction and normalized features
    - Created sequences for LSTM input and split into train/test sets
    - Built a multi-layer LSTM model with dropout and dense layers
    - Trained the model to predict future PM2.5 values with low error
    - Visualized predicted vs. actual PM2.5 concentration
    - Forecasted PM2.5 for the next 24 hours using model predictions

    🔗 [View Full Code & Dataset on GitHub](https://github.com/cleavestone/Air_quality_Forecasting)
    """)
    
    st.image("assets/project_visuals/image111.png", caption="Predicted vs Actual PM2.5 Concentration", use_container_width=True)
    
    st.markdown("---")
    

