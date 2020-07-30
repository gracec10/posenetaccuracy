import json
import dominate
import webbrowser
import time
import os
import subprocess
from dominate.tags import *

with open('urls.json') as json_file:
    data = json.load(json_file)
    urls = data [:25]

for x in urls:

    doc = dominate.document(title='Posenet')
    with doc.head:
        link(rel='icon', href='data:, ')
        script(src='https://cdn.jsdelivr.net/npm/@tensorflow/tfjs')
        script(src='https://cdn.jsdelivr.net/npm/@tensorflow-models/posenet')
        script(src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js')
    with doc:
        img(id='image', src="http://images.cocodataset.org/val2017/000000440475.jpg", crossorigin='anonymous')
        script(src='posenet.js')
    with open('index.html', 'wb') as file:
        file.write(bytes(doc.render(), "utf8"))

    p = subprocess.Popen(["google-chrome", "http://localhost:8000"])
    time.sleep(7)
    p.kill()