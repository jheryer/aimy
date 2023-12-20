from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
import os
import re


def load_pdf_documents_from_directory(input_directory: str) -> list:
    loader = DirectoryLoader(input_directory, glob="**/*.pdf", loader_cls=PyPDFLoader)
    return loader.load()


def load_text_documents_from_directory(input_directory: str) -> list:
    loader = DirectoryLoader(input_directory, glob="**/*.txt", loader_cls=TextLoader)
    return loader.load()


def load_markdown_documents_from_directory(input_directory: str) -> list:
    loader = DirectoryLoader(
        input_directory, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader
    )
    return loader.load()


def get_pdf_text(pdf_docs) -> str:
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text: str) -> list:
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_file_list(input_directory: str) -> list:
    pdf_files = [f for f in os.listdir(input_directory) if f.endswith(".pdf")]
    input_files = list(map(lambda f: os.path.join(input_directory, f), pdf_files))
    return input_files


def remove_non_ascii(text):
    return re.sub(r"[^\x00-\x7F]+", " ", text)


def consolidate_whitespace(text):
    return " ".join(text.split(" "))


def read_file_as_string(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)


def write_string_to_file(string_data, file_path):
    try:
        with open(file_path, "w") as file:
            file.write(string_data)
        return f"Data successfully written to {file_path}"
    except Exception as e:
        return str(e)
