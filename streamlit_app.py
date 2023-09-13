import streamlit as st
import pandas as pd

# from model import mape_metrics
from annotated_text import annotated_text
from timemodel import get_prediction
# from weekdatamodel import get_weekly

# df = pd.read_csv('train.csv')



# new_data = df.iloc[:,[1,4]]

# new_data['date'] = pd.DatetimeIndex(new_data['date'])


# new_data.set_index('date',inplace=True)


# monthly_data = new_data.resample('M').sum()


num = st.sidebar.slider('Select the time period',0,3 )

st.title('Demand Forecasting')


# genre = st.radio(
#     "Select the option",
#     ["Yearly", "Half-Yearly", "Weekly"])






# st.line_chart(get_prediction(num))

# st.set_page_config(layout="wide")

with st.empty():
    col1, col2 = st.columns(2)
    with col1:
        st.text('Yearly forecasting')
        st.line_chart(get_prediction(num)[0], height=250,color='#525FE1',use_container_width=True)
    with col2:
        st.text('Half Yearly forecasting')
        st.line_chart(get_prediction(num)[1], height=250,color='#FF2171',use_container_width=True)
