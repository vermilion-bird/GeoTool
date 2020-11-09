from GeoData.POI import POI

poi = POI()

#请求自建数据
print(poi.get_data_hub_pois(lat='12',lon='13',page=1,pageSize=10))

#请求高德地图接口
print(poi.get_gao_de_poi(key=None, locations='123.12,45.12',page=1))

#请求百度地图接口
print(poi.get_baidu_poi(key=None, location='123.12,45.12',page=1))

