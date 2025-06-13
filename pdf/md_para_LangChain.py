import pymupdf4llm
from langchain.text_splitter import MarkdownTextSplitter
import pathlib
import os
original_pdf_path = "Fichas_Muestras/PAZ_Diseño_primero primaria_Autonomía_Autonomía_F1_¿Qué es autonomía__02-05-2025.pdf"
# Convertir PDF a Markdown
md_text = pymupdf4llm.to_markdown(original_pdf_path)
splitter = MarkdownTextSplitter(chunk_size=40, chunk_overlap=0)
documents = splitter.create_documents([md_text])
# Concatenar el contenido de los fragmentos separados
combined_text = "\n\n".join(doc.page_content for doc in documents)
# Construir el nuevo nombre de archivo con "-splitter"
base_name = os.path.splitext(os.path.basename(original_pdf_path))[0]
new_filename = base_name + "-splitter.md"
new_filepath = os.path.join(os.path.dirname(original_pdf_path), new_filename)
# Guardar el contenido dividido en el nuevo archivo Markdown
pathlib.Path(new_filepath).write_text(combined_text, encoding="utf-8")
print(f"Archivo guardado en: {new_filepath}")
