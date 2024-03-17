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

image=Image.open('img.png')

# Streamlit Function For Building Button & app.

def main():
    st.image(image,width=650)
    st.title('Yield Crop Prediction')
    html_temp='''
    <div style='background-color:red; padding:12px'>
    <h1 style='color:  #000000; text-align: center;'>Yield Crop Prediction Machine Learning Model</h1>
    </div>
    <h2 style='color:  red; text-align: center;'>Please Enter Input</h2>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)
    country= st.selectbox("Type or Select a Country from the Dropdown.",df_main['area'].unique()) 
    crop= st.selectbox("Type or Select a Crop from the Dropdown.",df_main['item'].unique()) 
    average_rainfall=st.number_input('Enter Average Rainfall (mm-per-year).',value=None)
    presticides=st.number_input('Enter Pesticides per Tonnes Use (tonnes of active ingredients).',value=None)
    avg_temp=st.number_input('Enter Average Temperature (degree celcius).',value=None)
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
    result=(int(((predict[0]/100)*2.47105) * 100) / 100)
    return (f"The Production of Crop Yields:- {result} quintel/acers yield Production. "
            f"That means 1 acers of land produce {result} quintel of yield crop. It's all depend on different Parameter like average rainfall, average temperature, soil and many more.")


if __name__=='__main__':
    main()


