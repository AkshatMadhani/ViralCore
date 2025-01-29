import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime

st.set_page_config(page_title="Campaign Performance Dashboard")

st.title("Campaign Performance Dashboard")

st.sidebar.header("Filters")

campaign_name = st.sidebar.text_input("Enter Campaign Name")

start_date = st.sidebar.date_input("Start Date", value=datetime.today())
end_date = st.sidebar.date_input("End Date", value=datetime.today())



platform_filter = st.sidebar.multiselect(
    "Select Platforms:",
    ["Instagram", "Twitter", "YouTube", "Facebook"],
    default=["Instagram","Facebook"]

)

def get_campaign_data():
    return pd.DataFrame({
        "Platform": ["Instagram", "Twitter", "YouTube", "Facebook"],
        "Impressions": [random.randint(5000, 15000) for _ in range(4)],
        "Engagement": [random.randint(1000, 3000) for _ in range(4)],
        "Clicks": [random.randint(100, 500) for _ in range(4)],
        "CTR (%)": [round(random.uniform(2.0, 5.0), 2) for _ in range(4)],
        "ROI (%)": [round(random.uniform(10,100), 2) for _ in range(4)],
    })

campaign_data = get_campaign_data()

filtered_data = campaign_data[campaign_data["Platform"].isin(platform_filter)]

st.markdown(f"###  {campaign_name} (From {start_date} to {end_date})")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Impressions", filtered_data["Impressions"].sum())

with col2:
    st.metric("Total Engagement", filtered_data["Engagement"].sum())

with col3:
    avg_ctr = filtered_data["CTR (%)"].mean()
    st.metric("Average CTR (%)", f"{avg_ctr:.2f}")

with col4:
    avg_roi = filtered_data["ROI (%)"].mean()
    st.metric("Average ROI (%)", f"{avg_roi:.2f}")

st.markdown("### *Platform Performance*")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.bar(filtered_data["Platform"], filtered_data["Engagement"], color=["blue", "green", "red", "purple"])
    ax.set_title("Engagement by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Engagement")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.pie(filtered_data["ROI (%)"], labels=filtered_data["Platform"], autopct="%1.1f%%", colors=["blue", "green", "red", "purple"])
    ax.set_title("ROI Distribution by Platform")
    st.pyplot(fig)

st.markdown("### *Detailed Campaign Data*")
st.dataframe(filtered_data)



