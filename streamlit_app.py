import streamlit as st
st.text('Hello worldhhh')
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
st.text('Hello world')
st.plotly_chart(fig)
