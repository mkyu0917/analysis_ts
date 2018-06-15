from analysis_ts.collect.api import api
from analysis_ts.collect.api import web_request

'''
url=api.pd_gen_url(
            'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
            YM='{0:04d}{1:02d}'.format(2017,2),
            SIDO="서울특별시",
            GUNGU='',
            RES_NM='',
            numOfRows=10,
            _type='json',
            pageNo=1
)

print(url)
'''

for json_item in api.pd_fetch_tourspot_visitor(district1="서울특별시",year=2012,month=7):
    print(json_item)

