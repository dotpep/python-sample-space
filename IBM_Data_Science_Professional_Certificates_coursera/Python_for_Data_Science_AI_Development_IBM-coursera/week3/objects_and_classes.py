class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius;
        self.color = color;
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius


class Rectangle(object):
    def __init__(self, color, height, width):
        self.height = height;
        self.width = width
        self.color = color;


c1 = Circle(10, "red")
print(c1)
# give data attribute value
print(c1.radius)
print(c1.color)
# change data attribute value
c1.color = "aqua"
print(c1.color)

# Methods
# add

c1.add_radius(8)
print(c1.radius)

# function dir
# obtaining the list of data attributes and methods associated with a class. 
print(dir(Circle))
