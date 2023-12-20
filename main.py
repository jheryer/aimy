from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from lib.files import (
    get_pdf_text,
    get_text_chunks,
    load_pdf_documents_from_directory,
    read_file_as_string,
    write_string_to_file,
    remove_non_ascii,
    consolidate_whitespace,
)
from lib.lc import get_vectorstore

content = read_file_as_string("./bee_kind_pillow.txt")
content = remove_non_ascii(content)
content = consolidate_whitespace(content)
print(content)
write_string_to_file(content, "./bee_kind_pillow_clean.txt")

# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")
# print(api_key)
# llm = ChatOpenAI(openai_api_key=api_key)
# pdf_text = get_pdf_text(["./live_assets/Bee Kind Pillow Pattern.pdf"])
# print(pdf_text)
# chunks = get_text_chunks(pdf_text)
# vector_store = get_vectorstore(chunks)
# print(chunks)
# # print(pdf_text)

if __name__ == "__main__":
    print("Hello World!")
