## 地理位置计算
    安装 geo-tools-py
    pip install geo-tools-py==1.0.0
    
    链接:https://pypi.org/project/geo-tools-py/1.0.0/

#### 坐标点最近圆形半径搜索poi搜索
        1. 自建地图数据库(datahub.wtf)
            自建数据库，主要来自地图平台，另有美团，大众点评等其他服务类数据，最新最全poi数据
        2. 百度地图
        3. 高德地图

```
from GeoData.POI import POI
    poi = POI() #请求自建数据
    print(poi.get_data_hub_pois(lat='12',lon='13',page=1,pageSize=10))
    #请求高德地图接口,请先补全key
    print(poi.get_gao_de_poi(key=None, locations='123.12,45.12',page=1))
    #请求百度地图接口,请先补全Key
    print(poi.get_baidu_poi(key=None, location='123.12,45.12',page=1))
```


#### 电子围栏（点与多边形的位置关系）
        1. 点射线法判断
```
from GeoCal.Geometry import Geometry
    print(Geometry([]).point_intersect_line({"x":1,"y":1},{"x":3,"y":10},{"x":10,"y":0.2}))
```
        2. uber h3 判断

#### 多个经纬点与多个多边形匹配计算

#### 坐标点距离计算
```
from GeoCal.LocDisDir import LocDisDir
    l = LocDisDir()
    l.geodistance(116.498079, 39.752304,117.498079, 39.752304)
```

#### 距离坐标点loc1,相距500m,与正东方向成30度角的坐标点计算
```
from GeoCal.LocDisDir import LocDisDir

lat1,lon1 =39.752304,116.498079
print(LocDisDir.get_loc_with_angle(lon1, lat1, dist=500, angle=90))
```
