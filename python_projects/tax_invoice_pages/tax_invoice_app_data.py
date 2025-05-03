import streamlit as st

class CompanyData:
    def __init__(self, company_name, company_ph_no, company_address, company_gst_no, owner_name, creds):
        self.company_name = company_name
        self.company_ph_no = company_ph_no
        self.company_address = company_address
        self.company_gst_no = company_gst_no
        self.owner_name = owner_name
        self.creds = creds
    
    def __str__(self):
        return f'''Class CompanyData\n{self.company_name}\n{self.company_address}'''