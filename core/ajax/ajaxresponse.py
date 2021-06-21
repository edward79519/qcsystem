from django.http import JsonResponse
import xml.etree.ElementTree as xET
import requests
import json


def getArea(request):
    county = request.GET.get('county')
    area_xml_string = requests.get("https://api.nlsc.gov.tw/other/ListTown/{}/".format(county), verify=False).content
    area_xml = xET.fromstring(area_xml_string)
    option_html = "<option>選擇鄉鎮市區</option>"
    for i in range(len(area_xml)):
        # print(town_xml[i][0].text, town_xml[i][1].text)
        option_html += "<option value={}>{}</option>".format(area_xml[i][0].text, area_xml[i][1].text)
    print(option_html)
    return JsonResponse(option_html, safe=False)


def getSection(request):
    county = request.GET.get('county')
    area = request.GET.get('area')
    sec_xml_string = requests.get("https://api.nlsc.gov.tw/other/ListLandSection/{}/{}/".format(county, area),
                                  verify=False).content
    sec_xml = xET.fromstring(sec_xml_string)
    sec_list_html = "<option>選擇地段</option>"
    for i in range(len(sec_xml)):
        sec_list_html += \
            "<option office={} value={}>{}</option>".format(sec_xml[i][0].text, sec_xml[i][2].text,
                                                                sec_xml[i][3].text)
    print(sec_list_html)

    return JsonResponse(sec_list_html, safe=False)


def getLandGPS(request):
    office = request.GET.get('office')
    section = request.GET.get('section')
    locnum1 = request.GET.get('locnum1')
    locnum2 = request.GET.get('locnum2')
    locnum = locnum1.zfill(4)+locnum2.zfill(4)
    headers = {
        'Referer': 'https://maps.nlsc.gov.tw/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36',
    }
    session = requests.Session()
    url = "https://landmaps.nlsc.gov.tw/S_Maps/qryTileMapIndex?type=2&flag=2&" \
          "office={}&sect={}&landno={}".format(office, section, locnum)
    response = session.get(url, headers=headers)
    gpsres = json.loads(response.text[1:-1])
    if "msg" in gpsres:
        is_valid = False
    else:
        is_valid = True
    print(json.loads(response.text[1:-1]))
    print(office, section, locnum)
    context = {
        'is_valid': is_valid,
        'office': office,
        'locnum': locnum,
        'gpsres': gpsres,
    }
    return JsonResponse(context)