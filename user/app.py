import boto3
import streamlit as st
import uuid
import os

# s3 client
s3_client = boto3.client("s3")
BUCKET_NAME = os.getenv("BUCKET_NAME")

## Bedrock
from langchain_aws import BedrockEmbeddings, BedrockLLM, ChatBedrock

## Text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate

## PDF loader
from langchain_community.document_loaders import PyPDFLoader

## Vector store
from langchain_community.vectorstores import FAISS

## NEW (modern retrieval chain)
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


bedrock_client = boto3.client(
    "bedrock-runtime",
    region_name=os.getenv("AWS_REGION", "ap-south-1")
)

bedrock_embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0",
    client=bedrock_client
)

folder_path = "/tmp/"

def getUniqueId():
    return str(uuid.uuid4())

## Load FAISS index from S3
def load_index():
    s3_client.download_file(
        Bucket=BUCKET_NAME,
        Key="my_faiss.faiss",
        Filename=f"{folder_path}my_faiss.faiss"
    )
    s3_client.download_file(
        Bucket=BUCKET_NAME,
        Key="my_faiss.pkl",
        Filename=f"{folder_path}my_faiss.pkl"
    )

## LLM (cheap & safe)
# def get_llm():
#     llm = ChatBedrock(
#         model_id="anthropic.claude-3-haiku-20240307-v1:0",
#         client=bedrock_client,
#         model_kwargs={"max_tokens": 300}
#     )
#     return llm

def get_llm():
    llm = BedrockLLM(
        model_id="amazon.nova-lite-v1:0",
        client=bedrock_client,
        model_kwargs={"max_tokens": 300}
    )
    return llm


## RAG response (MODERN)
def get_response(llm, vectorstore, question):

    prompt_template = """
Human: Use the context below to answer the question.
If you don't know the answer, say you don't know.

<context>
{context}
</context>

Question: {question}

Assistant:
"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke(question)


def main():
    st.header("this is client side for chat with PDF demo using bedrock")

    load_index()

    st.write("Files in /tmp:", os.listdir(folder_path))
    st.write("Bucket:", BUCKET_NAME)

    faiss_index = FAISS.load_local(
        folder_path=folder_path,
        index_name="my_faiss",
        embeddings=bedrock_embeddings,
        allow_dangerous_deserialization=True
    )

    st.success("FAISS index loaded")

    question = st.text_input("Ask a question")

    if st.button("Ask Question") and question:
        with st.spinner("Querying Bedrock..."):
            llm = get_llm()
            answer = get_response(llm, faiss_index, question)
            st.write(answer)

if __name__ == "__main__":
    main()



# docker run   -e BUCKET_NAME=vaibhav-learning-bucket   -e AWS_REGION=ap-south-1   -e AWS_DEFAULT_REGION=ap-south-1   -v ~/.aws:/root/.aws   -p 8084:8084   -it pdf-reader-client