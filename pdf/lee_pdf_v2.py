import pymupdf
import os
# Directorio donde se encuentran los archivos PDF
input_directory = "pdf/229-3_Secundaría"
# Iterar sobre todos los archivos en el directorio
for filename in os.listdir(input_directory):
    if filename.endswith(".pdf"):  # Verificar si el archivo es un PDF
        pdf_path = os.path.join(input_directory, filename)  # Ruta completa del archivo PDF
        txt_filename = filename[:-4] + ".txt"  # Crear el nombre del archivo TXT
        txt_path = os.path.join(input_directory, txt_filename)  # Ruta completa del archivo TXT
        # Abrir el documento PDF
        doc = pymupdf.open(pdf_path)
        # Crear un archivo de salida para el texto
        with open(txt_path, "wb") as out:
            for page in doc:  # Iterar las páginas del documento
                text = page.get_text().encode("utf8")  # Obtener texto plano (en UTF-8)
                out.write(text)  # Escribir el texto de la página
                out.write(bytes((12,)))  # Escribir delimitador de página (form feed 0x0C)
        doc.close()  # Cerrar el documento PDF