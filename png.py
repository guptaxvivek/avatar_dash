import streamlit as st

st.title("Tiktok Stats")

data_dict = {
    "Likes": 3265,
    "Saves": 3265,
    "Comments": 2850,
    "Posts": 31,
    "Follows": 2965
}

cols = st.columns(len(data_dict))

i = 0
for data in data_dict:
    with cols[i]:
        st.metric(data, data_dict[data])
    i += 1
