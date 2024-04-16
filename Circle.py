import math


# 1
class Circle:

  def __init__(self, center, radius):
    self.center = center
    self.radius = radius


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y


# 3
def point_in_circle(circle, point):
  distancia = math.sqrt((point.x - circle.center.x)**2 +
                        (point.y - circle.center.y)**2)
  return distancia <= circle.radius


# 4
def rect_in_circle(circle, rectangle):
  sup_direito = Point(rectangle.canto.x + rectangle.largura, rectangle.canto.y)
  inf_esquerdo = Point(rectangle.canto.x, rectangle.canto.y - rectangle.altura)
  return (point_in_circle(circle, rectangle.canto)
          and point_in_circle(circle, sup_direito)
          and point_in_circle(circle, inf_esquerdo))


# 5
def rect_circle_overlap(circle, rectangle):
  sup_direito = Point(rectangle.canto.x + rectangle.largura, rectangle.canto.y)
  inf_esquerdo = Point(rectangle.canto.x, rectangle.canto.y - rectangle.altura)
  return (point_in_circle(circle, rectangle.canto)
          or point_in_circle(circle, sup_direito)
          or point_in_circle(circle, inf_esquerdo))


# teste
circle_center = Point(150, 100)
circle_radius = 75
circle = Circle(circle_center, circle_radius)


class Rectangle:

  def __init__(self, canto, largura, altura):
    self.canto = canto
    self.largura = largura
    self.altura = altura


rectangle_canto = Point(100, 50)
rectangle_largura = 100
rectangle_altura = 50
rectangle = Rectangle(rectangle_canto, rectangle_largura, rectangle_altura)

print("\n Ponto dentro do círculo:", point_in_circle(circle, Point(200, 100)))
print("\n Retângulo dentro do círculo:", rect_in_circle(circle, rectangle))
print("\n Sobreposição entre círculo e retângulo:",
      rect_circle_overlap(circle, rectangle))