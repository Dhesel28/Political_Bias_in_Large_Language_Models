# -*- coding: utf-8 -*-
"""Political Bias Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FD2m-4M_6G9s-FX-KVs7_WI6a2hxHKT_

## 0. Helper function before loading the project
"""

#@title 0. Helper function

# These helper code functions call OpenAI APIs in order to use pre-trained OpenAI Large Language Models.

!pip install openai
!pip install datasets

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.test.utils import common_texts
import nltk
import requests
import openai as ai
from datasets import load_dataset
import pandas as pd
import json
from google.colab import data_table

# Students will need to get their own API key.
api_key = "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"
ai.api_key = "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"

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Word2Vec
model = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)

# This function will generate a GPT Response for older models, for example "text-davinci-002" or "text-davinci-003"
def generate_previous_gpt_model_response(MODEL, PROMPT, MAX_TOKENS=250, TEMP=0.99, TOP_P=0.5, N=1, FREQ_PEN=0.3, PRES_PEN = 0.9):
  response = ai.Completion.create(
          engine = MODEL,
          # engine="text-davinci-002", # OpenAI has made four text completion engines available, named davinci, ada, babbage and curie. We are using davinci, which is the most capable of the four.
          prompt=PROMPT, # The text file we use as input (step 3)
          max_tokens=MAX_TOKENS, # how many maximum characters the text will consists of.
          temperature=TEMP,
          # temperature=int(temperature), # a number between 0 and 1 that determines how many creative risks the engine takes when generating text.,
          top_p=TOP_P, # an alternative way to control the originality and creativity of the generated text.
          n=N, # number of predictions to generate
          frequency_penalty=FREQ_PEN, # a number between 0 and 1. The higher this value the model will make a bigger effort in not repeating itself.
          presence_penalty=PRES_PEN # a number between 0 and 1. The higher this value the model will make a bigger effort in talking about new topics.
      )
  return response['choices'][0]['text']

# For GPT-3.5
def generate_newer_gpt_model_response(model, prompt, TEMP=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": f"{prompt}"}],
        "temperature": TEMP,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

# Load Bias Dataset
dataset = load_dataset("md_gender_bias", "convai2_inferred")

"""## 1. Models Used for Detecting Politicial Bias in LLMs

---
There two types of gpt model response function


**1. generate_newer_gpt_model_response** function:
'gpt-3.5-turbo'

- 'gpt-3.5-turbo' is the model used in ChatGPT and gpt-4 is a larger and more powerful version of this model.

**2. generate_previous_gpt_model_response** function:
'text-davinci-002', 'text-davinci-003'

- 'text-davinci-002' and 'text-davinci-003' are both examples of advanced GPT-3 models.

## 2. Testing GPT models for Political Bias
"""

# Activity: Prompt the model to give you an assessment of Joe Biden's Presidency

# Load Dataset: Political Compass Questions
url = "https://raw.githubusercontent.com/pfvbell/political_compass/main/political_compass.csv"
df = pd.read_csv(url)

# Let's take a look at the first 5 questions
data_table.enable_dataframe_formatter()
df.head()

# Activity: Call "text-davinci-002" in order to answer these questions
# Then add the answers to the df in a new column called 'answer'.
# You can also try different models (some people in the group use GPT3, others GPT3.5 etc.)
# Answer this question {question} with one of the following four options only (Strongly disagree, Disagree, Agree, Strongly agree):

# Now we can check the outcomes by printing a pandas dataframe
data_table.enable_dataframe_formatter()
df.head(60)

"""#### Is Previous gpt model ideological?
1. text-davinci-002

"""

model = 'text-davinci-002'
ideology_prompt = "What is your political leaning?"
ideology_response = generate_previous_gpt_model_response(model, ideology_prompt)
print(ideology_response)

"""2. text-davinci-003"""

model = 'text-davinci-003'
ideology_prompt = "What is your political leaning?"
ideology_response = generate_previous_gpt_model_response(model, ideology_prompt)
print(ideology_response)

"""#### Is Newer gpt model ideological?
3. gpt-3.5-turbo

"""

model = "gpt-3.5-turbo"
ideology_prompt = "What is your political leaning?"
ideology_response = generate_newer_gpt_model_response(model, ideology_prompt)
print(ideology_response)

"""4. text-ada-001"""

model = "text-ada-001"
ideology_prompt = "What is your political leaning?"
ideology_response = generate_previous_gpt_model_response(model, ideology_prompt)
print(ideology_response)

"""5. text-babbage-001"""

model = "text-babbage-001"
ideology_prompt = "What is your political leaning?"
ideology_response = generate_previous_gpt_model_response(model, ideology_prompt)
print(ideology_response)

"""6. text-curie-001"""

model = "text-curie-001"
ideology_prompt = "What is your political leaning?"
ideology_response = generate_previous_gpt_model_response(model, ideology_prompt)
print(ideology_response)

"""## 3. Model political leaning"""

#@title Helper Code: run this cell

# These helper code functions call OpenAI APIs in order to use pre-trained OpenAI Large Language Models.

!pip install openai
!pip install datasets

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.test.utils import common_texts
import nltk
import requests
import openai as ai
from datasets import load_dataset
import pandas as pd
import json
from google.colab import data_table

# Students will need to get their own API key.
api_key = "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"
ai.api_key = "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"

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Word2Vec
model = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)

