# Assignment5LLM
**Westmont College Fall 2024**

**CS 128 Information Retrieval and Big Data**

# Team Members:
- David Oyebade (doyebade@westmont.edu)
- Gabriel Leung (gleung@westmont.edu)
- Nice Teta Hirwa (nhirwa@westmont.edu)

*Demo link:* https://docs.google.com/presentation/d/15MbI7QSrifDiAkEs1deu6F1GjQt3lJBw75o0Zt7jMU0/edit#slide=id.g31d17e0d652_0_1
*Demo Code:* term

# Project Structure 

This README file thoroughly explains the structure of our project with its directories, files and their functions.
For context, our project is to make a chatbot that is personable. This Chat Bot can be trained based on your own files, the data set we chose contains 
text message corpus from Kaggle.

About our project Structure: In this project, we have two main directories that are fully written in python which are: 
data and src. 

*In the data folder:* this is where we kept our datasets for the project. Inside the directory, there is a csv file called "Documents.csv" which is a dataset that 
contains enormous information of text messages that we work with in this project.  

*In the src folder:* we have three main files, embedding.py, LLM_models.py, and LLM_runner.py. Here is what each file does in a brief description:
* Embedding.py: This file executes the embeddings on the text dataset by using the OpenAI Api and its model. 
Inside the file, we have a 'get_embedding' file that creates an embedding for the entire dataset. 


* LLM_Models.py: This file is the heart of our project. It takes a user query and a dataframe with text & embedding columns, and 
returns two lists, the top N texts, ranked by relevance and the list of their corresponding relevance scores. This is all done in
a function called 'string_relatedness'. Inside the file, there is also a function, 'ask' that passes a query into api and retrieves response. But for ask function 
to print out the answer, we created a query_message function that is designed to generate a message based on a given query and a DataFrame containing some text data. 
And of course, since we do not own the API, we had to create a function that compute the number of tokens in given text, to ensure that we do not exceed the rate of usage
allowed by our OpenAI model .

* LLM_runner.py: this is the runner of our project where a user is able to ask questions and get a response. This is all done due to 
the 'ask' function importation from the LLM_models.

# Detailed instructions on how one might go about utilizing your software
- Clone the repository - git clone (the ssh key)
- To use our chatbot - run LLM_runner.py

# Sources

Mervin Praison: 
https://www.youtube.com/watch?v=WJYvfTJPv-o

API from: 
https://platform.openai.com/chat-completions

API utilization: 
https://cookbook.openai.com/examples/question_answering_using_embeddings
