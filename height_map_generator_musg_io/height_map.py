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

   is_in_range(x: int, y: int) -> bool
      Returns true if the given (x, y) coordinate is inside the map, otherwise false.

   is_valid_height(height: float) -> bool
      Returns true if min_height <= height <= max_height, otherwise false.
   
   crop(new_x_axis_length: int, new_y_axis_length: int)
      Crops the height map to the new size.

   """

   x_axis_length: int

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
       if not self.is_in_range(x, y):
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

       if not self.is_valid_height(height):
           raise ValueError('The given height is out of range.')
       
       if not self.is_in_range(x, y):
           raise ValueError('The (x, y) coordinate is out of range.')
       
       self.__map[y][x] = height

   def is_in_range(self, x: int, y: int) -> bool:
       """Determines if a pair of (x, y) coordinates is inside the height map.

       :param x: The x coordinate.
       :type x: int

       :param y: The y coordinate.
       :type y: int

       :returns: True if the (x, y) coordinate is inside the height map, otherwise false.
       :rtype: bool
       """

       return x >= 0 and x <= self.x_axis_length - 1 and y >= 0 and y <= self.y_axis_length - 1
   
   def is_valid_height(self, height: float) -> bool:
       """Determines if the given height is valid.
       
       :param height: The height to test for validity.
       :type height: float

       :returns: True if min_height >= height <= max_height, otherwise false.
       :rtype: bool
       """

       return height >= self.min_height and height <= self.max_height
   
   def crop(self, new_x_axis_length: int, new_y_axis_length: int):
       """Crops the height map to the given size along the x and y axes.
       
       :param new_x_axis_length: The new length of the x-axis.
       :type new_x_axis_length: int

       :param new_y_axis_length: The new length of the y-axis.
       :type new_y_axis_length: int
       """

       if new_x_axis_length > self.x_axis_length or new_y_axis_length > self.y_axis_length:
           raise ValueError('The new axes are longer than the old axes.')

       for _ in range(new_y_axis_length - self.y_axis_length + 1):
           self.__map.pop()

       for row in self.__map:
           for _ in range(new_x_axis_length = self.x_axis_length + 1):
               row.pop()