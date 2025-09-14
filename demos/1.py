from llama_index.core import VectorStoreIndex,SimpleDirectoryReader, Settings
from dotenv import load_dotenv
load_dotenv()

docs=SimpleDirectoryReader("data").load_data()
index=VectorStoreIndex.from_documents(docs)
query_engine=index.as_query_engine()
response=query_engine.query("What are the different types of data and how are they categorized in data science?")
print(response)
