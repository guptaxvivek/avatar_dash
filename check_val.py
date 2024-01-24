import pickle
import streamlit as st


st.title("Tiktok Stats")
# Tiktok
# likes = 
comments = 1395
follow = 367
# Instagram 
ig_likes = 65
ig_comments = 185
ig_follow = 72
# Facebook
fb_comments = 302
fb_likes = 294
fb_shares = 294
#  pickle.load(open("dash\\tk-comments.pkl",'rb'))['successful']
col1, col2 = st.columns(2)
col1.metric("Comments", comments)
# col2.metric("Likes", likes)
col2.metric("Follow", follow)

st.title("Instagram Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Comments", ig_comments)
col2.metric("Likes", ig_likes)
col3.metric("Follow", ig_follow)


st.title("Facebook Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Comments", fb_comments)
col2.metric("Likes", fb_likes)
col3.metric("Shares", fb_shares)