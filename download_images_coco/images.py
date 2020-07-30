import urllib.request
import json

with open('urls.json') as json_file:
    data = json.load(json_file)
    urls = data[:50]

    for x in urls:
        name = x[38:]
        urllib.request.urlretrieve(x, name)   