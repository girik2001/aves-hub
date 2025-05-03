import streamlit as st
from python_projects.tax_invoice_pages.tax_invoice_app_data import CompanyData

if 'company_data' not in st.session_state:
    st.session_state['company_data'] = CompanyData

def register_company_form_button_clicked(company_name, company_address, company_phone_number, company_gst_number, user_name, password):
    st.session_state['company_data'] = CompanyData(
        company_name=company_name, 
        company_address=company_address, 
        company_ph_no=company_phone_number, 
        company_gst_no=company_gst_number,
        owner_name = user_name, 
        creds = password)
    st.session_state['tax_invoice_app_page'] = 'login_page'
    st.toast('Registration Successful. Please proceed to login...')

def register_company_page():

    with st.container(border=True):
        col1, col2 = st.columns([1,2])
        with col1:
            st.write('<p style="margin: 27px 0px 0px 0px; font-weight:bold; font-size:24px; text-align:right">Company Name: </p>', unsafe_allow_html=True)
            st.write('<p style="margin: 47px 0px 0px 0px; font-weight:bold; font-size:24px; text-align:right">Address: </p>', unsafe_allow_html=True)
            st.write('<p style="margin: 47px 0px 0px 0px; font-weight:bold; font-size:24px; text-align:right">Ph. No.:</p>', unsafe_allow_html=True)
            st.write('<p style="margin: 45px 0px 0px 0px; font-weight:bold; font-size:24px; text-align:right">GST No.:</p>', unsafe_allow_html=True)
            st.write('<p style="margin: 45px 0px 0px 0px; font-weight:bold; font-size:24px; text-align:right">User Name:</p>', unsafe_allow_html=True)
            st.write('<p style="margin: 45px 0px 47px 0px; font-weight:bold; font-size:24px; text-align:right">Password:</p>', unsafe_allow_html=True)
        with col2:
            company_name = st.text_input('Company Name', type='default', key='company_name_register', placeholder='Company Name here...', label_visibility='hidden')
            company_address = st.text_input('Company Address', type='default', key='address_register', placeholder='Address here...', label_visibility='hidden')
            company_phone_number = st.text_input('Company Ph. No.', type='default', key='ph_number_register', placeholder='Phone Number here...', label_visibility='hidden')
            company_gst_number = st.text_input('Company GST No.', type='default', key='gst_number_register', placeholder='GST Number here...', label_visibility='hidden')
            user_name = st.text_input('Company GST No.', type='default', key='username_register', placeholder='username', label_visibility='hidden')
            password = st.text_input('Company GST No.', type='password', key='password_register', placeholder='password', label_visibility='hidden')
    
        st.button("Register", key='register', on_click=register_company_form_button_clicked, args=(company_name, company_address, company_phone_number, company_gst_number, user_name, password), use_container_width=True, type='primary')