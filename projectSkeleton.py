import streamlit as st
import pandas as pd

# Load the startup funding dataset
df = pd.read_csv('startup_funding.csv')

# Data cleaning: fill missing investor names
df['Investors Name'] = df['Investors Name'].fillna("Undisclosed")

# Sidebar title
st.sidebar.title("Startup Funding Analysis")

# User selection from sidebar
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

# Display content based on user selection
if option == 'Overall Analysis':
    st.title('Overall Analysis')

elif option == 'Startup':
    # Select startup from dropdown
    st.sidebar.selectbox('Select Startup', sorted(df['Startup Name'].unique().tolist()))

    # Button to trigger startup analysis
    btn1 = st.sidebar.button('Find Startup Details')

    st.title('Startup Analysis')

else:
    # Select investor from dropdown
    st.sidebar.selectbox('Select Investor', sorted(df['Investors Name'].unique().tolist()))

    # Button to trigger investor analysis
    btn2 = st.sidebar.button('Find Investor Details')

    st.title('Investor Analysis')