# TLaaS: Thought Leadership as a Service

## Problem Statement

Many fields are now expecting existing and potential employees to have a robust social media presence. However, it can be difficult to come up with what to write about or tweet about. It would be useful if a finance or investment professional could easily generate sample text to use in keeping up their social media presence and emulating their favorite professionals. 


## Objective

This repo creates an NLP text generator that generates text based off of the most prominent venture capitalist Twitter accounts. A user will be able to generate a prompt with the click of a button. Readability of text may vary, humorous interpretation is welcome. Try it out on [HuggingFace](https://huggingface.co/spaces/erutis/vc-twitter). 


## 1. Data Collection

You'll need a Twitter API token in order to use the `01_twitter_user.py` file from [Mehran Shakarami's AI Spectrum](https://github.com/mehranshakarami/AI_Spectrum). Go to developer.twitter.com and request Elevated access. Once you have your credentials, create a new file and store the configurations in separate variables. 

Once you have this, just change the username and limit variables in `01_twitter_user.py` to download the desired number of tweets as a csv file. The cleaned file for my modeling can be found [here](https://drive.google.com/file/d/1zsKT4MKBQPmjMtYVrL1QQOuXxU8bHYib/view?usp=sharing). 


## 2. Data Cleaning

Use the `02_cleaning.ipynb` notebook to clean your .csv file with the Twitter data for model input. It will remove usernames, URLs, quotes, and the 'RT :' string. It also saves a new column to retain whether the tweet was originally a retweet or not in case that's important to you. 

## 3. Data EDA

`03_eda.ipynb` just vectorizes the data and checks the most common single words and two-word phrases to ensure that the content has the venture capital topic skew that we were looking for. 


## 4. Modeling

### 4a. gpt-2-simple

This project first used Max Woolf's `gpt-2-simple`, which also has a useful Google Colab notebook to help set it up: [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple). Using that Colab notebook, I fine-tuned the pre-trained model using the `124M` parameter configuration and my Twitter text data. The fine-tuned model was then downloaded locally (size: ~500MB). This took over 45 minutes per run and then took over 3-4 minutes for each text generation request. 


### 4b. aitextgen

Later on, it was pointed out that gpt-2-simple has a successor called [aitextgen](https://github.com/minimaxir/aitextgen). It also has an easy-to-use Google Colab notebook, but this time the fine-tuning takes less than 20 minutes and each text generation request is fulfilled in less than 10 seconds, even locally without GPU. 

The `04_aitextgen.ipynb` notebook is largely taken from this same Colab notebook with a few tweaks and is only used to generate text on an already fine-tuned model stored locally. It works well on Colab or locally. If you want to fine-tune the model on other text, please use the original Colab notebook linked inside [aitextgen](https://github.com/minimaxir/aitextgen)'s README. 

If you'd like to use the models I fine-tuned, they can be found in [Google Drive here](https://drive.google.com/drive/folders/1-0lJhen6aObbTU50BBTlS-IprfgD_iCY?usp=sharing).


gpt-2-simple runs: 

- `run1`: the original fine-tuning that didn't remove the strings with 'RT' and quote symbols; used only 300 tweets per user
- `run2`: second run using the 300 posts/user. Took out RT and quotes and it looks cleaner.
- `run3` - third run, this time using 3,000 posts/user. results are more matter-of-fact and less funny.
- `run4` - tried excluding tweets that had fewer than 20 characters to help the output be long each time. 

aitextgen runs:
- `run1.1`: uses 300 tweets/user in csv format to avoid strange spacing
- `run2.1`: uses 300 tweets/user in txt format
- `run3.1`: uses 3,000 tweets/user in csv format
- `run4.1`: uses 3,000 tweets/user in txt format

My opinion is that run1.1 has the funniest output, but that run3.1 has the most coherent. Use whichever you'd like. 


## Streamlit App on HuggingFace

The Streamlit app sets up the pre-trained, fine-tuned `run1.1` model to generate a text sample at the click of a button. You can access a working version of it [here](https://huggingface.co/spaces/erutis/vc-twitter). 


-------

## Data Sources

Twitter: The users chosen for this analysis are anonymous. Some proper names are still present in the tweets after cleaning, but those names are well-known and often talked about in venture capital. 


## Resources & Inspiration

Shoutout to Niraj Saran for pointing me to resource #2 below. 

1. The [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) library and Colab notebook for providing a pre-trained model and simple model training and fine-tuning. 

2. The [aitextgen](https://github.com/minimaxir/aitextgen) library that improves on gpt-2-simple by leaps and bounds. 

3. [Mehran Shakarami's AI Spectrum](https://github.com/mehranshakarami/AI_Spectrum) for a great, easy to use script for scraping tweets. 

4. StackOverflow help for the following regex: 

- [Removing Usernames in 02_cleaning.ipynb](https://stackoverflow.com/questions/50830214/remove-usernames-from-twitter-data-using-python)
- [Removing URLs in 02_cleaning.ipynb](https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python)