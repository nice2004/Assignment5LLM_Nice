import pandas as pd
# from openai import OpenAI
#  ## credit: https://www.youtube.com/watch?v=WJYvfTJPv-o - Mervin Praison
# client = OpenAI(api_key='<KEY>')
#
#
# def get_embedding(text, model="text-embedding-ada-002"):
#     text = text.replace('\n', ' ')
#     return client.embeddings.create(input=[text], model=model).data[0].embedding


df = pd.read_csv('../data/Documents.csv', index_col=0)
print(df.head())





