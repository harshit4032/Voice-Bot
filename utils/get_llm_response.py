from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
# from decouple import config
load_dotenv()

os.environ["GROQ_API_KEY"] =  os.getenv('GROQ_API_KEY')
# os.environ["ANTHROPIC_API_KEY"] = config("ANTHROPIC_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')


def get_openai_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who answer the questions concisely yet meaningfully, reflecting a balance of professional expertise, personal growth, and unique qualities. Structure each response clearly, providing specific examples where relevant. Maintain a confident and engaging tone and also include about yourself during introduction like i am an GPT-3.5-turbo llm"),
            ("human", "{input}"),
        ]
    )

    # Initialize the OpenAI Chat model (e.g., GPT-4)
    _model = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Chain the prompt with the model using LCEL
    chain = _prompt | _model

    # Execute the chain to get the response
    response = chain.invoke(input=transcribed_text)
    
    return response.content


def get_groq_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who answer the questions concisely yet meaningfully, reflecting a balance of professional expertise, personal growth, and unique qualities. Structure each response clearly, providing specific examples where relevant. Maintain a confident and engaging tone and also include about yourself during introduction like i am an Deepseek-R1-distill-llama-70b llm"),
            ("human", "{input}"),
        ]
    )

    # Initialize the Meta AI model (e.g., Llama 3.1 70b versetile)
    _model = ChatGroq(
        model="deepseek-r1-distill-llama-70b",
        temperature=0,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
    )
    # Chain the prompt with the model using LCEL
    chain = _prompt | _model

    # Execute the chain to get the response
    response = chain.invoke(input=transcribed_text)
    
    return response.content

def get_gemini_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who answer the questions concisely yet meaningfully, reflecting a balance of professional expertise, personal growth, and unique qualities. Structure each response clearly, providing specific examples where relevant. Maintain a confident and engaging tone and also include about yourself during introduction like i am an Gemini-1.5-pro llm"),
            ("human", "{input}"),
        ]
    )

    # Initialize the Google Deep Mind model (e.g., Gemini Pro 1.5)
    _model = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
    )

    # Chain the prompt with the model using LCEL
    chain = _prompt | _model

    # Execute the chain to get the response
    response = chain.invoke(input=transcribed_text)
    
    return response.content

