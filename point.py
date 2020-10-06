from math import sqrt
from math import pi
class Point:

    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def dist_to(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


    def abs(self):
        return sqrt(self.x**2 + self.y**2)

class Rectangle:
    #Two Points

    def __init__(self, point1, point2):
      self.p1 = point1
      self.p2 = point2

    def length(self):
      return abs(self.p2.x - self.p1.x)
    def height(self):
      return abs(self.p2.y - self.p1.y)
    def area(self):
      return(self.height()*self.length())
    def perimeter(self):
      return((2*self.height())+(2*self.length()))

class Circle:
  def __init__(self, point, radius):
    self.p = point
    self.rad = radius
  def pointinside(self):
    if abs(self.p.y - self.rad < 1):
      return "yes"
    else:
      return "no"
  def area(self):
    return (pi*(self.rad*self.rad))
  def perimeter(self):
    return (2*pi*self.rad)
def main():
  p1 = Point(1.0, 1.0)
  print("The point ({}, {}) is at a distance of {} from the origin.".format(p1.x, p1.y, p1.abs()))

  p2 = Point(4.0, 5.0)
  print("It is a distance {:.5} away from the point ({}, {}).".format(p1.dist_to(p2), p2.x, p2.y))

  p = Point(-2.0, 3.0)

  rad = 2

  rect = Rectangle(p1, p2)
  print("Rectangle Area:  ", rect.area())
  print("Rectangle Perimeter:  ", rect.perimeter())

  circle = Circle(p, rad)
  print("\nIs (0,1) in the circle:  ", circle.pointinside())
  print("Circle Area:  ", circle.area())
  print("Circle Perimeter:  ", circle.perimeter())
  


if __name__ == "__main__":
    main()
