import sys
from urllib.request import Request, urlopen #모듈임포트
from datetime import *
import json


'''
#tourspot Wrapper Function
from urllib.parse import urlencode

ACCESS_TOKEN="CltvcqjQZrEAZ%2BALT9RK1rIrikygd%2BKeHKuFqjc0N7Nf9EPcCxm3JvkMrD8AepS5BdKB6wc6prRZVSvU9DGmTg%3D%3D"
Base_URL_ts_API = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
'''
'''
def html_request(

            url='http://openapi.tour.go.kr/openapi/service',
            encoding = 'utf-8',
            success=None,
            error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)

):

    try: #예외처리
        request = Request(url) # 주소요청
        resp = urlopen(request) #url 열기
        html = resp.read().decode(encoding)

        print('%s: success for request[%s]' %(datetime.now(),url))

        if callable(success) is False:
            return html
        else:
            success(html)
    except Exception as e:
        if callable(error) is True: #함수를 부를 수 있느지 없늦지
            error(e)
'''
def json_request( #제이슨 요청함수
            url = '', #api에 접속하기 위한 url, api json_request(url=url)을 통해서 만든 주소를 전달
            encoding = 'utf-8', #utf-8로 바이트배열로 변환
            success = False, #성공을 확인하기 위한 매개변수
            error=lambda e: print('%s %s' %(e,datetime.now()), file=sys.stderr) # 에러가 발생했을시 시간과
):

    try: #예외처리
        request = Request(url) #url 요청
        resp = urlopen(request) #url 열기
        resp_body = resp.read().decode(encoding)

        json_result = json.loads(resp_body)
        json_result['response']["body"]["items"]["item"];
        print('%s: success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result
        else:
            success(json_result)
    except Exception as e:
        if callable(error) is True:  # 함수를 부를 수 있느지 없늦지
            error(e)
