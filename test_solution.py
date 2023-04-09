import unittest
from solution import parse_address


class TestParseAddress(unittest.TestCase):
    def test_parse_address(self):
        # Simple cases
        self.assertEqual(parse_address('Winterallee 3'), {"street": "Winterallee", "housenumber": "3"})
        self.assertEqual(parse_address('Musterstrasse 45'), {"street": "Musterstrasse", "housenumber": "45"})
        self.assertEqual(parse_address('Blaufeldweg 123B'), {"street": "Blaufeldweg", "housenumber": "123B"})

        # More complicated cases
        self.assertEqual(parse_address('Am Bächle 23'), {"street": "Am Bächle", "housenumber": "23"})
        self.assertEqual(parse_address('Auf der Vogelwiese 23 b'), {"street": "Auf der Vogelwiese", "housenumber": "23 b"})
        self.assertEqual(parse_address('4, rue de la revolution'), {"street": "rue de la revolution", "housenumber": "4"})
        self.assertEqual(parse_address('200 Broadway Av'), {"street": "Broadway Av", "housenumber": "200"})
        self.assertEqual(parse_address('Calle Aduana, 29'), {"street": "Calle Aduana", "housenumber": "29"})
        self.assertEqual(parse_address('Calle 39 No 1540'), {"street": "Calle 39", "housenumber": "No 1540"})
        self.assertEqual(parse_address('Via della Lungara, 231/233'), {"street": "Via della Lungara", "housenumber": "231/233"})
        self.assertEqual(parse_address('100, rue de la gare'), {"street": "rue de la gare", "housenumber": "100"})

        # Invalid cases
        with self.assertRaises(ValueError):
            parse_address('')
        with self.assertRaises(ValueError):
            parse_address('Winterallee')
        with self.assertRaises(ValueError):
            parse_address('3')
        with self.assertRaises(ValueError):
            parse_address('Winterallee -3')
        with self.assertRaises(ValueError):
            parse_address('Winterallee /3')
        with self.assertRaises(ValueError):
            parse_address('Winterallee (3)')
        with self.assertRaises(ValueError):
            parse_address('Winterallee "3"')



    def test_parse_address_edge_cases(self):
        # Empty input
        with self.assertRaises(ValueError):
            parse_address('')

        # One-word street names
        self.assertEqual(parse_address('Broadway 200'), {"street": "Broadway", "housenumber": "200"})
        self.assertEqual(parse_address('Woodside 8F'), {"street": "Woodside", "housenumber": "8F"})

        # One-letter street names
        self.assertEqual(parse_address('E 45th St 200'), {"street": "E 45th St", "housenumber": "200"})
        self.assertEqual(parse_address('N 5th St 200'), {"street": "N 5th St", "housenumber": "200"})

        # Street names with numbers
        self.assertEqual(parse_address('5th Avenue 200'), {"street": "5th Avenue", "housenumber": "200"})
        self.assertEqual(parse_address('1st Avenue 200'), {"street": "1st Avenue", "housenumber": "200"})

        # Complex street names
        self.assertEqual(parse_address('100, rue de la gare'), {"street": "rue de la gare", "housenumber": "100"})
        self.assertEqual(parse_address('rue de la république, 154'), {"street": "rue de la république", "housenumber": "154"})

        # Street names with special characters
        self.assertEqual(parse_address('Königstraße 10'), {"street": "Königstraße", "housenumber": "10"})
        self.assertEqual(parse_address('Friedrich-Wilhelm-Straße 3'), {"street": "Friedrich-Wilhelm-Straße", "housenumber": "3"})

        # House numbers with letters
        self.assertEqual(parse_address('Winterallee 3/a'), {"street": "Winterallee", "housenumber": "3/a"})
        self.assertEqual(parse_address('Musterstrasse 45B'), {"street": "Musterstrasse", "housenumber": "45B"})
        self.assertEqual(parse_address('Blaufeldweg 123C-4'), {"street": "Blaufeldweg", "housenumber": "123C-4"})

        # House numbers with commas
        self.assertEqual(parse_address('Via della Lungara, 231/233'), {"street": "Via della Lungara", "housenumber": "231/233"})

        # House numbers with spaces
        self.assertEqual(parse_address('Auf der Vogelwiese 23 b'), {"street": "Auf der Vogelwiese", "housenumber": "23 b"})
        self.assertEqual(parse_address('Via S. Antonio 4/b'), {"street": "Via S. Antonio", "housenumber": "4/b"})

        # House numbers with other special characters
        self.assertEqual(parse_address('Winterallee 3-5'), {"street": "Winterallee", "housenumber": "3-5"})
        self.assertEqual(parse_address('Winterallee 3:5'), {"street": "Winterallee", "housenumber": "3:5"})
        self.assertEqual(parse_address('Winterallee 3#5'), {"street": "Winterallee", "housenumber": "3#5"})


if __name__ == "__main__":
    unittest.main()

