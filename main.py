from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# load the GOOGLE_API_KEY
google_api_key =  os.getenv("GOOGLE_API_KEY")

# Initialize an instance of the GoogleGenerativeAI with specific parameters
llm =  GoogleGenerativeAI(
    model="gemini-1.5-flash",  # Specify the model to use
    temperature=0.2,            # Set the randomness of the model's responses (0 = deterministic, 1 = very random)
)


#1 Loading the file
try:
    loader = TextLoader("data.txt")
except Exception as e:
    print("Error while loading file=", e)
    
    
# 2 spliting the file data into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)


#3 Create embaddings
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001") 


#4 create the index with specified embedding model and text_splitter
index_creator = VectorstoreIndexCreator(
    embedding = embedding,
    text_splitter= text_splitter
)

index = index_creator.from_loaders([loader])

# query the index with llm
while True:
    Human_message = input("How i can help you?")
    response = index.query(Human_message, llm=llm)
   
      # Check if the response is relevant to the hotel's information 
    if response:
        print(response)  # Display the relevant response
    else:
        print("Please ask questions specifically about AneelaNasir Hotel services or information.")  # Request for relevant questions