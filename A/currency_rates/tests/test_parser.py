import unittest
from A.currency_rates.parser import parse_cbr_xml

class TestParser(unittest.TestCase):
    def test_parse_cbr_xml(self):
        sample_xml = """
        <ValCurs Date="28.04.2025" name="Foreign Currency Market">
            <Valute ID="R01010">
                <CharCode>USD</CharCode>
                <Nominal>1</Nominal>
                <Name>Доллар США</Name>
                <Value>95,32</Value>
            </Valute>
        </ValCurs>
        """
        result = parse_cbr_xml(sample_xml)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['code'], 'USD')
        self.assertEqual(result[0]['name'], 'Доллар США')
        self.assertEqual(result[0]['value'], '95,32')
        self.assertEqual(result[0]['nominal'], '1')
