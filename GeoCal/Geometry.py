# -*- coding: utf-8 -*-
"""
    点射线法判断
"""
class Geometry:
    def __init__(self,shapes):
        self.shapes = shapes

    def point_intersect_Geometry(self,point,isclose=True):
        """
        point点 是否在多边形内
        :param point:
        :return:
        内 返回 True
        外 返回 False
        """
        isIn = False
        if len(self.shapes)<2:
            return False
        for i,p1 in enumerate(self.shapes,1):
            if point==p1:
                return True
            if i == len(self.shapes) and (not isclose):
                p1 =  self.shapes[i-1]
                p2 = self.shapes[0]
            elif i == len(self.shapes) and isclose:
                continue
            else:
                p2  = self.shapes[i]
            if self.__point_horizontal_intersect_line(point,p1,p2):
                isIn = not isIn
        return isIn

    def __point_horizontal_intersect_line(self,p,p1,p2):
        """
        点p的水平正方向射线  与p1,p2连接线是否相交
        :param p:
        :param p1:
        :param p2:
        :return:
        相交返回 True
        不相交返回 False
        """
        if ((p1['y']-p['y'] > 0) == (p2['y'] - p['y'] > 0)):
            return False
        c_x = ((p1['x']-p2['x']) * (p['y']-p2['y']))/(p1['y']-p2['y']) + p2['x']
        return c_x >= p['x']

if __name__ == '__main__':
    pass
    # print(Geometry([]).point_intersect_line({"x":1,"y":1},{"x":3,"y":10},{"x":10,"y":0.2}))