"""
This module contains the Point class that is used to represent points and to manipulate them.
"""

class Point:
    """
    A class that represents a point in a cartesian plane.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __repr__(self):
        return f"<{self.x}, {self.y}>"
    
    def sum(self, point):
        """
        Sum a point with another. p1(1,1) p2(2,2) p3 = p1.sum(p2) => (3,3)  
        """
        return Point(self.x + point.x, 
                     self.y + point.y)
    
    def xy(self):
        """
        Return the product of the image(y) with the domain(x).
        """
        return self.x * self.y

    def square(self):
        """
        Return a new point that contains the square image(y) and domain(x).
        """
        return Point(self.x ** 2,
                     self.y ** 2)

    @staticmethod
    def sum_points(points):
        """
        This function sums a list of points.

        p1(1,1); p2(2,2); p3(3,3); p4(4,4)
        l = [p1,p2,p3,p4] => Point.sum_points(l) => Point(10,10).
        """
        ret = Point(0,0)
        for point in points:
            ret = ret.sum(point)
        return ret

    @staticmethod
    def sum_xy(points):
        """
        This function returns the sum of every product of x with y of a determined Point list.
        p1(1,1); p2(2,2); p3(3,3); p4(4,4)
        l = [p1,p2,p3,p4] => Point.sum_xy(l) => Point(30,30).
        """
        ret = 0
        for point in points:
            ret += point.xy()
        return ret

    @staticmethod
    def sum_square_points(points):
        """
        Returns the sum of the square of a list of points.

        p1(1,1); p2(2,2); p3(3,3); p4(4,4)
        l = [p1,p2,p3,p4] => Point.sum_square_points(l) => Point(30,30).
        """
        ret = Point(0,0)
        for point in points:
            ret = ret.sum(point.square())
        return ret

    

