import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
   page_title="H8-Milestone1",
   page_icon="mjolnir.png",
   layout="centered",
   initial_sidebar_state="expanded",
   menu_items={
       'Get Help': 'https://github.com/nesafadhila',
       'Report a bug': "https://www.google.com/",
       'About': "# This is my First Milestone!"
   }
)

selected = st.sidebar.selectbox('Select Page: ', options=['Homepage','Data Visualization', 'Hypothesis Testing'])


if selected == 'Homepage':
    st.title('WELCOME!')
    st.caption('Hello! This is Nesa aka Annesa Fadhila Damayanti from Batch 11 Hacktive8 Fulltime Data Science.\
        Nice to meet you!')
    df = pd.read_csv('supermarket_sales.csv')
    SM = df.copy()
    if st.checkbox('Show Data'):
        st.subheader('Data')
        st.write(SM)

if selected == 'Data Visualization':
    st.title('DATA VISUALIZATION')
    df = pd.read_csv('supermarket_sales.csv')
    SM = df.copy()
    SM.columns = [column.replace(" ","_") for column in SM.columns]

    ewallet_female = SM[
    (SM['City'] == 'Yangon') &
    (SM['Customer_type'] == 'Member') &
    (SM['Gender'] == 'Female') &
    (SM['Payment'] == 'Ewallet')
    ]

    cash_female = SM[
    (SM['City'] == 'Yangon') &
    (SM['Customer_type'] == 'Member') &
    (SM['Gender'] == 'Female') &
    (SM['Payment'] == 'Cash')
    ]

    ewallet_male = SM[
    (SM['City'] == 'Yangon') &
    (SM['Customer_type'] == 'Member') &
    (SM['Gender'] == 'Male') &
    (SM['Payment'] == 'Ewallet')
    ]

    cash_male = SM[
    (SM['City'] == 'Yangon') &
    (SM['Customer_type'] == 'Member') &
    (SM['Gender'] == 'Male') &
    (SM['Payment'] == 'Cash')
    ]

    if st.checkbox('Female E-Wallet'):
        st.write(ewallet_female)
        fig1, ax1 = plt.subplots()
        ax1.hist(ewallet_female[['Total', 'cogs']])
        st.subheader('Female Customer yang Menggunakan E-Wallet')
        st.pyplot(fig1)

    if st.checkbox('Female Cash'):
        st.write(cash_female)
        fig2, ax2 = plt.subplots()
        ax2.hist(cash_female[['Total', 'cogs']])
        st.subheader('Female Customer yang Menggunakan Cash')
        st.pyplot(fig2)

    if st.checkbox('Male E-Wallet'):
        st.write(ewallet_male)
        fig3, ax3 = plt.subplots()
        ax3.hist(ewallet_male[['Total', 'cogs']])
        st.subheader('Male Customer yang Menggunakan E-Wallet')
        st.pyplot(fig3)

    if st.checkbox('Male Cash'):
        st.write(cash_male)
        fig4, ax4 = plt.subplots()
        ax4.hist(cash_male[['Total', 'cogs']])
        st.subheader('Male Customer yang Menggunakan Cash')
        st.pyplot(fig4)

if selected == 'Hypothesis Testing':
    st.title('HYPOTHESIS TESTING')
    st.write('Total pembelanjaan perempuan yang menggunakan e-wallet dan laki-laki yang menggunakan e-wallet terlihat sedikit perbedaan.\
        Sedangkan total pembelanjaan perempuan yang menggunakan cash dan laki-laki yang menggunakan cash terlihat perbedaan yang agak jauh.')
    st.write('**Hipotesis Pertama**')
    st.write('H0: Total Perempuan yang menggunakan E-Wallet = Total Laki-Laki yang menggunakan E-Wallet')
    st.write('H1: Total Perempuan yang menggunakan E-Wallet != Total Laki-Laki yang menggunakan E-Wallet')

    st.write('**Hipotesis Kedua**')
    st.write('H0: Total Perempuan yang menggunakan Cash = Total Laki-Laki yang menggunakan Cash')
    st.write('H1: Total Perempuan yang menggunakan Cash != Total Laki-Laki yang menggunakan Cash')

    st.write('**Kesimpulan**')
    st.write('Berdasarkan hasil hipotesis tersebut, kami tidak dapat menolak H0. karena nilai P-Value pada kedua hipotesis tersebut lebih besar dari 0.05. \
        Dapat disimpulkan total perempuan yang menggunakan E-Wallet seerta Cash dan total laki-laki yang menggunakan E-Wallet serta Cash adalah sama.')
    