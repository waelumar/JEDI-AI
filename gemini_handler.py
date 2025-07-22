import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter 
import os

genai.configure(api_key=#insert your gemini api key here )

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

file=r#insert your text file path here


def create_faiss_index():
    loader = TextLoader(file, encoding="utf-8")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("my_faiss_index")

if not os.path.exists("my_faiss_index/index.faiss"):
    create_faiss_index()


def get_gemini_response(prompt, character="jedi knight"):
    retriever = FAISS.load_local(
        "my_faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    ).as_retriever()

    relevant_docs = retriever.get_relevant_documents(prompt)
    context = "\n".join([doc.page_content for doc in relevant_docs])

    system_prompt = f"Reply like {character} from Star Wars. Use their speech style and tone, and use the following context:\n{context}"

    model = genai.GenerativeModel('gemini-2.0-flash')

    response = model.generate_content(
        [system_prompt, prompt],
        generation_config={"temperature": 0.7}
    )

    return response.text.strip()