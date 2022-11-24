#imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import matplotlib.cm as cm
from io import StringIO

st.set_page_config(page_title= 'PR6 eHealth',page_icon=":eyes:",initial_sidebar_state="collapsed",layout="wide",menu_items={
        'About': "# This is a project for visual analytics."
    })

st.title("Creació del dataframe ")



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()

    # Can be used wherever a "file-like" object is accepted:
    data = pd.read_csv(uploaded_file,sep=";")
    df = pd.DataFrame()
    if 'codiUp' in data.columns:
        df['CodiUp']= data['codiUp']
    else: 
        df['CodiUp']=None
    df['Municipi']= data['nomMunicipi']
    df['Codi municipi']= data['codiMunicipi']
    df['Superfície Real Sòl']= data['superficieRealSol']
    df['Estat urbanístic']=data['estatUrbanisticDescription']
    df['Comercialització'] = data['comercialitzacio']
    df['Dret de propietat'] = data['dretPropietat']
    df['Referència cadastral']=None
    df['Ús']=None

    df

    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='readyToUpload.csv',
        mime='text/csv',
    )
   







