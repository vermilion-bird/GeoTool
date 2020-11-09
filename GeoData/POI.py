import requests
from GeoData.POIException import NoKeyError


class POI:
    def __init__(self):
        self.data_hub_url = 'http://datahub.wtf/api/MapPoiRouter/getPoiList'
        self.gaode_url = 'https://restapi.amap.com/v3/place/around '
        self.baidu_url = 'http://api.map.baidu.com/place/v2/search'
        self.header = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    def get_data_hub_pois(self, **kws):
        resp = requests.get(
            self.data_hub_url, params=kws, headers=self.header)
        return resp.json()

    def get_gao_de_poi(self, key=None, **kws):
        if not key:
            raise NoKeyError(
                "没有高德地图开发者key异常，请上高德申请(https://lbs.amap.com/api/webservice/summary/)")
        kws.update({"key": key})
        resp = requests.get(self.gaode_url, headers=self.header, params=kws)
        return resp.json()

    def get_baidu_poi(self, key=None, **kws):
        if not key:
            raise NoKeyError(
                "没有百度地图开发者key异常，请上百度申请(http://lbsyun.baidu.com/index.php?title=webapi)")
        kws.update({"key": key})
        resp = requests.get(self.gaode_url, headers=self.header, params=kws)
        return resp.json()


if __name__ == '__main__':
    pass
