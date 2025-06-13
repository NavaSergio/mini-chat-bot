import pymupdf4llm
import os
import pathlib
# Directorio donde se encuentran los archivos PDF
input_directory = "Fichas_Muestras"
# Iterar sobre todos los archivos en el directorio
for filename in os.listdir(input_directory):
    if filename.endswith(".pdf"):  # Verificar si el archivo es un PDF
        pdf_path = os.path.join(input_directory, filename)  # Ruta completa del archivo PDF
        md_filename = filename[:-4] + ".md"  # Crear el nombre del archivo Markdown
        md_path = os.path.join(input_directory, md_filename)  # Ruta completa del archivo Markdown
        # Convertir el documento PDF a Markdown
        md_text = pymupdf4llm.to_markdown(pdf_path)
        # Escribir el texto en un archivo Markdown en codificación UTF-8
        pathlib.Path(md_path).write_bytes(md_text.encode("utf-8"))




