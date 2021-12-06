"""
A Line class is composed by two points
a Point class is composed by two integer coordinates
"""

class Point:
    """
    A Point class is composed by two integer coordinates
    """
    def __init__(self, x: int, y: int):
        """"
        Initialize a Point class
        >>> p = Point(1, 2)
        >>> p.x
        1
        >>> p.y
        2
        """
        assert(type(x) == int and type(y) == int)
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of a Point class
        >>> p = Point(1, 2)
        >>> str(p)
        '(1, 2)'
        """
        return f'({self.x}, {self.y})'

    def __eq__(self, __o: object) -> bool:
        """
        Return True if two lines are equal, False otherwise
        >>> l1 = Line(Point(1, 2), Point(3, 4))
        >>> l2 = Line(Point(1, 2), Point(3, 4))
        >>> l1 == l2
        True
        >>> l3 = Line(Point(1, 2), Point(3, 5))
        >>> l1 == l3
        False
        """
        assert(type(__o) == Point)
        return self.x == __o.x and self.y == __o.y

    def __repr__(self) -> str:
        """
        Return a string representation of a Point class
        >>> p = Point(1, 2)
        >>> repr(p)
        'Point(1, 2)'
        """
        return f'Point({self.x}, {self.y})'

class Line:
    """
    A Line class is composed by two points
    a Point class is composed by two integer coordinates
    """
    def __init__(self, p1: Point, p2: Point):
        """
        Initialize a Line class
        >>> l = Line(Point(1, 2), Point(3, 4))
        >>> l.p1.x
        1
        >>> l.p1.y
        2
        >>> l.p2.x
        3
        >>> l.p2.y
        4
        """
        assert(type(p1) == Point and type(p2) == Point)
        self.p1 = p1
        self.p2 = p2

    def create_line_by_coordinates(self, x1, y1, x2, y2):
        """
        Alternative initialization of the class line
        """
        assert(type(x1) == int and type(y1) == int and type(x2) == int and type(y2) == int)
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        return Line(p1, p2)

    def __str__(self):
        """
        Return a string representation of a Line class
        >>> l = Line(Point(1, 2), Point(3, 4))
        >>> str(l)
        '(1, 2) -> (3, 4)'
        """
        return f'{self.p1} -> {self.p2}'

    def __eq__(self, __o: object) -> bool:
        """
        Return True if two lines are equal, False otherwise
        >>> l1 = Line(Point(1, 2), Point(3, 4))
        >>> l2 = Line(Point(1, 2), Point(3, 4))
        >>> l1 == l2
        True
        >>> l3 = Line(Point(1, 2), Point(3, 5))
        >>> l1 == l3
        False
        """
        assert(type(__o) == Line)
        return self.p1 == __o.p1 and self.p2 == __o.p2

    def list_points(self):
        """
        list of coordinates between two points
        """
        raise NotImplementedError

    def is_vertical(self):
        """
        Return True if the line is vertical, False otherwise
        >>> l = Line(Point(1, 2), Point(3, 4))
        >>> l.is_vertical()
        False
        >>> l = Line(Point(1, 2), Point(1, 4))
        >>> l.is_vertical()
        True
        """
        return self.p1.x == self.p2.x
    
    def is_horizontal(self):
        """
        Return True if the line is horizontal, False otherwise
        >>> l = Line(Point(1, 2), Point(3, 4))
        >>> l.is_horizontal()
        False
        >>> l = Line(Point(2, 1), Point(4, 1))
        >>> l.is_horizontal()
        True
        """
        return self.p1.y == self.p2.y

    def overlaps(self, l : object) -> bool:
        """
        Return True if the line overlaps with the line l, False otherwise
        >>> l1 = Line(Point(0, 9), Point(5, 9))
        >>> l2 = Line(Point(0, 9), Point(2, 9))
        >>> l1.overlaps(l2)
        True
        >>> l3 = Line(Point(1, 2), Point(3, 5))
        >>> l1.overlaps(l3)
        False
        """
        assert(type(l) == Line)
        if self.is_vertical() and l.is_vertical():
            return self.p1.x == l.p1.x
        if self.is_horizontal() and l.is_horizontal():
            return self.p1.y == l.p1.y
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()