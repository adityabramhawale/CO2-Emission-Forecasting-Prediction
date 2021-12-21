import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from statsmodels.tsa.arima.model import ARIMA

st.title("CO2 Emission Forecaster")
st.image("co2 (1).jpg")

st.write("This forecaster is bulit on ARIMA model which considers the previous CO2 emissions, and try to forecast the values of CO2 emission for coming years. This forecast will be helpful to understand what can be the estimated emision levels, and if estimated levels are high, organization can undertake preventive measures to keep them below the standards provided by Government")

try:

    df = pd.read_excel("CO2 dataset.xlsx")
    df1 = df.drop("Year", axis=1)
    index = pd.date_range(start="1800", end="2015", freq="A-DEC")
    df1.set_index(index, inplace=True)
    model_arima_final = ARIMA(df1, order = (10, 1, 15)).fit()

    sel_list = ["Select method", "Table", "Graph"]

    year = st.sidebar.number_input("Select the number of year to see the previous data (Between 1 to 215)",min_value = 1, max_value = 215)
    method1 = st.sidebar.selectbox("Select Visualization Method", sel_list)
    button1 = st.sidebar.button (label="show")
    if button1:
        if method1 =="Table":
            st.header("Previous year's data")
            st.table(df1.head(year))
        elif method1 == "Select method":
            st.header("Please select the method")
        else:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.plot (df1.head(year), label='Historic data', color="green")
            plt.title('Previous data')
            plt.xlabel("Year")
            plt.ylabel("CO2 emission levels")
            st.pyplot()

    number = st.sidebar.number_input('Enter the number of years to be forecasted (Between 1 to 100)', min_value = 1, max_value = 100)
    method2 = st.sidebar.selectbox("Result Visualization Method", sel_list)
    button2= st.sidebar.button(label="submit")
    
    
    if button2 :
        forecast =model_arima_final.forecast(number)

        if method2 =="Table":
            st.header("Forecast values are")
            st.table(forecast)
        elif method2 == "Select method":
            st.header("Please select the method")
        else:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.plot(df1, label='Historic data', color="green")
            plt.plot(forecast, label='forecasted data', color="Red")
            plt.title('Forecast data')
            plt.xlabel("Year")
            plt.ylabel("CO2 emission levels")
            plt.legend(loc='upper left', fontsize=8)
            st.pyplot()

except KeyError:
    pass