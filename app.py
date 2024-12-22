import app as st
import pandas as pd 
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

"""
data = pd.read_excel("german_credit_data.csv")
st.set_pages_config(layout = "wide")
st.markdown('')"""
col1,col2  = st.columns([0.1,0.9])
with col1:
    box_date = str(datetime.date.now().strftime("%d %B %Y"))
    st.write(f"last updated by : \n {box_date}")