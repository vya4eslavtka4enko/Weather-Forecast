import streamlit as st
import plotly.express as px
from backend import get_data
st.set_page_config(layout="wide")
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:  ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help='Select the number of forecasted days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')


if place:
    #get the temperature / sky data
    try:
        filtered_data = get_data(place,days)
        if option == "Temperature":
            temperature = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            #Create a temperature plot
            figure = px.line(x=dates, y=temperature, labels={'X': 'Date', 'Y': 'Temperature (C)'})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear":"image/clear.png","Clouds":"image/cloud.png",
                      "Rain":"image/rain.png","Snow":"image/snow.png"}
            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_condition]
            print(image_paths)
            st.image(image_paths,width = 180)
    except KeyError:
        st.subheader(f"'{place}'Not correct city ")