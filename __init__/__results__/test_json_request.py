from analysis_ts.collect.api import web_request as wr
from analysis_ts.collect.api import api as ap
url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'

def success_fetch_user_list(response): #fetch 어디 있는지 알고 있는 것을 가져오다, retrive 어디있는지 찾아서 가져오다. get 가져오다
    print(response)                     # callable 에서 success 값인 json_result함수를 호출

def error_fetch_user_list(e): #wr에 있는 json_request를 호출할때 url값이 맞지 않거나 오류가생기면 404출력
    print(e)



wr.json_request(url=url, success=success_fetch_user_list, error=error_fetch_user_list)
#web_request에 있는 json_request 함수호출

json_result = wr.json_request(url)
print(json_result)