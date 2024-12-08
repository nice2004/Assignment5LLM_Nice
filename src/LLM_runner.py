# heavily referenced from this user example in OpenAI cookbook :
# https://cookbook.openai.com/examples/question_answering_using_embeddings

# imports
import ast
from openai import OpenAI
import pandas as pd
import tiktoken
import os
from scipy import spatial

# I will remove my key before pushing my code, to run a user must input their own key
client = OpenAI(
    api_key='sk-proj'
            '-CxCwKarCT5TOyR0XUvczZA4yc2S1mkJoEWjo5dwzvzrYuIp7my4yX7FV6t1QfIgYEkxuIF0wvRT3BlbkFJ7baR9YpZmU5k2jZcp3jWSuy'
            'jOMtEatDVQNt1TPw9AcGO8J2j9TuAMC_h_G_V_RDwBrfvhv8CMA')

# accessing embeddings, your path to embedding file will likely vary, I set mine outside my git repository because of
# its size
df = pd.read_csv('../../Assignment5LLM-API/doc_df.csv')
df['embedding'] = df['embedding'].apply(ast.literal_eval)


# writing a search function that takes and embeds a user query, and then returns the most relevant embeddings
def string_relatedness(query: str, df: pd.DataFrame, relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
                       top_n: int = 100) -> tuple[list[str], list[float]]:
    embedded_query = client.embeddings.create(model='text-embedding-ada-002', input=query)
    query_embedding = embedded_query.data[0].embedding
    strings_relatedness = [(row["text"], relatedness_fn(query_embedding, row["embedding"]))
                           for i, row in df.iterrows()]
    strings_relatedness = sorted(strings_relatedness, key=lambda x: x[1], reverse=True)
    strings, relatedness = zip(*strings_relatedness)
    return strings[:top_n], relatedness[:top_n]


# writing a function to compute the number of tokens in given text, to ensure that we do not exceed the rate of usage
# allowed by our OpenAI model
def token_count(text: str, model: str = "gpt-4o-mini") -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))



