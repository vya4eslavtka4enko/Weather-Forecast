import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:  ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help='Select the number of forecasted days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')


def get_data(days):
    dates = ['2022-25-10', '2022-26-10', '2022-27-10']
    temperature = [10, 5, 12]
    temperature=[days * i for i in temperature]
    return dates,temperature



figure = px.line(x=get_data(days)[0], y=get_data(days)[1], labels={'X': 'Date', 'Y': 'Temperature'})
st.plotly_chart(figure)
