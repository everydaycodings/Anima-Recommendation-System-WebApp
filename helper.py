import pandas as pd
import pickle
import numpy as np
from pandas.io import api
import streamlit as st
import requests
import json

@st.cache(allow_output_mutation=True)
def load_model():
    data = pd.read_csv("data/anime.csv")
    model = pickle.load(open("model/model.pkl", 'rb'))
    piviot_table = pickle.load(open("model/piviot_table.pkl", 'rb'))
    return data, model, piviot_table

data, model, piviot_table = load_model()

def fetch_data_for_options():

    options = data["Name"].values
    return options


def api_fetching(selected_anime):
    
    anime_id = np.where(data.Name == selected_anime)[0][0]
    print(anime_id)
    base_url = "https://api.jikan.moe/v3/anime/{}".format(anime_id)

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.io)" 
    }
    print(base_url)
    payload = ""

    response = requests.request("GET", base_url, data=payload,  headers=headersList).text
    json_response = json.loads(response)

    url = json_response["url"]
    image_url = json_response["image_url"]

    return image_url




def recommend(movie_name):

    anime_id = anime_id  = np.where(piviot_table.index == movie_name)[0][0]

    query = piviot_table.iloc[anime_id, :].values.reshape(1, -1)
    distance, suggestions = model.kneighbors(query, n_neighbors=6)

    recommend_list = []
    recommend_poster_list = []
    print(recommend_poster_list)

    for i in range(0, len(distance.flatten())):
        if i == 0:
            movie_name ='Recommendations for {0}:\n'.format(piviot_table.index[anime_id])
        else:
            recommend_list.append('{0}: {1}'.format(i, piviot_table.index[suggestions.flatten()[i]]))
            recommend_poster_list.append(api_fetching(piviot_table.index[suggestions.flatten()[i]]))
            print(piviot_table.index[suggestions.flatten()[i]])

    return movie_name, recommend_list, recommend_poster_list