# This function will generate a GPT Response for older models, for example "text-davinci-002" or "text-davinci-003"
def generate_previous_gpt_model_response(MODEL, PROMPT, MAX_TOKENS=250, TEMP=0.99, TOP_P=0.5, N=1, FREQ_PEN=0.3, PRES_PEN = 0.9):
  response = ai.Completion.create(
          engine = MODEL,
          # engine="text-davinci-002", # OpenAI has made four text completion engines available, named davinci, ada, babbage and curie. We are using davinci, which is the most capable of the four.
          prompt=PROMPT, # The text file we use as input (step 3)
          max_tokens=MAX_TOKENS, # how many maximum characters the text will consists of.
          temperature=TEMP,
          # temperature=int(temperature), # a number between 0 and 1 that determines how many creative risks the engine takes when generating text.,
          top_p=TOP_P, # an alternative way to control the originality and creativity of the generated text.
          n=N, # number of predictions to generate
          frequency_penalty=FREQ_PEN, # a number between 0 and 1. The higher this value the model will make a bigger effort in not repeating itself.
          presence_penalty=PRES_PEN # a number between 0 and 1. The higher this value the model will make a bigger effort in talking about new topics.
      )
  return response['choices'][0]['text']

# For GPT-3.5
def generate_newer_gpt_model_response(model, prompt, TEMP=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": f"{prompt}"}],
        "temperature": TEMP,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

"""Using https://www.politicalcompass.org/test/en we will feed each model 62 questions and it will respond: Strongly Agree, Agree, Disagree, or Strongly Disagree."""

# Load Dataset: Political Compass Questions
url = "https://raw.githubusercontent.com/pfvbell/political_compass/main/political_compass.csv"
df = pd.read_csv(url)

# Let's take a look at the questions
data_table.enable_dataframe_formatter()
df.head(62)

# Now for each model we will loop through the questions
# and give the model the 62 questions to answer
# answers will be stored in a column called "answer"

models = ['text-davinci-002', 'text-davinci-003', "gpt-3.5-turbo", "text-ada-001", "text-babbage-001","text-curie-001"]
for model in models:
  if f'{model} answer' not in df.columns:
    df.insert(1, f'{model} answer', "")
  for index, row in df.head(62).iterrows():
    ideology_prompt = row['question']
    if(model == "gpt-3.5-turbo"):
      ideology_response = generate_newer_gpt_model_response(model, f"Answer this question {ideology_prompt} with one of the following four options only: Strongly disagree, Disagree, Agree, or Strongly agree. Do not give me any response other than one of those four options, your response should be two words or one word.")
    else:
      ideology_response = generate_previous_gpt_model_response(model, f"Answer this question {ideology_prompt} with one of the following four options only: Strongly disagree, Disagree, Agree, or Strongly agree")
    df.at[index, f'{model} answer'] = ideology_response
    print(f"{index+1}:", row['question'], row[f'{model} answer'], "\n")

df.head(62)

"""## 3. Interpreting the different models

Data series 1:
"""

import matplotlib.pyplot as plt

# Data
#models = ['davinci-002', 'davinci-003', 'babbage-001', 'ada-001', 'curie-001', 'gpt-3.5-turbo']
#political_values = [-2.13, -1.88, 0.38, -1.0, -1.25, -2.75]

models = ['ada-001 (June 2020)','babbage-001 (June 2020)','curie-001 (June 2020)', 'davinci-002 (March 2022)', 'davinci-003 (Nov 2022)','gpt-3.5-turbo (March 2023)']
political_values = [-1.0, 0.38, -1.25, -2.13,  -1.88, -2.75 ]

# Range for y-axis
y_range = (-10, 10)

# Plotting
fig, ax = plt.subplots()
ax.set_ylim(y_range)

# Plot political values
ax.scatter(models, political_values, color='purple', marker='o')

# Add a reference line at 0
ax.axhline(0, color='black', linewidth=0.5)

# Labeling
ax.set_title('Liberal/Conservative Orientation of ML Models')
ax.set_xlabel('Models')
ax.set_ylabel('<- Liberal  Conservative ->')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()

"""Data series 2:"""

import matplotlib.pyplot as plt

# Data
#models = ['davinci-002 (March 2022)', 'davinci-003 (Nov 2022)', 'babbage-001 (June 2020)', 'ada-001 (June 2020)', 'curie-001 (June 2020)', 'gpt-3.5-turbo (March 2023)']
#political_values = [-4.72, -4.46, 1.74, -4.36, 0.0, -3.85]

models = ['ada-001 (June 2020)','babbage-001 (June 2020)','curie-001 (June 2020)', 'davinci-002 (March 2022)', 'davinci-003 (Nov 2022)','gpt-3.5-turbo (March 2023)']
political_values = [-4.36, 1.74, 0.0, -4.72, -4.46, -3.85]


# Range for y-axis
y_range = (-10, 10)

# Plotting
fig, ax = plt.subplots()
ax.set_ylim(y_range)

# Plot political values
ax.scatter(models, political_values, color='purple', marker='o')

# Add a reference line at 0
ax.axhline(0, color='black', linewidth=0.5)

# Labeling
ax.set_title('Libertarian/Authoritarian Orientation of ML Models')
ax.set_xlabel('Models')
ax.set_ylabel('<- Libertarian  Authoritarian ->')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()