import streamlit as st
import data_mgmt 

df = data_mgmt.df #gets the dataframe and data that was read in data_mgmt.py

st.title("Vehicle Dynamics Data Dashboard")
st.dataframe(df)

vehicle = st.sidebar.selectbox(
    "Vehicle Type", df["VehicleType"].unique()
)

profile = st.sidebar.selectbox(
    "Profile Type", df["ProfileType"].unique()
)

filtered = df[
    (df["VehicleType"] == vehicle) &
    (df["ProfileType"] == profile)
]

st.subheader("Filtered Data")
st.dataframe(filtered)

st.subheader("Speed vs Time")
st.line_chart(filtered, x="Time", y="Speed")