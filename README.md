# vc-twitter README

----- Work in progress -------


## Problem Statement

Many fields are now expecting candidates to have a robust social media presence. However, it can be difficult to come up with what to write about or tweet about. It would be useful if a finance or investment candidate could easily generate sample text to use in keeping up their social media presence and emulating their favorite professionals. 


## Objective

The objective of this project is to create an NLP text generator that generates text based off of the most prominent venture capitalist Twitter accounts. A user will be able to generate a useful prompt with the click of a button. Interpretability of text may vary. 


## 1. Data Collection

You'll need a Twitter API token in order to use the `01_twitter_user.py` file from [Mehran Shakarami's AI Spectrum](https://github.com/mehranshakarami/AI_Spectrum). Go to developer.twitter.com and request Elevated access. Once you have your credentials, create a new file and store the configurations in separate variables. 


## 2. Data Cleaning

Use the `02_cleaning.ipynb` notebook to clean your .csv file with the Twitter data for model input. It will remove usernames, URLs, quotes, and the 'RT :' string. It also saves a new column to retain whether the tweet was originally a retweet or not. 

## 3. Data EDA

`03_eda.ipynb` just vectorizes the data and checks the most common single words and two-word phrases. It also outputs a .txt file from the dataframe. 


## 4. Modeling

This project uses Max Woolf's `gpt-2-simple`, which also has a useful Google Colab notebook to help set it up: [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple). the `05_gpt_2_simple.ipynb` notebook is largely taken from this Colab notebook with a few tweaks. The model will take in a .txt file from the previous notebook (3). 



## Data Sources

**Twitter.com** The users chosen for this analysis are anonymous, but not random. Some proper names are still present in the tweets after cleaning, but those names are well-known and often talked about in venture capital. 


## Resources & Inspiration

2. StackOverflow help for the following regex: 

- [Removing Usernames in 02_cleaning.ipynb](https://stackoverflow.com/questions/50830214/remove-usernames-from-twitter-data-using-python)
- [Removing URLs in 02_cleaning.ipynb](https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python)