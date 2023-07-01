from index import generar_html
from resenas import noticias

final_html = generar_html()

# Guarda el resultado en un archivo HTML
with open('Web_HDP_GPT/index.html', 'w', encoding='utf-8') as file:
    file.write(final_html)