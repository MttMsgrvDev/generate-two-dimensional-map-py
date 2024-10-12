import unittest

from context import height_map_generator_musg_io

class TestHeightMap(unittest.TestCase):
   def test_height_map_initialized_min_value_zero(self):
      height_map = height_map_generator_musg_io.HeightMap(3, 3, 0, 10)

      for x in range(3):
         for y in range(3):
            self.assertEqual(0, height_map.get_height(x, y))

   def test_height_map_initialized_min_value_nonzero(self):
      height_map = height_map_generator_musg_io.HeightMap(3, 3, 1, 10)

      for x in range(3):
         for y in range(3):
            self.assertEqual(1, height_map.get_height(x, y))

   def test_set_height_valid_height_origin(self):
      height_map = height_map_generator_musg_io.HeightMap(5, 5, 0, 10)

      height_map.set_height(0, 0, 5)

      self.assertEqual(5, height_map.get_height(0, 0))

   def test_set_height_valid_height_one_side(self):
      height_map = height_map_generator_musg_io.HeightMap(5, 5, 0, 10)

      height_map.set_height(0, 1, 5)

      self.assertEqual(5, height_map.get_height(0, 1))

   def test_set_height_valid_height_other_side(self):
      height_map = height_map_generator_musg_io.HeightMap(5, 5, 0, 10)

      height_map.set_height(1, 0, 5)

      self.assertEqual(5, height_map.get_height(1, 0))

   def test_is_in_range_origin_true(self):
      height_map = height_map_generator_musg_io.HeightMap(5, 5, 0, 10)

      self.assertTrue(height_map.is_in_range(0, 0))

   def test_is_in_range_edge_true(self):
      height_map = height_map_generator_musg_io.HeightMap(5, 5, 0, 10)

      self.assertTrue(height_map.is_in_range(4, 4))

   def test_is_in_range_negative_false(self):
      height_map = height_map_generator_musg_io.HeightMap(5, 5, 0, 10)

      self.assertFalse(height_map.is_in_range(-1, -1))

   def test_is_in_range_outside_false(self):
      height_map = height_map_generator_musg_io.HeightMap(5, 5, 0, 10)

      self.assertFalse(height_map.is_in_range(5, 5))