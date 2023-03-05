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
        rectangle_pic = ("*" * self.width + "\n") * self.height
        return rectangle_pic
            
    def get_amount_inside(self, shape): 
        return self.get_area() // shape.get_area()
           

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.width = side
        self.height = side

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_width(self, new_side):
        self.width = new_side

    def set_height(self, new_side):
        self.height = new_side
