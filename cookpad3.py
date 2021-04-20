import requests

def dataGet():

    # URIスキーム
    url = 'https://static.cookpad.com/hr/screen/category-1.json'

    res = requests.get(url)
    data = res.json()
   
dataGet()