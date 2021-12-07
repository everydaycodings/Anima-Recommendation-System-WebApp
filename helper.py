import pandas as pd
import pickle
import numpy as np
from pandas.io import api
import streamlit as st
import requests
import json

st.set_page_config(
     page_title="Anime Recommender System",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/everydaycodings/Anima-Recommendation-System-WebApp#readme',
         'Report a bug': "https://github.com/everydaycodings/Anima-Recommendation-System-WebApp/issues/new/choose",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)


@st.experimental_memo
def load_data():

    data = pd.read_csv("data/anime_output10m.csv")
    return data

data = load_data()


@st.cache(allow_output_mutation=True)
def load_model():

    model = pickle.load(open("model/model10m.pkl", 'rb'))
    piviot_table = pickle.load(open("model/piviot_table10m.pkl", 'rb'))

    return model, piviot_table

model, piviot_table = load_model()

def fetch_data_for_options():

    options = data["Name"].values

    return options


def api_fetching(selected_anime):
    try:
        anime_id = data[data["Name"] == selected_anime].anime_id.values[0]

        base_url = "https://api.jikan.moe/v3/anime/{}".format(anime_id)

        headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.io)" 
        }

        payload = ""

        response = requests.request("GET", base_url, data=payload,  headers=headersList).text
        json_response = json.loads(response)

        url = json_response["url"]
        image_url = json_response["image_url"]

        return image_url
    except KeyError:
        st.write("Error: Unable to Fetch the Anime details it may be because of the weak internet connection, PLease try again later or inform the error to the admin.")



def api_fetching_url(selected_anime):
    try:
        anime_id = data[data["Name"] == selected_anime].anime_id.values[0]

        base_url = "https://api.jikan.moe/v3/anime/{}".format(anime_id)

        headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.io)" 
        }

        payload = ""

        response = requests.request("GET", base_url, data=payload,  headers=headersList).text
        json_response = json.loads(response)

        url = json_response["url"]
        image_url = json_response["image_url"]

        return url
    except KeyError:
        st.write("Error: Unable to Fetch the Anime details it may be because of the weak internet connection, PLease try again later or inform the error to the admin.")


def recommend(movie_name):
    try:
        anime_id =  np.where(piviot_table.index == movie_name)[0][0]
    
    except IndexError:
        st.error("Error: The Anime which you are Searching for is not in our database, please try out another Anime.")
    
    query = piviot_table.iloc[anime_id, :].values.reshape(1, -1)
    distance, suggestions = model.kneighbors(query, n_neighbors=6)

    recommend_list = []
    recommend_poster_list = []
    recommend_anime_url = []


    for i in range(0, len(distance.flatten())):

        if i == 0:
            movie_name ='Recommendations for {0}:\n'.format(piviot_table.index[anime_id])

        else:
            recommend_list.append('{}'.format(piviot_table.index[suggestions.flatten()[i]]))
            recommend_poster_list.append(api_fetching(piviot_table.index[suggestions.flatten()[i]]))
            recommend_anime_url.append(api_fetching_url(piviot_table.index[suggestions.flatten()[i]]))
        
    return movie_name, recommend_list, recommend_poster_list, recommend_anime_url
    

