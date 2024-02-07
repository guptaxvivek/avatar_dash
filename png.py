import streamlit as st

st.title("Tiktok Stats Until Now")

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

st.title("G - Stats")
g_dict = {
    "Likes": 8459,
    "Saves": 8459,
    "Comments": 1108,
    "Posts": 328,
    "Follows": 0
}

cols = st.columns(len(g_dict))

i = 0
for data in g_dict:
    with cols[i]:
        st.metric(data, g_dict[data])
    i += 1
