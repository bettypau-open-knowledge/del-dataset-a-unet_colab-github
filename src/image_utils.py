from pathlib import Path
from PIL import Image

def cargar_imagen(ruta):
    """Carga una imagen desde una ruta."""
    '''Input: ruta (str): La ruta del archivo de imagen.
	   Output: imagen (PIL.Image.Image): La imagen cargada.'''
    
    ruta = Path(ruta)
    return Image.open(ruta)

def convertir_grises(imagen):
    """Convierte una imagen a escala de grises."""
    '''Input: imagen (PIL.Image.Image): La imagen a convertir.
	   Output: imagen (PIL.Image.Image): La imagen convertida a escala de grises.'''
    
    return imagen.convert("L")