from scripts.chp2.video2.mapmaker_start import Point
import pytest


def test_make_one_point():
    p1 = Point('Dakar', 14.7167, 17.4676)
    assert p1.get_lat_long() == (14.7167, 17.4676)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("New York", 120.678120, -555.01238)
    assert str(exp.value) == 'Invalid latitude and longitude'


def test_invalid_city_name():
    with pytest.raises(Exception) as exp:
        Point("$anFrancisco", 37.6192, 122.3816)
    assert str(exp.value) == 'Name should contain only alphabets'
