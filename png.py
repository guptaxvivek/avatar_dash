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
    "Likes": 1652,
    "Saves": 1652,
    "Comments": 1237,
    "Posts": 0,
    "Follows": 0
}

cols = st.columns(len(g_dict))

i = 0
for data in data_dict:
    with cols[i]:
        st.metric(data, data_dict[data])
    i += 1

st.title("P - Stats")
p_dict = {
    "Likes": 0,
    "Saves": 0,
    "Comments": 0,
    "Posts": 0,
    "Follows": 0
}

cols = st.columns(len(p_dict))

i = 0
for data in p_dict:
    with cols[i]:
        st.metric(data, data_dict[data])
    i += 1
