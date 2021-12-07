import streamlit as st
import helper

st.image("https://images.unsplash.com/photo-1581833971358-2c8b550f87b3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format")
st.title("Anime Recommender System") 


selected_anime_name = st.selectbox("Enter The Name of the Anime", options = helper.fetch_data_for_options())

if st.button("Recommend"):
    movie_name, recommend_list, recommend_poster_list = helper.recommend(selected_anime_name)
    st.header(movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader(recommend_list[0])
        st.image(recommend_poster_list[0])

    with col2:
        st.subheader(recommend_list[1])
        st.image(recommend_poster_list[1])

    with col3:
        st.subheader(recommend_list[2])
        st.image(recommend_poster_list[2])
    
    with col4:
        st.subheader(recommend_list[3])
        st.image(recommend_poster_list[3])
    
    with col5:
        st.subheader(recommend_list[4])
        st.image(recommend_poster_list[4])