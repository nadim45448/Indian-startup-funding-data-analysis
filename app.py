import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_icon='Startup Analysis')

# Load the startup funding dataset
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# see investors detail analysis
def load_investor_details(investor):
    st.title(investor)

    # Most Recent Investments
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values, color='blue')
        st.pyplot(fig)
    with col2:
        verical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(verical_series, labels=verical_series.index, autopct="%0.01f%%")

        st.pyplot(fig1)

    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('YoY Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index, year_series.values)

    st.pyplot(fig2)

# Sidebar title
st.sidebar.title("Startup Funding Analysis")

# User selection from sidebar
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

# Display content based on user selection
if option == 'Overall Analysis':
    st.title('Overall Analysis')

elif option == 'Startup':
    # Select startup from dropdown
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))

    # Button to trigger startup analysis
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')

else:
    # Select investor from dropdown
    selectedInvestor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))

    # Button to trigger investor analysis
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selectedInvestor)