import math

class Shape(object):

	def draw(self):
		pass

	def get_area(self):
		return self.get_area()

	def get_perimeter(self):
		return None
#create static method for find figure with max area
	#def get_max_shape():
		#max_shape = max(rect.get_area(), square.get_area(), circle.get_area(), triangle.get_area())
		#return

	def __str__(self):
		return 'I am Shape'

	def __cmp__(self, other):
		return cmp(self.get_area(), other.get_area())


class Rectangular(Shape):
	"""calculate area and perimeter for Rectangular"""

	def __init__(self, height, widht):
		self.height = height
		self.widht = widht

	def get_area(self):
		return self.height * self.widht

	def get_perimeter(self):
		return 2 * (self.height + self.widht)

	def __str__(self):
		return super(Rectangular, self).__str__() + ' of type Rectangular'


class Circle(Shape):
	"""calculate area and perimeter for Circle"""

	def __init__(self, radius):
		self.radius = radius

	def get_area(self):
		return math.pi * self.radius ** 2

	def get_perimeter(self):
		return math.pi * 2 * self.radius

	def __str__(self):
		return super(Circle, self).__str__() + ' of type Circle'

class Point(Shape):
	"""calculate distance between two point"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def get_distance_to(point1, point2):
		return math.sqrt(((point2.x - point1.x) ** 2) + ((point2.y - point1.y) ** 2))


class Triangle(Shape):
	"""calculate area and perimeter for Triangle"""
	def __init__(self, point1, point2, point3):
		self.point1 = point1
		self.point2 = point2
		self.point3 = point3

	@property
	def ab(self):
		return self.point1.get_distance_to(self.point2)

	@property
	def bc(self):
		return self.point2.get_distance_to(self.point3)

	@property
	def ac(self):
		return self.point1.get_distance_to(self.point3)

	def get_area(self):
		p = self.get_perimeter() / 2
		return math.sqrt((self.ab) * (p - self.bc) * (p - self.ac))

	def get_perimeter(self):
		return self.ab + self.bc + self.ac

	def __str__(self):
		return super(Triangle, self).__str__() + ' of type Triangle'


class Square(Shape):
	"""calculate area and perimeter for Square"""
	def __init__(self, side):
		#if Rectangular.height == Rectangular.widht
		self.side = side

	#def __getattr__(self, height):
		#if Rectangular.height == Rectangular.widht:
		#return getattr(self.rect, height)

	def get_area(self):
		return self.side ** 2

	def get_perimeter(self):
		return self.side * 4

	def __str__(self):
		return super(Square, self).__str__() + ' of type Square'




if __name__ == '__main__':
	rect = Rectangular(3, 3)
	p1 = Point(0, 2)
	p2 = Point(2, 2)
	p3 = Point(2, 0)
	radius = Circle(5)
	triangle = Triangle(p1, p2, p3)
	circle = Circle(5)
	square = Square(3)
	print str(triangle)
	print triangle.get_area()
	#print triangle.get_perimeter()
	#print triangle.ab
	print str(circle)
	print circle.get_area()
	#print circle.get_perimeter()
	print str(square)
	print square.get_area()
	#print square.get_perimeter()
	#triangle.ab = 10
	print str(rect)
	print rect.get_area()
	#print rect.get_perimeter()
	print 'compare'
	print cmp(rect, square)
	print cmp(triangle, rect)
	print cmp(circle, triangle)
	print cmp(square, circle)