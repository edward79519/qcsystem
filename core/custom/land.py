import requests
import xml.etree.ElementTree as xET


def get_county_choice():
    choice = []
    try:
        string_xml = requests.get("https://api.nlsc.gov.tw/other/ListCounty", verify=False).content
        tree = xET.fromstring(string_xml)
        for element in tree:
            choice.append((element[0].text, element[1].text))
    except:
        print("Get County Error, Please check the url is correct.")
        choice.append(("", "取得資訊錯誤！請聯絡管理員。"))
    return choice
