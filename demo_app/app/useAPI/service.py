import requests

def get_results():
    url = "http://localhost:9000/test/"
    params = {'format': 'json'}
    r = requests.get(url, params=params)
    obj = r.json()
    results_list = obj['results']
    count = int(obj['count'])
    page = 2
    while( len(results_list) != count):
        params.update({'page':page})
        r = requests.get(url, params=params)
        obj = r.json()
        for i in obj['results']:
            results_list.append(i)
        page+=1        
    return results_list