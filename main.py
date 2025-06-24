from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model='llama3.2')

template = """
You are an expert in answering questions about a Pneumonia, Covid-19, and Lung Dieseases

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    question = input("Ask yout question (q for quit): ")
    if question == 'q':
        break
    
    