import xml.etree.ElementTree as ET

def parse_cbr_xml(xml_data):
    root = ET.fromstring(xml_data)
    currencies = []
    for valute in root.findall('Valute'):
        char_code = valute.find('CharCode').text
        name = valute.find('Name').text
        value = valute.find('Value').text
        nominal = valute.find('Nominal').text
        currencies.append({
            'code': char_code,
            'name': name,
            'value': value,
            'nominal': nominal
        })
    return currencies
