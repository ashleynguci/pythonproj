# -*- coding: utf-8 -*-
"""
user interface
"""
from point import Point
from triangle import Triangle
def length(_p_1, _p_2):
    """ distance between two given points """
    return pow(((_p_1.x - _p_2.x)**2 + (_p_1.y - _p_2.y)**2), 0.5)

def main():
    """ analogous to other programming languages
        in Python has no special role
        """
# =============================================================================
#         example 1
# =============================================================================
# #    #named object created without parameters
# #    _p_1 = Point()
# #    #call object services
# #    _len_1 = _p_1.length()
# #    print("Point 1 distance from origo ", _len_1)
# #   #named object created with parameters
# #    _p_2 = Point(3, 4)
# #    #call object services
# #    _len_2 = _p_2.length()
# #    print("Point 2 distance forr origo ", _len_2)
# #    #nameless object created without parameters
# #    #call object services
# #    _len_3 = Point().length()
# #    print("Nameless point created without parameters  distance from origo ", _len_3)
# #    #nameless object created with parameters
# #    #call object services
# #    _len_4 = Point(7, 1).length()
# #    print("Nameless point created with parameters (7,1) distance from origo ", _len_4)
# =============================================================================








# =============================================================================
#      exercize2
#    create point objects and calculate the distances
# =============================================================================
    _p_1 = Point()
    _p_1.xy(1, 2)
    _p_2 = Point(4, 3)
    _p_3 = Point(6, -2)
    print(f"Point 1:({_p_1.x}, {_p_1.y}) length (length from origo) is {_p_1.length():.2f}")
    print(f"Point 2:({_p_2.x}, {_p_2.y}) length (length from origo) is {_p_2.length():.2f}")
    print(f"Point 3:({_p_3.x}, {_p_3.y}) length (length from origo) is {_p_3.length():.2f}")

    print(f"Point 1:({_p_1.x}, {_p_1.y}) length from Point 3 is {_p_1.length(_p_3):.2f}")
    print(f"Point 2:({_p_2.x}, {_p_2.y}) length from Point 1 is {_p_2.length(_p_1):.2f}")
    print(f"Point 3:({_p_3.x}, {_p_3.y}) length from Point 2 is {_p_3.length(_p_2):.2f}")

    _p_4 = Point(4, 5)
    print(f"Point 1:({_p_1.x}, {_p_1.y}) length from Point is ({_p_4.x},{_p_4.y})",
          f" is {length(_p_1, _p_4):.2f}")
    print(f"Point 2:({_p_2.x}, {_p_2.y}) length from Point is ({_p_4.x},{_p_4.y})",
          f" is {length(_p_2, _p_4):.2f}")
    print(f"Point 3:({_p_3.x}, {_p_3.y}) length from Point is ({_p_4.x},{_p_4.y})",
          f" is {length(_p_3, _p_4):.2f}")
    
    _abc = Triangle()
    
    print(_abc.perimeter(_p_1,_p_2,_p_3))
    print(_abc.area(_p_1,_p_2,_p_3))



# execute main() if the program is launched as a script,
# but not if it is imported as a module
if __name__ == "__main__":
    main()

