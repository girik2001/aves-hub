import streamlit as st

def login_btn_clicked(username, password):
    if username==password:
        st.toast('login successful')
    else:
        st.toast('invalid password')

def login_page():
    
    with st.container(border=True):
        col1, col2 = st.columns([1,2])
        with col1:
            st.write('<p style="margin: 27px 0px 0px 0px; font-weight:bold; font-size:24px; text-align:right">User Name:</p>', unsafe_allow_html=True)
            st.write('<p style="margin: 45px 0px 47px 0px; font-weight:bold; font-size:24px; text-align:right">Password:</p>', unsafe_allow_html=True)
        with col2:
            user_name = st.text_input('Company GST No.', type='default', key='username_login', placeholder='username', label_visibility='hidden')
            password = st.text_input('Company GST No.', type='password', key='password_login', placeholder='password', label_visibility='hidden')
    
        st.button("Login", key='login', on_click=login_btn_clicked, args=(user_name, password), use_container_width=True, type='primary')