class Square:
      def __init__(self):
          self.__height = 2
          self.__width = 2
      def set_side(self, new_side):
          self.__height = new_side
          self.__width = new_side
      def get_height(self):
          return self.__height
      def set_height(self, h):
          if h >= 0:
              self.__height = h
          else:
              raise Exception("value needs to be 0 or larger")

  square = Square()
  square.__height = 3 # raises AttributeError
  
  
  

class Square:
    def __init__(self, w, h):
        self.__height = h
        self.__width = w
  
    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_value):
        if new_value >= 0:
            self.__height = new_value
        else:
            raise Exception("Value must be larger than 0")