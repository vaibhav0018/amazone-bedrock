import boto3
import streamlit as st
import uuid
import os 

#s3_client
s3_client = boto3.client("s3")
BUCKET_NAME = os.getenv("BUCKET_NAME")


##bedrock
from langchain_aws import BedrockEmbeddings

## text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

## pdf loader
from langchain_community.document_loaders import PyPDFLoader

## vector store
from langchain_community.vectorstores import FAISS

bedrock_client = boto3.client(
    "bedrock-runtime",
    region_name=os.getenv("AWS_REGION", "ap-south-1")
)

bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0", client=bedrock_client)

def getUniqueId():
    return str(uuid.uuid4())

## creating vector store
# def create_vectore_store(request_id, documents):
#     vectore_store = FAISS.from_documents(documents, bedrock_embeddings)
#     file_name = f"{request_id}.bin"
#     folder_path = "/tmp/"
#     vectore_store.save_local(index_name=file_name, folder_path=folder_path)
    
#     ## upload to S3
#     s3_client.upload_file(Filename=folder_path + "/" + file_name + ".faiss", Bucket = BUCKET_NAME, Key="my_faiss.faiss")
#     s3_client.upload_file(Filename=folder_path + "/" + file_name + ".pkl", Bucket = BUCKET_NAME, Key="my_faiss.pkl")
    
#     return True    

def create_vectore_store(documents):
    try:
        folder_path = "/tmp/"
        index_name = "my_faiss"

        vectore_store = FAISS.from_documents(documents, bedrock_embeddings)
        vectore_store.save_local(folder_path=folder_path, index_name=index_name)

        s3_client.upload_file(
            Filename=f"{folder_path}{index_name}.faiss",
            Bucket=BUCKET_NAME,
            Key="my_faiss.faiss"
        )
        s3_client.upload_file(
            Filename=f"{folder_path}{index_name}.pkl",
            Bucket=BUCKET_NAME,
            Key="my_faiss.pkl"
        )
        
        return True
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

## split the pages/ text on the pages into chunks
def split_text(pages, chunk_size, chunk_overlap):
    text_spliter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_spliter.split_documents(pages)
    return docs
    

def main():
    st.write("this is admin side for chat with PDF demo")
    uploaded_file = st.file_uploader("choose a file", "pdf")
    if uploaded_file is not None:
        request_id = getUniqueId()
        st.write(f"request id: {request_id}")
        saved_file_name = f"{request_id}.pdf"
        with open(saved_file_name, mode= "wb") as w:
            w.write(uploaded_file.getvalue())
            
        loader = PyPDFLoader(saved_file_name)
        pages = loader.load()
        st.write(f"Total pages are : {len(pages)}")
        
        ## split text
        splitted_docs = split_text(pages, 500, 100)
        st.write(f"splitted docs length: {len(splitted_docs)}")
        st.write("================================")
        st.write(splitted_docs[0])
        
        ## vectore store
        st.write("creating ths vector store")
        result = create_vectore_store(splitted_docs)

        if result:
            st.write("hurray")
        else:
            st.write("error")

if __name__ == "__main__":
    main()
    
    
    
    
    

#vaibhav
    
# docker build -t pdf-reader-admin .
# docker run -p 8083:8083 -it pdf-reader-admin