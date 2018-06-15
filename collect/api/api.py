#tourspot Wrapper Function
import os
from urllib.parse import urlencode
from .web_request import json_request
import math
import json


ACCESS_TOKEN='bpU9ConJZs44J4b%2FbIStu29uOgtlQ%2Fvl%2BMma1RXL5c2vz8Wdayhg33wAmEqn51Mf2loTqXUr%2BGI9QsfMdFjKXQ%3D%3D' #접속하기 위한 ACCESS_TOKEN
BASE_URL_TS_API ='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList' #api에 접속하기 위한 주소

def pd_gen_url(endpoint,serviceKey=ACCESS_TOKEN, **params): # url을 시험하기 위한 함수 endpoint주소값, serviceKey토큰값 ,**param 나머지 변수를 한번에 받음
    url = '%s?serviceKey=%s&%s' % (endpoint, serviceKey ,urlencode(params)) # url을 리턴하여 주소값을 출력
    return url

#%s?ACCESS_TOKEN=%s&%s

def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0): # 함수로 전달받은 값을 주소에 넣어 출력하기 위한 함수
    pageno =1 #페이지 값을 받아 PageNo에 저장하기 위한 변수
    isnext = True #이게 true면 루프를 돔
    while isnext is True: #isnext가 True 일때 무한루프, 탈출조건필요

        url = pd_gen_url(endpoint=BASE_URL_TS_API,
                    YM='{0:04d}{1:02d}'.format(year, month),
                    SIDO=district1,
                    GUNGU=district2,
                    RES_NM=tourspot,
                    _type='json',
                    numofrows = 10,
                    pageNo=pageno
                         )
        # 파싱하여 데이터에 접근하기 위한 방법
        json_result = json_request(url=url)
        json_response = json_result.get('response')
        json_body = json_response.get('body')
        json_items = json_body.get('items')
        json_item = json_items.get('item')
        numofrows = json_body.get('numOfRows')
        totalcount = json_body.get('totalCount')

        if totalcount==0:
            break
        last_page = math.ceil(totalcount / numofrows)
        if pageno == last_page:
            isnext = False
        else:
            pageno += 1

        yield json_item
       # items =None if json_result is None else json_result['response']['body'].get('items')  #페이징 정보를빼옴. python 3항 연산자
        #item = None if json_result is None else json_result['response']['body']['items'].get("item")

            #results+=posts #50개씩 리스트로
        #url =  None if items is None else items.get('next')  #마지막데이터는 Null
        #isnext = url is not None  #None이 아니면 True 반환 None이면 루프탈출


        #return results

    '''
    페이징 의사코드
    hasnext=True
    pageno =1
    while hasNext:
        url = pd_gen_url(.......,numOfRows=50, pageNum=pagenm)
        json_request (url=url)

        json_body = json_response.get('body')
        numofrows = json_body.get('numofRows')
        totalcount = json_body.get('totalCount')

        if totalcount=0:
            break
        last_page = math.ceil(totalcount/numofrows)
        if pageno == last_page:
            hasnext = False
        else:
            pageno +=1
    '''
