from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain import LLMChain
from langchain.prompts import PromptTemplate

class Chatbot:
    def __init__(self, courses):
        if not courses:
            raise ValueError("No courses found. Please check the data extraction logic.")
        
        self.embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = FAISS.from_texts([course['description'] for course in courses], self.embeddings)
        self.prompt = PromptTemplate("You are a helpful assistant. Answer the user's question based on the following courses: {context}")


    def get_response(self, user_input):
        similar_courses = self.vector_store.similarity_search(user_input)
        context = "\n".join([course['description'] for course in similar_courses])
        llm_chain = LLMChain(llm='gpt-3.5-turbo', prompt=self.prompt)
        return llm_chain.run(context=context)
