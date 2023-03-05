class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height}'


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
            return ("*" * self.width + "/n") * self.height
        


# get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".

# get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

# Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
        
    def __len__(self):
        return len(self.players)
    
    def __getitem__(self, i):
        return self.players[i]
    
    def __repr__(self):
        return f'Club {self.name}: {self.players}'
    
    def __str__(self):
        return f'Club {self.name} with {len(self)} players'

# class Square:
