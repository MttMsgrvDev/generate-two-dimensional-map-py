import math
import random

class HeightMapGenerator:
   """Generates a hight map.
   
   Functions
   ------------
   generate_height_map()
      Generates a height map.
   
   """

   __x_axis_length: int

   __y_axis_length: int

   __working_axis_length: int

   __min_height: int

   __max_height: int

   __random_scale: int

   __map: list[list[int]]

   def __init__(self, x_axis_length: int, y_axis_length: int, min_height: int, max_height: int, random_scale: int) -> None:
      self.__x_axis_length = x_axis_length
      self.__y_axis_length = y_axis_length
      self.__min_height = min_height
      self.__max_height = max_height
      self.__random_scale = random_scale

      self.__working_axis_length = self.__get_closest_size(max(x_axis_length, y_axis_length))

      self.__map = [[0 for _ in range(self.__working_axis_length)] for _ in range(self.__working_axis_length)]

   def generate_height_map(self) -> list[list[int]]:
      """Generates a height map with the given length of the x and y axes and the min and maximum heights.
      
      :returns: A matrix that represents the generated hieght map.
      :rtype: list[list[int]]
      """

      self.__init_map()
      pass

   def __diamond_step(self):
      

      pass

   def __get_closest_size(self, size: int) -> int:
      """Finds the closest int x such that x = 2^n + 1 and x >= size"""

      #TODO: Need to find a more efficient method

      power = 0
      next_size = math.pow(2, power)

      while next_size < size:
         power += 1
         next_size = math.pow(2, power)

      return next_size
   
   def __init_map(self):
      self.__map[0, 0] = random.randint(self.__min_height, self.__max_height)
      self.__map[0, self.__working_axis_length - 1] = random.randint(self.__min_height, self.__max_height)
      self.__map[self.__working_axis_length - 1, 0] = random.randint(self.__min_height, self.__max_height)
      self.__map[self.__working_axis_length - 1, self.__working_axis_length - 1] = random.randint(self.__min_height, self.__max_height)