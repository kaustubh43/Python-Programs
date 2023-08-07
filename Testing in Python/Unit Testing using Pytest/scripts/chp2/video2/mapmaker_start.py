class Point():
    """Coords for cities, Latitude and Longitude"""

    def __init__(self, name, lat, long) -> None:
        if not (-90 <= lat <= 90) or not (-180 <= long <= 180):
            raise ValueError("Invalid latitude and longitude")
        if not name.isalpha():
            raise ValueError("Name should contain only alphabets")
        self._latitude = lat
        self._longitude = long
        self._name = name

    def get_lat_long(self):
        """returns latitude and longitude"""
        return self._latitude, self._longitude
