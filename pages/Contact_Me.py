import streamlit as st

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.header("Contact Me")

with st.form(key="contact_me"):
   user_email = st.text_input(
        "Your Email Address 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="FabulousUser@example.com",
    )
   
   message_input = st.text_area(
        "Your Message",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="Enter your message here...",
    )
   
   submitted = st.form_submit_button("Submit")
   
if submitted:
    try:
        st.write("Form submitted successfully.")
    except: 
        st.write("Uanble to submit your request at this time. Please try again in a couple of minutes...")
        st.write("If this issue persists please contact Chris directly through x")
        
