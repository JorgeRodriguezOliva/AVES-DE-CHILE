import requests
import json

def aves(url):
    response = json.loads(requests.get(url).text)
    return response

if __name__ == "__main__":
    aves_data = aves('https://aves.ninjas.cl/api/birds')
    print(aves_data)  
