class HeightMap:
   """Represents a height map.
   
   Attributes
   ----------

   x_axis_length: int
      The length of the x-axis of the map.

   y_axis_length: int
      The length of the y-axis of the map.

   min_height: float
      The minimum allowed height.

   max_height: float
      The maximum allowed height.

   Functions
   ---------

   set_height(x: int, y: int, height: float)
      Sets the height at the given position within the map.

   get_height(x: int, y: int) -> float
      Gets the height at the given position within the map.
   
   """

   axis_length: int

   y_axis_length: int

   min_height: float

   max_height: float

   __map: list[list[float]]

   def __init__(self, x_axis_length: int, y_axis_length: int, min_height: float, max_height: float):
      """Creates a new instance of HeightMap
      
      :param x_axis_length: The length of the x-axis of the map.
      :type x_axis_length: int

      :param y_axis_length: The length of the y-axis of the map.
      :type y_axis_length: int

      :param min_height: The minimum allowed height.
      :type min_height: float

      :param max_height: The maximum allowed height.
      :type max_height: float
      """

      self.x_axis_length = x_axis_length
      self.y_axis_length = y_axis_length
      self.min_height = min_height
      self.max_height = max_height

      self.__map = [[min_height for _ in range(self.x_axis_length)] for _ in range(self.y_axis_length)]

   def get_height(self, x: int, y: int) -> float:
       """Gets the height at the given (x, y) coordinate.
       
       :param x: The x coordinate.
       :type x: int

       :param y: The y coordinate.
       :type y: int

       :returns: The height at the given (x, y) coordinate.
       :rtype: float
       """
       if not self.__is_in_range(x, y):
           raise ValueError('The (x, y) coordinate is out of range.')

       return self.__map[y][x]
   
   def set_height(self, x: int, y: int, height: float):
       """Sets the height at the given (x, y) coordinate.
       
       :param x: The x coordinate.
       :type x: int

       :param y: The y coordinate.
       :type y: int

       :param height: The height value to be set.
       :type height: float
       """

       if not self.__is_valid_height(height):
           raise ValueError('The given height is out of range.')
       
       if not self.__is_in_range(x, y):
           raise ValueError('The (x, y) coordinate is out of range.')
       
       self.__map[y][x] = height

   def __is_in_range(self, x: int, y: int) -> bool:
       return x >= 0 and x <= self.x_axis_length - 1 and y >= 0 and y <= self.y_axis_length - 1
   
   def __is_valid_height(self, height: float) -> bool:
       return height >= self.min_height and height <= self.max_height