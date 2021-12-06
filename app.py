import streamlit as st
import helper

st.image("https://images.unsplash.com/photo-1581833971358-2c8b550f87b3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format")
st.title("Anime Recommender System") 


selected_anime_name = st.selectbox("Enter The Name of the Anime", options = helper.fetch_data_for_options())

if st.button("Recommend"):
    movie_name, recommend_list, recommend_poster_list = helper.recommend(selected_anime_name)
    st.write(movie_name)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")