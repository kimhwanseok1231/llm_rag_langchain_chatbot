import getpass
import os
from dotenv import load_dotenv
from langchain_upstage import UpstageEmbeddings
from langchain_upstage import ChatUpstage
from langchain_classic import hub
from langchain_classic.chains import RetrievalQA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_pinecone import PineconeVectorStore


def get_retrieval():
    # upstage에서 embedding 코드참고함 
    embeddings = UpstageEmbeddings( model="solar-embedding-1-large")  
    index='tax-index-markdown'
    database = PineconeVectorStore.from_existing_index(index_name=index, embedding=embeddings)
    retriever=database.as_retriever(search_kwargs={'k':4})
    return get_retrieval
    

def get_llm():
    llm=ChatUpstage()
    return llm


def get_dictionary_chain():
    dictionary = ["사람을 나타내는 표현 -> 거주자"]
    llm=get_llm()

    prompt = ChatPromptTemplate.from_template(f"""
        사용자의 질문을 보고, 우리의 사전을 참고해서 사용자의 질문을 변경해주세요.
        만약 변경할 필요가 없다고 판단된다면, 사용자의 질문을 변경하지 않아도 됩니다.
        그런 경우에는 질문만 리턴해주세요
        사전: {dictionary}
        
        질문: {{question}}
    """)

    dictionary_chain = prompt | llm | StrOutputParser()
    return dictionary_chain


def get_ai_message(user_message):
    # def  get_ai_messasge(user_message):
   
# 환경변수를 불러옴
    load_dotenv()


    

  
       
    
    dictionary_chain=get_dictionary_chain()
    qa_chain=get_qa_chain()
    tax_chain = {"query": dictionary_chain} | qa_chain
    ai_message=tax_chain.invoke({"question" :user_message})
    return ai_message["result"]

def get_qa_chain():
      llm=get_llm()
      retriever=get_retrieval
      prompt=hub.pull("rlm/rag-prompt")
      qa_chain=RetrievalQA.from_chain_type(llm,retriever=retriever,chain_type_kwargs={"prompt":prompt} 
    )