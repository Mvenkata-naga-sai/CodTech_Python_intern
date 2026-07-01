
import streamlit as st
import pandas as pd
import time
import plotly.express as px
from utils.data_generator import generate_data

st.set_page_config(page_title="Real-time Dashboard", layout="wide")

st.title("📊 Real-time Data Dashboard")

refresh_rate = st.sidebar.slider("Refresh Rate (seconds)", 1, 10, 2)
num_points = st.sidebar.slider("Data Points", 10, 100, 50)

chart_placeholder = st.empty()
table_placeholder = st.empty()

data = pd.DataFrame(columns=["time", "value"])

while True:
    new_data = generate_data()
    data = pd.concat([data, new_data]).tail(num_points)

    fig = px.line(data, x="time", y="value", title="Live Data Stream")

    chart_placeholder.plotly_chart(fig, use_container_width=True)
    table_placeholder.dataframe(data)

    time.sleep(refresh_rate)
