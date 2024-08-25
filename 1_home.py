import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    #df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)']>0]
    df_data = df_data.sort_values('Overall', ascending=False)
    df_data.set_index('Name', inplace=True)
    st.session_state['data'] = df_data
else:
    df_data = st.session_state['data']

st.set_page_config(
    layout='wide'
)

st.markdown('# FIFA23 OFFICIAL DATASET!')
st.sidebar.markdown('Desenvolvido por [EACosta](https://www.linkedin.com/in/costa-everton/)')

btn = st.button('Acesse os dados no Kaggle')
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data?select=CLEAN_FIFA23_official_data.csv')

st.markdown(
    '''
    The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. With over 17,000 records, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.
    '''
)

df_data