import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.write("Presentation on USA Housing Dataset")
st.title("Analysis on USA Housing")

df_housing=pd.read_csv("USA_Housing.csv")
st.dataframe(df_housing)
df_housing.head(5)

st.line_chart(data = df_housing, x="Avg. Area Number of Bedrooms", y="Area Population")
