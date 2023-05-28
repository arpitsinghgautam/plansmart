from auth0_component import login_button
import streamlit as st

clientId = "dvRDDJds6nepPy5HlAMyAYbd6sbwgcwE"
domain = "dev-gia30i7t2e5omi3f.us.auth0.com"

user_info = login_button(clientId, domain = domain)
st.write(user_info)