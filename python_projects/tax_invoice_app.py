import streamlit as st
from python_projects.tax_invoice_pages.register_company import register_company_page
from python_projects.tax_invoice_pages.login_page import login_page

if 'tax_invoice_app_page' not in st.session_state:
    st.session_state['tax_invoice_app_page'] = ''

def register_company_btn_clicked():
    st.session_state['tax_invoice_app_page'] = 'register_company_page'

def login_btn_clicked():
    st.session_state['tax_invoice_app_page'] = 'login_page'

col1, col2 = st.columns([1,1])
with col1:
    register_company_btn = st.button('Register Company', key='register_page', use_container_width=True, on_click=register_company_btn_clicked)
with col2:
    login_btn = st.button('Login', use_container_width=True, on_click=login_btn_clicked)

if st.session_state['tax_invoice_app_page'] == 'register_company_page':
    register_company_page()

if st.session_state['tax_invoice_app_page'] == 'login_page':
    login_page()