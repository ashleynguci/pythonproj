# -*- coding: utf-8 -*-
"""
class that implements 2D point
"""

class Point:
    """ class that knows x and y coordinates """

    def __init__(self, _x=0, _y=0):
        self.__x = _x
        self.__y = _y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def xy(self, _x, _y):
        """ sets new values to point's coordinates """
        self.__x = _x
        self.__y = _y

    #objects methods
#    def length(self):
#        """ Point distance from origo """
#        return pow((self.__x**2 + self.__y**2), 0.5)

    def length(self, _point=None):
        """ Point distance from origo if _point is None else
        distance from given point
        """
        if _point is None:
            _point = Point()
        return pow(((self.__x - _point.x)**2 + (self.__y - _point.y)**2), 0.5)
