import requests
url='http://opendata.hccg.gov.tw/dataset/1f334249-9b55-4c42-aec1-5a8a8b5e07ca/resource/3f2d8472-7bae-48d0-909f-546591a34d34/download/20191231090605186.json'
html_content=requests.get(url)
print(html_content.status_code)
json_content = html_content.json()
for i in json_content :
    lat = i. get('經度')
    lon = i. get('緯度')
    locationName=i.get('站點名稱')
    stationId=i.get('站點位置')
    print(locationName,stationId,lat,lon)

