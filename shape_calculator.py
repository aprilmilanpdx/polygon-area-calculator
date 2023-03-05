class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


    def set_width(self, new_width):
        self.width = new_width


    def set_height(self, new_height):
        self.height = new_height


    def get_area(self):
        area = self.width * self.height
        return area


    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter
    

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal
    

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.width + "\n") * self.height
        

    #  The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

class Square:
    def __init__(self, side):
        super().init(side, side)
        self.width = side
        self.height = side


    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

# # Additionally, the set_width and set_height methods on the Square class should set both the width and height.

    def set_width(self, new_side):
        self.width = new_side


    def set_height(self, new_side):
        self.height = new_side

# The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, it should look like: Square(side=9)

    def __repr__(self):
        return f'Square(side={self.side})'


# get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.



# rect = Rectangle(5, 10)
# print(rect.get_area())
# rect.set_width(3)
# rect.set_height(6)
# print(rect.get_perimeter())
# print(rect.get_diagonal())
# print(rect)
# print(rect.get_picture())


sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
