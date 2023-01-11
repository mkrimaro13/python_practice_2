import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/products') # Se obtiene la información\
    status = r.status_code
    text = r.text
    print(status) # obtiene el código HTTP
    print(text) # Imprime el texto
    categories = r.json() # aquí me devuelve el contenido de la api en el formato JSON, lista de diccionarios
    for category in categories:
        print(category['title'])