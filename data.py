class Location:
    def __init__(self,location_name=None,
                 lat=None,lon=None,stationid=None,
                 time=None,weather_element=None):
        self.location_name=location_name
        self.lat=lat
        self.lon=lon
        self.stationid=stationid
        self.time=time
        self.weather_element=weather_element
    def from_json(self,json_data):
        self.locationName=json_data.get('locationName')