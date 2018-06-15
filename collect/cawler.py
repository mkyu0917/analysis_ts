import os
import json
from datetime import datetime, timedelta #date객체 delta는 함수
from .api import api

RESULT_DIRECTORY='__results__/crawling/'


def preprocess_item(json_item):
    del json_item['addrCd']
    del json_item['rnum']

    # 내국인방문객수

    json_item['CustomerNationalCount'] = json_item['csNatCnt'] #데이터를 정규화를 통해서 필요한 데이터만 받아옴,
    del json_item['csNatCnt'] # 변수를 다른 변수에 할당해서 중복된 값이 생기기때문에 삭제
     #외국인방문객수

    json_item['CustomerNationlCount'] = json_item['csForCnt']
    del json_item['csForCnt']
    #관광지

    json_item['RegionNumber'] = json_item['resNm']
    del json_item['resNm']
    #날짜

    json_item['YearMonth'] = json_item['ym']
    del json_item['ym']
    #시,도

    json_item['SIDO'] = json_item['sido']
    del json_item['sido']

    #시군구

    json_item['GUNGU'] = json_item['gungu']
    del json_item['gungu']


    #kst = utc +9
    #kst = datetime.strptime(json_item['created_time'],'%Y-%m-%dT%H:%M:%S+0000') #스트링을 타임객체로 변환
    #kst = kst + timedelta(hours=9)
    #json_item['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')


def crawling_tourspot_visitor(district, start_year, end_year): #메인함수를 호출하고 전달받은 매개변수를 리스트에 저장
    results= []
    for year in range(start_year,end_year+1): #년도를 구함 ex) 17년도에서 17년도
        for month in range(1, 13):            # 1월부터 12월까지
            for json_items in api.pd_fetch_tourspot_visitor(district, year=year, month=month):  # fb_fetch에서 년도와 달을 하나씩 출력
                #print(json_items)
                for i in json_items: #출력한 값을 i에 넣고 정규화에 하나씩 추가하고 리스트에 저장
                    #print(i)
                    preprocess_item(i)
                    #results.append(i)



     # save results to file(저장, 적재)
    filename = '%s/%s_touristspot_%s_%s.json' % (RESULT_DIRECTORY, district, start_year, end_year)
    with open(filename, "w", encoding='utf-8') as outfile: #쓰기모드 utf-8로 인코딩해라
        json_string=json.dumps(
            results,
            indent=4,
            sort_keys=True,
            ensure_ascii=False) #제이슨을 만들때 띄어쓰기 4칸해라 indent, 키갑슬 정렬 sort_key,
        outfile.write(json_string)



if os.path.exists(RESULT_DIRECTORY) is False: #처음실행했을때 디렉토리가 없으면 맹그러라
    os.makedirs(RESULT_DIRECTORY)