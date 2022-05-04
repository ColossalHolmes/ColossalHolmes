import requests
import xmltodict, json


def crawling_gold_price():
    try:
        url = "https://sjc.com.vn/xml/tygiavang.xml"
        resp = requests.get(url, verify=False)
        data = resp.text
        raw_data = xmltodict.parse(data)
        json_data = json.loads(json.dumps(raw_data))
        returned_data = {
            'gold_type': json_data['root']['ratelist']['city'][0]['item'][0]['@type'],
            "date": json_data['root']['ratelist']['@updated'],
            "buy_price": json_data['root']['ratelist']['city'][0]['item'][0]['@buy'],
            "sell_price": json_data['root']['ratelist']['city'][0]['item'][0]['@sell']
        }
    except:
        raise AttributeError

    return returned_data


if __name__ == "__main__":
    data = crawling_gold_price()
    print(data)
