import pandas as pd

# TODO: link OpenAI here
# from openai import OpenAI
#  ## credit: https://www.youtube.com/watch?v=WJYvfTJPv-o - Mervin Praison
# client = OpenAI(api_key='<KEY>')
#
#
# this function is defined to create embeddings for text
# def get_embedding(text, model="text-embedding-ada-002"):
#     text = text.replace('\n', ' ')
#     return client.embeddings.create(input=[text], model=model).data[0].embedding

# TODO: convert text file into a dataframe before embedding, for more information see linked youtube video above. 
df = pd.read_csv('../data/Documents.csv', index_col=0)
print(df.head())
df.to_csv('../data/doc_df.csv')




