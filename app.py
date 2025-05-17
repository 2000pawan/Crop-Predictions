# Import Important Library.

import joblib
import streamlit as st 
from PIL import Image
import pandas as pd


# Load Model & Scaler & Polynomial Features

model=joblib.load('model.pkl')
sc=joblib.load('sc.pkl')
pf=joblib.load('pf.pkl')

# load dataset

df_final=pd.read_csv('test.csv')
df_main=pd.read_csv('main.csv')

# Load Image

image=Image.open('img.jpeg')

# Streamlit Function For Building Button & app.

def main():
    st.image(image,width=650)
    st.title('💠AI Crop Prediction Model💠')
    html_temp='''
    <div style='background-color:red; padding:12px'>
    <h1 style='color:  #000000; text-align: center;'>Crop Prediction AI Model</h1>
    <h2 style='color: #000000; text-align: center;'> We Use Three Nationwide Parameter to Predict Crop :-</h2>
    <h3 style='color: #000000;text-align: left; font-size: 25px;'>💠 The Total Rainfall (mm per year during the crop’s season)</h3>
    <h3 style='color: #000000;text-align: left; font-size: 25px;'>💠 The Total Pesticides used (all cultivated hectares land) </h3>
    <h3 style='color: #000000;text-align: left; font-size: 25px;'>💠 The Average Temperature (°C throughout that season)</h3>
    <h2 style='color: #000000; text-align: center;'> For example, in India’s Rice Cultivation:</h2>
    <h3 style='color: #000000;text-align: left; font-size: 25px;'>💠 Total Cultivated area: ≈ 47.6 million hacter (≈ 117.6 million acres)</h3>
    <h3 style='color: #000000;text-align: left; font-size: 25px;'>💠 Total Pesticide use: ≈ 61,347 tonnes all area (≈ 0.52 kg per acre) </h3>
    <h3 style='color: #000000;text-align: left; font-size: 25px;'>💠 Average Rainfall: (annual in millimeter during rice growth)</h3> 
    <h3 style='color: #000000;text-align: left; font-size: 25px;'>💠 Average Temperature: (average temp in °C during rice season)</h3>
    <h4 style= 'color: #000000; text-align: left; font-size: 20px;'> 👉 “Customize this model with your country’s crop type, total pesticide used to cultivated all over area whaere this crop grow, average rainfaal, average temperature data to generate accurate yield insights.”</h4>
    </div>
    <p style= "color: red;text-align: right; font-size: 30px;">
    &copy; 2025 Developed by Pawan Yadav. All rights reserved.</p>
    <h2 style='color:  red; text-align: center;'>Please Enter Input</h2>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)
    country= st.selectbox("Type or Select a Country from the Dropdown.",df_main['area'].unique()) 
    crop= st.selectbox("Type or Select a Crop from the Dropdown.",df_main['item'].unique()) 
    average_rainfall=st.number_input('Enter Average Rainfall (in mm per year during the crop’s cultivation period in the selected country).',value=None)
    presticides=st.number_input('Enter pesticide usage (in tonnes, applied over the entire area where this crop is grown).',value=None)
    avg_temp=st.number_input(" Enter Average Temperature (°C during the crop's growing season).",value=None)
    input=[country,crop,average_rainfall,presticides,avg_temp]
    result=''
    if st.button('Predict',''):
        result=prediction(input)
    temp='''
     <div style='background-color:navy; padding:8px'>
     <h1 style='color: gold  ; text-align: center;'>{}</h1>
     </div>
     '''.format(result)
    st.markdown(temp,unsafe_allow_html=True)
    
    
    

# Prediction Function to predict from model.
# Albania	Soybeans	1990	7000	1485.0	121.00	16.37
# input=['Albania','Soybeans',1485.0,121.00,16.37]
def update_columns(df, true_columns):
    df[true_columns] = True
    other_columns = df.columns.difference(true_columns)
    df[other_columns] = False
    return df
def prediction(input):
    categorical_col=input[:2]
    input_df=pd.DataFrame({'average_rainfall':input[2],'presticides_tonnes':input[3],'avg_temp':input[4]},index=[0])
    input_df1=df_final.head(1)
    input_df1=input_df1.iloc[:,3:]
    true_columns = [f'Country_{categorical_col[0]}',f'Item_{categorical_col[1]}']
    input_df2= update_columns(input_df1, true_columns)
    final_df=pd.concat([input_df,input_df2],axis=1)
    final_df=final_df.values
    test_input=sc.transform(final_df)
    test_input1=pf.transform(test_input)
    predict=model.predict(test_input1)
    # result=predict[0]
    result = round(((predict[0]*0.1)/100)/2.47105, 2)
    return (f"The production of {true_columns[1].split('_')[1]} crop in {true_columns[0].split('_')[1]} is {result} quintals per acre. "
 f"This means that one acre of land produces {result} quintals of {true_columns[1].split('_')[1]}. "
 f"The yield depends on various parameters like average rainfall, average temperature, soil quality, and many more.")


if __name__=='__main__':
    main()


