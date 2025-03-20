
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import warnings
warnings.filterwarnings('ignore')

# Custom CSS to hide the Streamlit header elements
hide_header_css = """
<style>
    /* Hide the "Deploy" button */
    .stDeployButton {
        display: none;
    }

    /* Hide the "Hamburger" menu */
    #MainMenu {
        visibility: hidden;
    }

    /* Hide the footer */
    footer {
        visibility: hidden;
    }

    /* Hide the Streamlit header */
    header {
        visibility: hidden;
    }

    /* Optional: Add padding to the top of the page */
    .stApp {
        margin-top: -50px;
    }
</style>
"""

# Inject custom CSS
st.markdown(hide_header_css, unsafe_allow_html=True)

# Function to generate plots
def generate_plots(df):
    df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})

    numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

    # Gender and Churn Distributions
    g_labels = ['Male', 'Female']
    c_labels = ['No', 'Yes']
    fig1 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig1.add_trace(go.Pie(labels=g_labels, values=df['gender'].value_counts(), name="Gender"), 1, 1)
    fig1.add_trace(go.Pie(labels=c_labels, values=df['Churn'].value_counts(), name="Churn"), 1, 2)
    fig1.update_traces(hole=.4, hoverinfo="label+percent+name", textfont_size=16)
    fig1.update_layout(title_text="Gender and Churn Distributions", annotations=[dict(text='Gender', x=0.16, y=0.5, font_size=20, showarrow=False), dict(text='Churn', x=0.84, y=0.5, font_size=20, showarrow=False)])
    st.plotly_chart(fig1)

    # Churn Distribution w.r.t Gender
    churn_counts = df['Churn'].value_counts()
    gender_counts = df.groupby(['Churn', 'gender']).size().unstack()

    values = [churn_counts.get('Yes', 0), churn_counts.get('No', 0)]
    sizes_gender = [
       gender_counts.loc['Yes', 'Female'] if 'Yes' in gender_counts.index and 'Female' in gender_counts.columns else 0,
       gender_counts.loc['Yes', 'Male'] if 'Yes' in gender_counts.index and 'Male' in gender_counts.columns else 0,
       gender_counts.loc['No', 'Female'] if 'No' in gender_counts.index and 'Female' in gender_counts.columns else 0,
       gender_counts.loc['No', 'Male'] if 'No' in gender_counts.index and 'Male' in gender_counts.columns else 0
    ]

    plt.figure(figsize=(6, 6))
    labels = ["Churn: Yes", "Churn: No"]
    labels_gender = ["F", "M", "F", "M"]
    colors = ['#ff6666', '#66b3ff']
    colors_gender = ['#c2c2f0', '#ffb3e6', '#c2c2f0', '#ffb3e6']
    explode = (0.3, 0.3)
    explode_gender = (0.1, 0.1, 0.1, 0.1)
    textprops = {"fontsize": 15}

    plt.pie(values, labels=labels, autopct='%1.1f%%', pctdistance=1.08, labeldistance=0.8,
        colors=colors, startangle=90, frame=True, explode=explode, radius=10,
        textprops=textprops, counterclock=True)

    plt.pie(sizes_gender, labels=labels_gender, colors=colors_gender, startangle=90,
        explode=explode_gender, radius=7, textprops=textprops, counterclock=True)

    centre_circle = plt.Circle((0, 0), 5, color='black', fc='white', linewidth=0)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title('Churn Distribution w.r.t Gender: Male(M), Female(F)', fontsize=15, y=1.1)
    plt.axis('equal')
    plt.tight_layout()
    st.pyplot(plt.gcf())
   
    # Customer contract distribution
    fig3 = px.histogram(df, x="Churn", color="Contract", barmode="group", title="<b>Customer contract distribution<b>")
    fig3.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig3)

    # Payment Method Distribution
    labels = df['PaymentMethod'].unique()
    values = df['PaymentMethod'].value_counts()
    fig4 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig4.update_layout(title_text="<b>Payment Method Distribution</b>")
    st.plotly_chart(fig4)

    # Customer Payment Method distribution w.r.t. Churn
    fig5 = px.histogram(df, x="Churn", color="PaymentMethod", title="<b>Customer Payment Method distribution w.r.t. Churn</b>")
    fig5.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig5)

    # Churn Distribution w.r.t. Internet Service and Gender
    fig6 = go.Figure()
    fig6.add_trace(go.Bar(x=[['Churn:No', 'Churn:No', 'Churn:Yes', 'Churn:Yes'], ["Female", "Male", "Female", "Male"]], y=[965, 992, 219, 240], name='DSL'))
    fig6.add_trace(go.Bar(x=[['Churn:No', 'Churn:No', 'Churn:Yes', 'Churn:Yes'], ["Female", "Male", "Female", "Male"]], y=[889, 910, 664, 633], name='Fiber optic'))
    fig6.add_trace(go.Bar(x=[['Churn:No', 'Churn:No', 'Churn:Yes', 'Churn:Yes'], ["Female", "Male", "Female", "Male"]], y=[690, 717, 56, 57], name='No Internet'))
    fig6.update_layout(title_text="<b>Churn Distribution w.r.t. Internet Service and Gender</b>")
    st.plotly_chart(fig6)

    # Dependents distribution
    color_map = {"Yes": "#FF97FF", "No": "#AB63FA"}
    fig7 = px.histogram(df, x="Churn", color="Dependents", barmode="group", title="<b>Dependents distribution</b>", color_discrete_map=color_map)
    fig7.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig7)

    # Churn distribution w.r.t. Partners
    color_map = {"Yes": '#FFA15A', "No": '#00CC96'}
    fig8 = px.histogram(df, x="Churn", color="Partner", barmode="group", title="<b>Churn distribution w.r.t. Partners</b>", color_discrete_map=color_map)
    fig8.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig8)

    # Churn distribution w.r.t. Senior Citizen
    color_map = {"Yes": '#00CC96', "No": '#B6E880'}
    fig9 = px.histogram(df, x="Churn", color="SeniorCitizen", title="<b>Churn distribution w.r.t. Senior Citizen</b>", color_discrete_map=color_map)
    fig9.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig9)

    # Churn w.r.t Online Security
    color_map = {"Yes": "#FF97FF", "No": "#AB63FA"}
    fig10 = px.histogram(df, x="Churn", color="OnlineSecurity", barmode="group", title="<b>Churn w.r.t Online Security</b>", color_discrete_map=color_map)
    fig10.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig10)

    # Churn distribution w.r.t. Paperless Billing
    color_map = {"Yes": '#FFA15A', "No": '#00CC96'}
    fig11 = px.histogram(df, x="Churn", color="PaperlessBilling", title="<b>Churn distribution w.r.t. Paperless Billing</b>", color_discrete_map=color_map)
    fig11.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig11)

    # Churn distribution w.r.t. TechSupport
    fig12 = px.histogram(df, x="Churn", color="TechSupport", barmode="group", title="<b>Churn distribution w.r.t. TechSupport</b>")
    fig12.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig12)

    # Churn distribution w.r.t. Phone Service
    color_map = {"Yes": '#00CC96', "No": '#B6E880'}
    fig13 = px.histogram(df, x="Churn", color="PhoneService", title="<b>Churn distribution w.r.t. Phone Service</b>", color_discrete_map=color_map)
    fig13.update_layout(width=700, height=500, bargap=0.1)
    st.plotly_chart(fig13)

# Streamlit app
st.title("Customer Churn Analysis")

col1,col1,col3 = st.columns([.1,5,10])

with col1:
    
    # Year selection
    years = [2020, 2021, 2022, 2023, 2024]
    selected_year = st.selectbox("Select Year", years, index=years.index(2023), format_func=lambda x: f"{x} (Not Available)" if x < 2023 else str(x))

    # Disable the select box for years before 2023
    if selected_year < 2023:
        st.warning("Please select a year from 2023 or 2024 to proceed.")
    else:
        # Quarter selection
        quarters = [f"{selected_year}Quarter{i}" for i in range(1, 5)]
        selected_quarter = st.selectbox("Select Quarter", quarters)

        # Fetch data from the specified URL
        url = f"http://localhost:8084/data/{selected_quarter}"
        response = requests.get(url)
    
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    
    st.write("Data Preview:")
    st.write(df.head())
    generate_plots(df)
    st.link_button("Churn Prediction", "http://localhost:3000/")
else:
    st.write("Failed to fetch data. Please check the URL and try again.")
        