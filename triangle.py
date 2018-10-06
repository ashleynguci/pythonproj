    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
from point import Point
    
class Triangle:
    def __init__(self, _p1 = None,_p2= None,_p3= None):
            _p1 = Point();
            _p2 = Point();
            _p3 = Point();
            
            self.__p1 = _p1
            self.__p2 = _p2
            self.__p3 = _p3
    """class knows 3 objects"""
    def length(self, _p1,_p2):
        return pow(((_p1.x - _p2.x)**2 + (_p1.y - _p2.y)**2), 0.5)
    
    def perimeter(self, _p1,_p2,_p3):
        ab = self.length(_p1,_p2)
        cb = self.length(_p2,_p3)
        ac = self.length(_p3,_p1)
        return ab+cb+ac
    
    def area (self, _p1,_p2,_p3):
        s = self.perimeter(_p1,_p2,_p3)/2
        ab = self.length(_p1,_p2)
        bc = self.length(_p2,_p3)
        ac = self.length(_p3,_p1)
        
        return pow((s*(s-ab)*(s-bc)*(s-ac)),0.5)
        
        