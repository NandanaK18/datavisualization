import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data
file_path = "F:\healthcare_dataset.csv\healthcare_dataset.csv"
data = pd.read_csv(file_path)

# Set the title of the dashboard
st.title('Healthcare Data Dashboard')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.selectbox('Select a page:', ['Home', 'Age Distribution', 'Billing Amounts by Condition'])

# Home page
if page == 'Home':
    st.header('Home')
    st.write("Welcome to the healthcare data dashboard!")
    st.dataframe(data)

# Age Distribution
elif page == 'Age Distribution':
    st.header('Age Distribution')
    fig, ax = plt.subplots()
    sns.histplot(data['Age'], bins=20, ax=ax)
    ax.set_title('Age Distribution')
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    st.pyplot(fig)

# Billing Amounts by Condition
elif page == 'Billing Amounts by Condition':
    st.header('Billing Amounts by Medical Condition')
    fig = px.box(data, x='Medical Condition', y='Billing Amount', title='Billing Amounts by Medical Condition')
    st.plotly_chart(fig)
