import pymupdf

doc = pymupdf.open("Fichas_Muestras/PAZ_Diseño_primero primaria_Autonomía_Autonomía_F1_¿Qué es autonomía__02-05-2025.pdf") # open a document
out = open("output.txt", "wb") # create a text output
for page in doc: # iterate the document pages
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
out.close()