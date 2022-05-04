import requests
import xmltodict, json
import urllib3

def main():
    try:
        url = "https://sjc.com.vn/xml/tygiavang.xml"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        resp = requests.get(url, verify=False)
        data = resp.text
        raw_data = xmltodict.parse(data)
        json_data = json.loads(json.dumps(raw_data))
        returned_data = {
            "gold_type": json_data['root']['ratelist']['city'][0]['item'][0]['@type'],
            "date": json_data['root']['ratelist']['@updated'],
            "buy_price": json_data['root']['ratelist']['city'][0]['item'][0]['@buy'],
            "sell_price": json_data['root']['ratelist']['city'][0]['item'][0]['@sell']
        }
        output_string = " Gia {0} ngay {1}: Mua vao {2} - Ban ra {3}".format(returned_data['gold_type'], returned_data['date'], returned_data['buy_price'], returned_data['sell_price'])
    except:
        pass
    print("hohohoho")
    print(f"::set-output name=myOutput::{output_string}")


if __name__ == "__main__":
    main()
