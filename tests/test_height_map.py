import unittest

from context import height_map_generator_musg_io

class TestHeightMap(unittest.TestCase):
   def test_set_height_valid_height(self):
      height_map = height_map_generator_musg_io.HeightMap(5, 5, 0, 10)

      height_map.set_height(0, 0, 5)

      self.assertEqual(5, height_map.get_height(0, 0))

   def test_set_height_valid_height(self):
      height_map = height_map_generator_musg_io.HeightMap(5, 5, 0, 10)

      height_map.set_height(0, 0, 5)

      self.assertEqual(5, height_map.get_height(0, 0))