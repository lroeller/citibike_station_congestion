import urllib.request, json 
with urllib.request.urlopen("https://gbfs.citibikenyc.com/gbfs/en/station_information.json") as url:
    data = json.loads(url.read().decode())
    print(data)
