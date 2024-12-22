import streamlit as st
import pandas as pd 
import datetime
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv('german_credit_data.csv')
st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:irem;}</style>',unsafe_allow_html=True)
image = Image.open('bagging_train.png')

col1, col2 = st.columns([0.01,0.09]) # creation de colonnes 

with col1:
    st.image(image,width=100)
    
htlm_title = """
<style>
    .title-test {
    font-wight : bold;
    padding : 5px;
    border-radius:6px
    }
    </style>
    <center><h1> class = "title-test"> Tableau pour identifier les clients en risque de credit</h1></center>"""
with col2:
    st.markdown(htlm_title,unsafe_allow_html=True)

col3,col4,col5 = st.columns([0.1,0.45,0.45])

#cat_cols = [col for col in data.columns if data[col].dtypes == 'O'] # selection des colonnes de types objets

with col3:
    box_t_date = str(datetime.datetime.now().strftime('%d %B %Y'))
    st.write(f'Mis a jour : \n {box_t_date}')
    
with col4:
    fig = px.bar(data,x= 'Risk',y ="Housing" ,labels="risque f(housing)",
                 title="variation",hover_data=["Risk"],template="gridon",
                 height=500)
    st.plotly_chart(fig,use_container_width=True)
