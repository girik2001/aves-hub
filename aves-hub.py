import streamlit as st

home_page = st.Page("home.py", title="Ave's Hub Home", icon='')
tax_invoice_challan = st.Page("python_projects/tax_invoice_app.py", title='Tax Invoice Application', icon='')

app = st.navigation(
    {   
        "Home": [home_page],
        "Python Projects": [tax_invoice_challan],
    }
)

app.run()