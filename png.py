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
    "Likes": 4576,
    "Saves": 4576,
    "Comments": 708,
    "Posts": 78,
    "Follows": 0
}

cols = st.columns(len(g_dict))

i = 0
for data in g_dict:
    with cols[i]:
        st.metric(data, g_dict[data])
    i += 1

st.title("P - Stats")
p_dict = {
    "Likes": 43,
    "Saves": 43,
    "Comments": 43,
    "Posts": 10,
    "Follows": 0
}

cols = st.columns(len(p_dict))

i = 0
for data in p_dict:
    with cols[i]:
        st.metric(data, p_dict[data])
    i += 1
