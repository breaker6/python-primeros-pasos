#Importamos la libreria requests
import requests
from lxml import html

#Creamos la variable encabezado con la información que enviaremos al servidor que contiene la web que queremos scrapear. Esto es necesario ya que si no lo hacemos, el servidor puede detectarnos como un robot y cortandonos en acceso
#Al enviar esta información le decimos que no somos un robot
encabezado = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}
#Ponemos en la variable url la página que queremos scrapear
url = "https://wikipedia.org/"

#Scrapeamos la información de la url escrita arriba enviando el encabezado
respuesta = requests.get(url, headers = encabezado)

#Imprimimos por pantalla la información. En este caso, será todo el html de la página
#print(respuesta.text)

#Parseamos a html el codigo plano de la página
parser = html.fromstring(respuesta.text)

#Buscamos un elemento por su id
elementobuscado = parser.get_element_by_id("js-link-box-es")
#Imprimimos por consola el text contenido del elemento con ese id
print(elementobuscado.text_content())

#Hacemos una busqueda compleja. Buscamos en todo el documento (//) la etiqueta a con la id js-link-box-es y que tenga un hijo strong y que saque su texto
#elementobuscado = parser.xpath("//a[@id='js-link-box-es']/strong/text()")
#Imprimos el elemento
#print(elementobuscado)