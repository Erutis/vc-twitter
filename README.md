# vc-twitter 

# Objective

The objective of this project is to create an NLP text generator that generates text based off of the most prominent venture capitalist Twitter accounts. The final format will either be a website with a button that generates text or even a Twitter bot that posts generated tweets. The purpose of this is to simulate founder advice and inspiration from what VCs say on their accounts. 

Success metrics will be focused on interpretability of output and humor. The funnier the text generation is, the more successful it will be considered. 



## Data Collection

This project will use Twitter's API to scrape the latest tweets from a select few accounts. For privacy reasons, I will not reveal which venture capital accounts I will use for this text generation. 

For EDA and cleaning, I will attempt to focus on those tweets that mention certain keywords so that I can avoid samples that are not startup-related. 


## Modeling

I am considering training my own models from scratch or making use of an accessible version of GPT. If I choose the latter, I will use something available on Hugging Face (possibly [this one](https://huggingface.co/gpt2)). # vc-twitter
