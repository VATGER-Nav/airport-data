import unittest

from numpy.testing import assert_allclose

from src.utils.coordinate import parse_latitude, parse_longitude

# relative tolerance
RTOL = 0.0000001  # 0.0000001 => 11 cm difference, also the precision given in the example data


class TestCoordinates(unittest.TestCase):
    def test_parse_latitude(self):
        assert_allclose(50.876163055556, parse_latitude("N050.52.34.187"), rtol=RTOL)
        assert_allclose(50.877331388889, parse_latitude("N050.52.38.393"), rtol=RTOL)
        assert_allclose(50.87684, parse_latitude("N050.52.36.624"), rtol=RTOL)
        assert_allclose(50.877255833333, parse_latitude("N050.52.38.121"), rtol=RTOL)

        assert_allclose(53.631514, parse_latitude("53.631514"), rtol=RTOL)

    def test_parse_longitude(self):
        assert_allclose(7.1199863888889, parse_longitude("E007.07.11.951"), rtol=RTOL)
        assert_allclose(7.1219872222222, parse_longitude("E007.07.19.154"), rtol=RTOL)
        assert_allclose(7.1225155555556, parse_longitude("E007.07.21.056"), rtol=RTOL)
        assert_allclose(7.1234688888889, parse_longitude("E007.07.24.488"), rtol=RTOL)

        assert_allclose(10.000554, parse_longitude("10.000554"), rtol=RTOL)
