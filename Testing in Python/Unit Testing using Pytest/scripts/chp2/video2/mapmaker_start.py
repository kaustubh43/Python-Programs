class Point():
    """Coords for cities, Latitude and Longitude"""

    def __init__(self, name, lat, long) -> None:
        self._latitude = lat
        self._longitude = long
        self._name = name

    def get_lat_long(self):
        """returns latitude and longitude"""
        return self._latitude, self._longitude
