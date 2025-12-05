# You are given lots of starting functions so you don't need to rewrite most of
# the logic from your previous project.
import streamlit as st
from datetime import datetime
from db_setup_and_helpers import (
    clean_phone_number,
    get_customer_if_exists,
    get_all_stylists,
    get_index_of_most_recent_stylist,
    pretend_to_get_a_haircut,
    hairstyles_dict,
    Appointment,
    Customer,
)

# Add "current_view" to session_state if it isn't already there
if 'current_view' not in st.session_state:
    st.session_state['current_view'] = 'enter_phone_number'

# =======================
# ENTER PHONE NUMBER VIEW
# =======================
# Check session_state for 'enter_phone_number'. If True, then display this view.
if st.session_state.get('current_view') == 'enter_phone_number':
    pass # replace with the enter phone number view logic

# =================
# NEW CUSTOMER VIEW
# =================
elif st.session_state.get('current_view') == 'new_customer':
    pass # replace with the new customer view logic

# ===================
# SELECT OPTIONS VIEW
# ===================
elif st.session_state.get('current_view') == 'select_options':
    pass # replace with select options view logic

# ====================
# GETTING HAIRCUT VIEW
# ====================
# this one is just for fun, so here it is already written
elif st.session_state.get('current_view') == 'getting_haircut':
    pretend_to_get_a_haircut()
    st.session_state['current_view'] = 'check_out'
    st.rerun()

# ==============
# CHECK OUT VIEW
# ==============
elif st.session_state.get('current_view') == 'check_out':
    pass # replace with check out view logic