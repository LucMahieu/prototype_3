import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle
import os
from dotenv import load_dotenv
import tiktoken
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

pdf_upload = st.file_uploader("Choose a PDF file", type="pdf")
# st.write(pdf_upload)

if pdf_upload is not None:
    pdf_reader = PdfReader(pdf_upload)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # st.write(text)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks = text_splitter.split_text(text=text)
    # st.write(chunks)

    # embeddings
    store_name = pdf_upload.name[:-4]
    # st.write(store_name)

    if os.path.exists(f"{store_name}.pkl"):
        with open(f"{store_name}.pkl", 'rb') as f:
            VectorStore = pickle.load(f)
        # st.write('Embeddings loaded from disk')
    else:
        embeddings = OpenAIEmbeddings()
        VectorStore = FAISS.from_texts(texts=chunks, embedding=embeddings)
        with open(f"{store_name}.pkl", 'wb') as f:
            pickle.dump(VectorStore, f)
        # st.write('Embeddings created and uploaded to disk')


    # Input question/query from user
    query = st.text_input('Ask a question about your document')
    # st.write(query)

    if query:
        docs = VectorStore.similarity_search(query=query, k=3)
        st.write(docs)

        llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
        chain = load_qa_chain(chain_type="stuff", llm=llm)
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=query)
            print(cb)
        st.write(response)

