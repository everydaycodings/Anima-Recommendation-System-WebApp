# User-Based-Movie-Recommender-System | Collaborative-Method

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-sreamlit-red)
![API](https://img.shields.io/badge/API-myanimelist-fcba03)


**Collaborative filtering systems** use the actions of users to recommend other movies. In general, they can either be user-based or item-based. Item based approach is usually preferred over **user-based approach.** User-based approach is often harder to scale because of the dynamic nature of users, whereas items usually don’t change much, and item based approach often can be computed offline and served without constantly re-training.


Check out the live demo: https://mrswsa.herokuapp.com/

Link to youtube demo: https://www.youtube.com/watch?v=dhVePtyECFw

# Note

> #### Use this URL - [Click Me](https://github.com/everydaycodings/Anima-Recommendation-System-WebApp#source-to-the-pre-trained-modles-and-datasets) - in case if you are faccing any problem with th eweb app or source code.



Source Code: [github link](https://github.com/everydaycodings/Anima-Recommendation-System-WebApp)


## How to get the API key?

Actually, you don't have to get any API Key for **myanimelist.net** as it is free and even You don't have to Get an Account to use API.

## How to run the project?

1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt](https://github.com/everydaycodings/Anima-Recommendation-System-WebApp/blob/master/requirements.txt) file with the command `pip3 install -r requirements.txt`
3. Download the Data from the Given Link Below. And create a data and model folder in the project home directory.
4. Past the CSV File inside data folder and .pkl extension file to your model folder
4. Open your terminal/command prompt from your project directory and run the file `app.py` by executing the command `streamlit run app.py`.
5. You will be automatically redirected the your localhost in brower where you can see you WebApp in live.

## Architecture of your Project Home Directory

![IMG-20210306-WA0012](https://raw.githubusercontent.com/everydaycodings/Anima-Recommendation-System-WebApp/master/images/1.png)


## Source to the Pre-trained Modles and Datasets
### Sources of the datasets 
1) Original source: [Download Data](https://www.kaggle.com/hernan4444/anime-recommendation-database-2020), in This datasets there are arround 109Million records.

### Source to the Trained Model
If you don't want to download dataset and train it then i have uploaded the prebuild models, You can use that.
1) If you wat the **smaller** version of the model, THen i have trained **10million** records and uploaded it you can download it by [clicking here](https://mega.nz/file/FKoRVI6K#hbHMdIPV8keuAmb0Nhhu9tCjkgn7Q2U2zydAFD2dloY)
2) If you wat the **medium** version of the model, THen i have trained **20million** records and uploaded it you can download it by [clicking here](https://mega.nz/file/ZSwzQKLR#Aj4wP6nKXUzfeudeXfUkw3vi3thgbS9W1GbI682epNM)
3) If you wat the **large** version of the model, THen i have trained **50million** records and uploaded it you can download it by [clicking here](https://mega.nz/file/tagAgSaT#1vQ88TQDJfcIL6iZ6pwVUG3IYVMdOYQWRzSgO3utEF4)

### Note: The WebApp uses 10Million records so you can check the accuracy of 10Million records model by using the WebApp.
### Note: I couldn't train all 109Million records because of my pc limitation so I don't have a model for 109million records.

