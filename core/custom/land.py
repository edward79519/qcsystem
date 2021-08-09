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


def get_area(county):
    area_xml_string = requests.get("https://api.nlsc.gov.tw/other/ListTown/{}/".format(county), verify=False).content
    area_xml = xET.fromstring(area_xml_string)
    area = []
    for i in range(len(area_xml)):
        print(area_xml[i][0].text, area_xml[i][1].text)
        area.append((area_xml[i][0].text, area_xml[i][1].text))
    return area
