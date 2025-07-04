import unittest

from pydantic import ValidationError

from views.airport import AirportData


class TestAirportDataModel(unittest.TestCase):
    def test_valid_airport_data(self):
        data = {
            "airports": [
                {
                    "icao": "EDDF",
                    "links": [
                        {
                            "category": "Charts",
                            "name": "Charts (IFR)",
                            "url": "https://chartfox.org/EDDF",
                        },
                        {
                            "category": "Briefing",
                            "name": "Pilotbriefing",
                            "url": "https://aip.dfs.de/BasicVFR/pages/C019C8.html",
                        },
                    ],
                },
                {"icao": "EDDL", "links": []},
            ]
        }

        airport_data = AirportData(**data)
        self.assertEqual(len(airport_data.airports), 2)
        self.assertEqual(airport_data.airports[0].icao, "EDDF")
        self.assertEqual(airport_data.airports[1].links, [])

    def test_invalid_url(self):
        data = {
            "airports": [
                {
                    "icao": "EGLL",
                    "links": [
                        {
                            "category": "Briefing",
                            "name": "Heathrow Briefing",
                            "url": "not-a-valid-url",
                        }
                    ],
                }
            ]
        }

        with self.assertRaises(ValidationError):
            AirportData(**data)

    def test_invalid_category(self):
        data = {
            "airports": [
                {
                    "icao": "EDDF",
                    "links": [
                        {
                            "category": "InvalidCategory",
                            "name": "EDDF Charts",
                            "url": "https://example.com/eddf/charts",
                        }
                    ],
                }
            ]
        }

        with self.assertRaises(ValidationError):
            AirportData(**data)


if __name__ == "__main__":
    unittest.main()
