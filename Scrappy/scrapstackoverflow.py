import requests
from lxml import html
from bs4 import BeautifulSoup #pip install beautifulsoup4

#User agent para protegernos de baneos
encabezado = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

#Url de donde extraemos la información
url = 'https://stackoverflow.com/questions'

#Lo que pedimos al servidor
respuesta = requests.get(url, headers=encabezado)

#Parseo del arbol con beautifulsoup
soup = BeautifulSoup(respuesta.text)

#Buscamos en la respuesta parseada el elemento con id questions
contenedorRespuestas = soup.find(id="questions")
#Buscamos dentro del contenedor de respuestas todos los div con la clase s-post-summary
listaPreguntas = contenedorRespuestas.find_all('div', class_="s-post-summary")

#Recorremos todas las preguntas almacenadas en listaPreguntas
for pregunta in listaPreguntas:
    #Extraemos de pregunta el texto contenido en los elementos tipo h3
    textoPregunta = pregunta.find('h3').text
    #print(textoPregunta)
    #Extraemos el texto contenido en los elementos con clase s-post-summary--content-excerpt
    descripcionPregunta = pregunta.find(class_='s-post-summary--content-excerpt').text
    print(descripcionPregunta)

    