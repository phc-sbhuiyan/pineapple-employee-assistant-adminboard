import streamlit as st
import os
from trulens.core import TruSession
from base import rag # a rag app with a query method
from base import tru_rag # a rag app wrapped by trulens
from trulens.dashboard import streamlit as trulens_st
from trulens.dashboard.Leaderboard import render_leaderboard

session = TruSession()

def generate_and_log_response(input_text):
    with tru_rag as recording:
        response = rag.query(input_text)
    record = recording.get()
    return record, response

with st.form("my_form"):
    text = st.text_area("Enter text:", "How do I launch a streamlit app?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        record, response = generate_and_log_response(text)
        st.info(response)
        trulens_st.trulens_feedback(record=record)
        trulens_st.trulens_trace(record=record)

render_leaderboard()
