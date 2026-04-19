import streamlit as st
import plotly.express as px
import pandas as pd
# This line tells Python: "Go into the src folder, find data_engine.py, and grab the function"
from src.data_engine import generate_poll_data 

# --- 1. SETUP ---
st.set_page_config(page_title="Industry Poll Visualizer", layout="wide")

# --- 2. DATA LOADING (Calling the logic from src/) ---
df = generate_poll_data()

# --- 3. SIDEBAR FILTERS ---
st.sidebar.header("📊 Filter Dashboard")
selected_region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
filtered_df = df[df['Region'].isin(selected_region)]

# --- 4. DASHBOARD HEADER & METRICS ---
st.title("🏆 Industry Poll Results Visualizer")
st.markdown("Modular Project Structure: Logic (src/) + UI (app.py)")

m1, m2, m3 = st.columns(3)
m1.metric("Total Responses", len(filtered_df))
m2.metric("Market Leader", filtered_df['Vote'].value_counts().idxmax())
m3.metric("Avg. Satisfaction", f"{round(filtered_df['Satisfaction'].mean(), 1)} / 5.0")

st.divider()

# --- 5. VISUALIZATIONS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Market Share %")
    vote_counts = filtered_df['Vote'].value_counts().reset_index()
    fig_pie = px.pie(vote_counts, values='count', names='Vote', hole=0.5,
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("Regional Preference Breakdown")
    fig_bar = px.histogram(filtered_df, x='Region', color='Vote', barmode='group',
                           color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("Demographic Deep-Dive: Age Group vs. Choice")
age_pivot = filtered_df.groupby(['Age_Group', 'Vote']).size().reset_index(name='Count')
fig_heat = px.density_heatmap(age_pivot, x='Age_Group', y='Vote', z='Count', 
                              text_auto=True, color_continuous_scale='Viridis')
st.plotly_chart(fig_heat, use_container_width=True)