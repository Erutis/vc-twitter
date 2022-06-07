# TLaaS: Thought Leadership as a Service

## Problem Statement

Many fields are now expecting existing and potential employees to have a robust social media presence. However, it can be difficult to come up with what to write about or tweet about. It would be useful if a finance or investment professional could easily generate sample text to use in keeping up their social media presence and emulating their favorite professionals. 


## Objective

This repo creates an NLP text generator that generates text based off of the most prominent venture capitalist Twitter accounts. A user will be able to generate a prompt with the click of a button. Interpretability of text may vary, humor is welcome.  


## 1. Data Collection

You'll need a Twitter API token in order to use the `01_twitter_user.py` file from [Mehran Shakarami's AI Spectrum](https://github.com/mehranshakarami/AI_Spectrum). Go to developer.twitter.com and request Elevated access. Once you have your credentials, create a new file and store the configurations in separate variables. 

Once you have this, just change the username and limit variables in `01_twitter_user.py` to download the desired number of tweets as a csv file. The cleaned file for my modeling can be found [here](https://drive.google.com/file/d/1zsKT4MKBQPmjMtYVrL1QQOuXxU8bHYib/view?usp=sharing). 


## 2. Data Cleaning

Use the `02_cleaning.ipynb` notebook to clean your .csv file with the Twitter data for model input. It will remove usernames, URLs, quotes, and the 'RT :' string. It also saves a new column to retain whether the tweet was originally a retweet or not in case that's important to you. 

## 3. Data EDA

`03_eda.ipynb` just vectorizes the data and checks the most common single words and two-word phrases. 


## 4. Modeling

This project uses Max Woolf's `gpt-2-simple`, which also has a useful Google Colab notebook to help set it up: [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple). 

Using that Colab notebook, I fine-tuned the pre-trained model using the `124M` configuration and my Twitter text data. The fine-tuned model was then downloaded locally (size: ~500MB). 

The `04_text_gen.ipynb` notebook is largely taken from this same Colab notebook with a few tweaks and is only used to generate text on an already fine-tuned model stored locally. It's recommended to only use this notebook in Google Colab. If you want to fine-tune the model on other text, please use the original Colab notebook linked inside the [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple)'s README. 


## Streamlit App

The Streamlit app sets up the pre-trained, fine-tuned local model to generate a text sample at the click of a button. There are issues here. 

1. The model takes at least 3 minutes to run once without a GPU.
2. If using the `st.cache()` method saved in `app.py`, it will cut down local runtime by about 50%, however it will also mean that the button can only generate one text sample before having to be restarted. 


-------

## Data Sources

Twitter: The users chosen for this analysis are anonymous. Some proper names are still present in the tweets after cleaning, but those names are well-known and often talked about in venture capital. 


## Resources & Inspiration

1. The [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) library and Colab notebook for providing a pre-trained model and simple model training and fine-tuning. 

2. [Mehran Shakarami's AI Spectrum](https://github.com/mehranshakarami/AI_Spectrum) for a great, easy to use script for scraping tweets. 

3. StackOverflow help for the following regex: 

- [Removing Usernames in 02_cleaning.ipynb](https://stackoverflow.com/questions/50830214/remove-usernames-from-twitter-data-using-python)
- [Removing URLs in 02_cleaning.ipynb](https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python)