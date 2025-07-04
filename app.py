
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("facebook_live_data.csv")

st.title("📊 Facebook Live Post Engagement Dashboard")

# Sidebar filters
st.sidebar.header("Filter by Post Type")
post_types = ["Photo", "Status", "Video", "Link"]
selected_types = []

for p in post_types:
    col_name = f"status_type_{p.lower()}"
    if col_name in df.columns:
        if st.sidebar.checkbox(p, value=True):
            selected_types.append(col_name)

# Filter the data
if selected_types:
    mask = df[selected_types].sum(axis=1) > 0
    filtered_df = df[mask]
else:
    filtered_df = df.copy()

# Layout
st.subheader("Engagement Overview")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(filtered_df, y="num_reactions", title="Total Reactions")
    st.plotly_chart(fig1)

with col2:
    fig2 = px.bar(filtered_df, y="num_comments", title="Total Comments")
    st.plotly_chart(fig2)

st.subheader("Reaction Breakdown")

fig3 = px.box(filtered_df, y=["num_likes", "num_loves", "num_wows", "num_hahas", "num_sads", "num_angrys"],
              title="Distribution of Reactions")
st.plotly_chart(fig3)

st.markdown("Built with ❤️ using Streamlit and Plotly")
