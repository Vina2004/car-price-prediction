import streamlit as st
import pandas  as pd
import pickle as pkl
import numpy as np


st.title("Car Price Prediction Project")
df= pd.read_csv("cleaned_data.csv")
import os
import pickle as pkl

# Fix the path issue
file_path = os.path.join(os.path.dirname(__file__), "car-price-predictor.pkl")
pipe = pkl.load(open(file_path, "rb"))




companies =sorted(df["company"].unique())
name =sorted(df["name"].unique())
fuel_type =sorted(df["fuel_type"].unique())


company=st.selectbox("Select company",companies)
name=st.selectbox("Select name",name)
year=st.number_input("Enter year",min_value=1900,max_value=2025,value=2020,step=1)
kms_driven=st.number_input("Enter kms_driven",min_value=10000,value=50000,step=5000)
fuel_type=st.selectbox("select fuel type", fuel_type)


if st.button("Predict Price"):
    st.write("Your company:",company)
    st.write("Your name:",name)
    st.write("Your year:",str(year))
    st.write("Your kms_driven:",str(kms_driven))
    st.write("Your fuel_type:",fuel_type)


    columns = ['company', 'name', 'year', 'kms_driven', 'fuel_type']
    data = [[company, name, year, kms_driven, fuel_type]]
    myinput=pd.DataFrame(data,columns=columns)
    price = pipe.predict(myinput)

    st.success("Predicted price: ₹" + str(round(float(price[0]))))