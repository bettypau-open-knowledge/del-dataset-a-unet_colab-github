from pathlib import Path

def leer_texto(ruta):
    """Lee un archivo de texto y devuelve su contenido."""
    '''Input: ruta (str): La ruta del archivo de texto.
	   Output: contenido (str): El contenido del archivo de texto.'''
    
    ruta = Path(ruta)

    with ruta.open("r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    return contenido