import pandas as pd

from openai import OpenAI

## credit: https://www.youtube.com/watch?v=WJYvfTJPv-o - Mervin Praison
client = OpenAI(
    api_key='sk-proj'
            '-CxCwKarCT5TOyR0XUvczZA4yc2S1mkJoEWjo5dwzvzrYuIp7my4yX7FV6t1QfIgYEkxuIF0wvRT3BlbkFJ7baR9YpZmU5k2jZcp3jWSuy'
            'jOMtEatDVQNt1TPw9AcGO8J2j9TuAMC_h_G_V_RDwBrfvhv8CMA')


#
# this function is defined to create embeddings for text

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace('\n', ' ')
    return client.embeddings.create(input=[text], model=model, encoding_format="float").data[0].embedding


df = pd.read_csv('../data/Documents.csv', index_col=0)
print(df.info())

example_text = "A man walked down the road"
# the below line of code is extremely time-consuming
# df["embedding"] = df["SMS"].apply(lambda x: get_embedding(x, model="text-embedding-ada-002"))


# example_embeddings = get_embedding(example_text, model="text-embedding-ada-002")
# print(example_embeddings)
