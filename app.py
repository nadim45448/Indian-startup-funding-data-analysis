import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_icon='Startup Analysis')

# Load the startup funding dataset
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Function to display overall investment analysis dashboard
def load_overall_analysis():
    st.title('Overall Analysis')

    # Calculate total invested amount across all startups
    total = round(df['amount'].sum())

    # Find the highest funding received by a single startup (max deal size)
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]

    # Compute average funding per startup (total funding divided by number of startups)
    avg_funding = df.groupby('startup')['amount'].sum().mean()

    # Count unique startups that received funding
    num_startups = df['startup'].nunique()

    # Create 4 columns layout for key metrics
    col1, col2, col3, col4 = st.columns(4)

    # Display key metrics using Streamlit cards
    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')
    with col3:
        st.metric('Avg', str(round(avg_funding)) + ' Cr')
    with col4:
        st.metric('Funded Startups', num_startups)

    st.header('MoM graph')

    # Let user choose between total investment or number of deals (Month-on-Month)
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])

    # Aggregate data based on user selection
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    # Create a combined month-year label for x-axis
    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    # Plot the trend line
    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])

    # Display plot in Streamlit
    st.pyplot(fig3)

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
st.session_state.option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])
option = st.session_state.option

# Display content based on user selection
if option == 'Overall Analysis':
    load_overall_analysis()

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