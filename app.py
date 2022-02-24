import pandas as pd
import numpy as np 
import streamlit as st
import streamlit_authenticator as stauth
from chrome_reviews.chrome_Reviews import reviews_tag

names = ['Biswajit']
usernames = ['rb']
passwords = ['123']
key='a'
cookie='b'

st.title("Check the Records where there is No Match with Text & Rating")
hashed_passwords = stauth.hasher(passwords).generate()
authenticator = stauth.authenticate(names,usernames,hashed_passwords,cookie,key,cookie_expiry_days=0)
name, authentication_status = authenticator.login('Login','main')
st.write(authentication_status)
if authentication_status:
   st.write('Welcome *%s*' % (name))
   data_file = st.file_uploader("Upload CSV",type=["csv"])
   if data_file is not None: 
      file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
      st.write(file_details)
      df = pd.read_csv(data_file)
      df_res=reviews_tag(df)
      st.dataframe(df_res)
elif authentication_status == False:
     st.error('Username/password is incorrect')
elif authentication_status == None:
     st.warning('Please enter your username and password')

