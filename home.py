import streamlit as st
import pandas

user_name="Chris Harris"
user_introduction=f"""Hello! I am {user_name}, a professional Platform Engineer based in Manchester, England. I specialize in Developer Expierence, User Journeys and Cloud Technology.<br><br>
My passion lies in understanding the unique needs of my clients and delivering tailored solutions that exceed expectations.<br><br>
Collaborating with diverse teams and working on various challenging projects has shaped my expertise. Whether it's a small-scale project or a comprehensive business solution, I believe in using the power of creativity and technology to make a real difference.<br>
"""

st.set_page_config(page_title="Harris Showcase", page_icon="./images/icon.ico", layout="wide")

###################

col1, col2 = st.columns([2, 2], gap="medium")
with col1:  
   container1 = st.container()
   container1.image("./images/rick_wink2.jpeg", use_column_width="auto")

with col2:
   container2 = st.container()
   container2.header(user_name)
   container2.write(user_introduction, unsafe_allow_html=True)

page_info = "Below you can find some of the applications I have built using Python. Feel free to contact me!"
st.info(page_info)

######################

data_frame = pandas.read_csv("data.csv", sep=";")

col3, space_col, col4 = st.columns([2, 0.25, 2])
with col3:
   for index,row in data_frame[:10].iterrows():
      st.header(row["title"])
      st.write(row["description"])
      # st.image(image=f"""./images/{row["image"]}""", width=500)
      st.image(image=f"./images/{row['image']}", use_column_width="auto")
      st.write(f"[Source Code](%s)" % row["url"])

with col4:
   for index,row in data_frame[10:].iterrows():
      st.header(row["title"])
      st.write(row["description"])
      st.image(image=f"./images/{row['image']}", use_column_width="auto")
      st.write(f"[Source Code](%s)" % row["url"])
   