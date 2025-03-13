import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard") 

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df =pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data summary")
    st.write(df.describe())


    st.subheader("Filter data")
    columns = df.columns.tolist()
    selected_columns =st.selectbox("select columns to list by " , columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("select value",unique_values)
    

    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)

    st.subheader("plot data")
    x_column = st.selectbox("select x-axis", columns)
    y_column = st.selectbox("select y-axis", columns)
     
    if st.button("Generate plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("waiting for file upload....") 

    

