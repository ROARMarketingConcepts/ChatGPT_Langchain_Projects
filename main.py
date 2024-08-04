from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv  
import argparse
import os
import sys
import json

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument('--language', type=str, default='Python')
parser.add_argument('--task', type=str, default='return a list of prime numbers')
args=parser.parse_args()

llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a short {language} function that will {task}.",
    input_variables=["language", "task"]
    )
code_chain = LLMChain(
    llm=llm, 
    prompt=code_prompt
    )   

result = code_chain({
    "language": args.language, 
    "task": args.task
    })
print(result)
print(result["text"])   
