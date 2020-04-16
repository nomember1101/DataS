import requests
url='https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content=requests.get(url)
json_content = html_content.json()
print(json_content)
records=json_content.get('records')
location = records.get('location')
for i in  location:
    lat = i. get('lat')
    lon = i. get('lon')
    locationName=i.get('locationName')
    stationId=i.get('stationId')
    time=i.get('time').get('obsTime')
    print(locationName,stationId,time)

