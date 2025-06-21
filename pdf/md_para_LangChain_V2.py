import pymupdf4llm
import pathlib
import os

# Directorio donde están los archivos PDF
input_directory = "pdf/229-2_Primaria"

# Iterar sobre todos los archivos del directorio
for filename in os.listdir(input_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_directory, filename)

        try:
            # Convertir PDF completo a texto en formato Markdown
            md_text = pymupdf4llm.to_markdown(pdf_path)

            # Crear nombre y ruta del archivo Markdown de salida
            base_name = os.path.splitext(filename)[0]
            md_filename = base_name + ".md"
            md_path = os.path.join(input_directory, md_filename)

            # Guardar el texto Markdown
            pathlib.Path(md_path).write_text(md_text, encoding="utf-8")
            print(f"[✔] Guardado: {md_filename}")

        except Exception as e:
            print(f"[✘] Error procesando {filename}: {e}")
