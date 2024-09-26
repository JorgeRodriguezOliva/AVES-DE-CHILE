import requests
import json
from string import Template

div_aves = Template('''<div class="item">
                <br>
                <h5 class="spa">Español: $nombre</h5>
                <h6 class="eng">English: $name</h6>
                <img class="foto" src="$url" data-bs-toggle="tooltip" data-bs-custom-class="custom-tooltip" data-bs-html="true" data-bs-html="true" title="<b>Ubicación: $texto</b><br><br>Detalle: $otros">
                </div>
                ''')

html_full = Template('''
                <!DOCTYPE html>
                <html lang="es">
                <head>
                <meta charset="utf-8">
                <meta http-equiv=”Content-Type” content=”text/html />
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta name="author" content="Jorge Rodríguez">
                <meta name="description" content="AVES DE CHILE">
                <meta name="Keywords" content="aves, chile">
                <link rel="icon" type="image/png" href="Chile_26448.png">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"
                integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy"
                crossorigin="anonymous"></script>
                <title>AVES DE CHILE</title>
                <style>
                body{
                background-color: black;
                color: white;
                }
                .contenedor {
                
                display: inline-block;
                padding-inline: 5rem;    
                }
                .titulo {
                text-align: center;
                }
                .item {
                display: inline-block;    
                text-align: center;
                border: solid;
                margin: 2px;
                }
                .custom-tooltip{
                content: attr(data-tooltip);
                font-size: 10px;
                } 
                
                .item img{
                width: 320px;
                height: 320px;
                margin: 5px;
                transition: all 300ms;
                }
                .spa{
                    color: chartreuse
                }
                .eng{
                    color:darkorange
                }
                .item img:hover{
                transform: scale(1.25);
                }
                </style>
                </head>
                <br>
                <h1 class="titulo">AVES DE CHILE</h1>
                <br>
                <div class="contenedor">
                $body
                </div>
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
                integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
                crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"
                integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy"
                crossorigin="anonymous"></script>
                <script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4="
                crossorigin="anonymous"></script>
                <script src="index.js"></script>
                </body></html>''')


if __name__ == "__main__":
    pass

