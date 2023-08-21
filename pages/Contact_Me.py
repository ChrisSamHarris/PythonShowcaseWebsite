import streamlit as st
import re
from email_sender import contact_me_email


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

email_correct = False
message_valid = False

st.header("Contact Me")

with st.form(key="contact_me"):
    user_email = st.text_input(
        "Your Email Address 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="FabulousUser@example.com",
    )
    if len(user_email) > 0:
      if is_valid_email(user_email):
        email_correct = True
      else:
        st.warning('Invalid email address..', icon="⚠️")
   
    message_input = st.text_area(
        "Your Message",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="Enter your message here...",
    )
    message_warning_placeholder = st.empty()

    submitted = st.form_submit_button("Submit")

    # If submitted and message is empty, show the warning in the placeholder
    if submitted and len(message_input) == 0:
         message_warning_placeholder.warning('Please enter a message!', icon="⚠️")
    else:
         message_valid = True

   
if submitted and email_correct and message_valid:
    submitted_message_placeholder = st.empty()
    submitted_message_placeholder.write('Contact form submitted, please wait for verification...')
    try:
        contact_me_email(contact_email=user_email, message=message_input)
        submitted_message_placeholder.write("Form submitted successfully.")
    except: 
        submitted_message_placeholder.empty()
        st.write("Uanble to submit your request at this time. Please try again in a couple of minutes...")
        st.write("If this issue persists please contact Chris directly through ### X ###")
        
