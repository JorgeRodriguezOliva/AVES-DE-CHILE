import requests
import json
from string import Template
from peticiones import aves
from templates import div_aves,html_full

url="https://aves.ninjas.cl/api/birds"

listado_full = aves(url)

aves_full = ''

for p in listado_full:
    a=(p["name"]["spanish"])
    b=(p["name"]["english"])
    c=(p["images"]["main"])
    d=(p["uid"])
    url_detalle=url+'/'+d

    listado_detalle=json.loads(requests.get(url_detalle).text)
    e=listado_detalle["map"]["title"]
    f=listado_detalle["habitat"]
    aves_full += div_aves.substitute(nombre=a,name=b,url=c,texto=e,otros=f) + '\n'

html_original= html_full.substitute(body=aves_full)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_original)

