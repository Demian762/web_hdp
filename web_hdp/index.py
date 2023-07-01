from resenas import noticias, videojuegos, cine_series
from flask import Flask, request

def generar_html(opcion='noticias', resenas=noticias):
  seccion_html = ''
  if opcion == 'noticias':
      seccion_html = f'''<section id="noticias">
                          {resenas}
                        </section>'''
  elif opcion == 'videojuegos':
      seccion_html = f'''<section id="videojuegos">
                          {resenas}
                        </section>'''
  elif opcion == 'cine-series':
      seccion_html = f'''<section id="cine-series">
                          {resenas}
                        </section>'''

  html_template = f'''
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <header>
      <div class="logo-container">
          <img src="images/logo_hdp.png" alt="HDP">
      </div>
      <nav>
        <ul>
          <button id="btn-noticias">Noticias</button>
          <button id="btn-videojuegos">Videojuegos</button>
          <button id="btn-cine-series">Cine y series</button>
        </ul>
      </nav>
    </header>
    
    <section>
      {seccion_html}
    
    <footer>
      <p>© 2023 Hablemos de Pavadas. Todos los derechos reservados.</p>
    </footer>
    <script>
  document.getElementById("btn-noticias").addEventListener("click", function() {{
    fetch('/cambiar-seccion?opcion=noticias')
      .then(response => response.text())
      .then(data => {{
        console.log(data); // Imprime la respuesta del servidor en la consola (opcional)
      }});
  }});

  document.getElementById("btn-videojuegos").addEventListener("click", function() {{
    fetch('/cambiar-seccion?opcion=videojuegos')
      .then(response => response.text())
      .then(data => {{
        console.log(data); // Imprime la respuesta del servidor en la consola (opcional)
      }});
  }});

  document.getElementById("btn-cine-series").addEventListener("click", function() {{
    fetch('/cambiar-seccion?opcion=cine-series')
      .then(response => response.text())
      .then(data => {{
        console.log(data); // Imprime la respuesta del servidor en la consola (opcional)
      }});
  }});
</script>
  </body>
  </html>
  '''

  return html_template

def generar_resenas_html(resenas):
  resenas_html = ''
  for resena in resenas:
      titulo = resena['titulo']
      contenido = resena['contenido']
      resena_html = f'''
          <article>
              <h3>{titulo}</h3>
              <p>{contenido}</p>
          </article>
      '''
      resenas_html += resena_html


app = Flask(__name__)

@app.route('/cambiar-seccion')
def cambiar_seccion():
  opcion = request.args.get('opcion')  # Obtiene la opción seleccionada desde la URL
  
  resenas_html = ''
  if opcion == 'noticias':
      resenas_html = generar_resenas_html(noticias)
  elif opcion == 'videojuegos':
      resenas_html = generar_resenas_html(videojuegos)
  elif opcion == 'cine-series':
      resenas_html = generar_resenas_html(cine_series)

  final_html = generar_html(opcion, resenas_html)

  # Retorna el HTML generado como respuesta al cliente
  return final_html

if __name__ == '__main__':
    app.run()