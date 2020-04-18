class Screen(object):
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @property
    def width(self,w):
        self.__width=w
    @property
    def height(self,h):
        self.__height=h
    @property
    def resolution(self):
        return self.__width*self.__height
s = Screen()
s.width=2
s.height=3
print(s.resolution)
