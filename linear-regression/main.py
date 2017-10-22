"""
This module is used to calculate a linear regression and print it's value,
which comes with some points to use as an example.
"""

from point import Point

def calculate(points):
    """
    This function is main function that calculates a linear regression.
    """
    # f(x) = ax + b
    # a = (Σy * Σx² - Σx * Σxy) / (n * Σ(x²) - (Σx)²) 
    # b = (n(Σxy) - Σx * Σy) / (n * Σ(x²) - (Σx)²))
    n = len(points)
    sum_points = Point.sum_points(points)
    sum_square = Point.sum_square_points(points)
    sum_xy = Point.sum_xy(points)

    equation_divider = n * sum_square.x - sum_points.square().x

    a = ((sum_points.y * sum_square.x) - (sum_points.x * sum_xy)) / equation_divider
    b = (n * sum_xy - (sum_points.x * sum_points.y)) / equation_divider

    print('-' * 90)
    print(f'The sum of points { points } is:')
    print(f'f(x) = { a } * x + { b }')
    return (a,b)

if __name__ == '__main__':
    a = Point(2.3, 89)
    b = Point(2.1, 63)
    c = Point(2.5, 71)
    d = Point(4.5, 70)
    e = Point(5.9, 80)
    f = Point(4.1, 89)
    g = Point(8.9, 150)    
    
    lista = [a,b,c,d,e,f,g]
    calculate(lista)