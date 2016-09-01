from geopy.geocoders import Nominatim
from geopy.distance import vincenty


class Cities():
    cities = ['Budapest', 'Miskolc', 'Krakkó', 'Los Angeles']

    @classmethod
    def closest(cls, city):
        try:
            geolocator = Nominatim()
            location = geolocator.geocode(str(city))
            code1 = (location.latitude, location.longitude)
            schools = {i: geolocator.geocode(i) for i in cls.cities}
            code2 = {i: (schools[i].latitude, schools[i].longitude) for i in schools}
            closest = {i: vincenty(code1, code2[i]).km for i in code2}
            return sorted(closest, key=closest.get)[0]
        except:
            return "Budapest"
