"""Contains components needed to generate a height map.

Classes
-------

HeightMapGenerator:
    Generates a height map.

"""

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

    __min_height: float

    __max_height: float

    __random_scale: float

    __step: int

    __map: list[list[float]]

    def __init__(self, x_axis_length: int, y_axis_length: int, min_height: float, max_height: float, random_scale: float) -> None:
        """Creates a new instance of HeightMapGenerator.

        :param x_axis_length: The length of the x-axis of the height map to be generated.
        :type x_axis_length: int

        :param y_axis_length: The length of the y-axis of the height map to be generated.
        :type y_axis_length: int

        :param min_height: The minimum height allowed for any point on the height map.
        :type min_height: float

        :param max_height: The maximum height allowed for any point on the height map.
        :type max_height: float

        :param random_scale: A scale value used to generate random height differences on the map. Larger values result in larger differences.
        :type random_scale: float
        """

        self.__x_axis_length = x_axis_length
        self.__y_axis_length = y_axis_length
        self.__min_height = min_height
        self.__max_height = max_height
        self.__random_scale = random_scale

        self.__working_axis_length = self.__get_closest_size(
            max(self.__x_axis_length, self.__y_axis_length))

        self.__step = self.__working_axis_length - 1

        self.__map = [[0 for _ in range(self.__working_axis_length)] for _ in range(
            self.__working_axis_length)]

    def generate_height_map(self) -> list[list[float]]:
        """Generates a height map with the given length of the x and y axes and the min and maximum heights.

        :returns: A matrix that represents the generated height map.
        :rtype: list[list[int]]
        """

        self.__init_map()

        while (self.__step > 1):

            self.__diamond_step()

            self.__square_step()

            self.__step //= 2
            self.__random_scale //= 2

        return self.__crop_map()

    def __diamond_step(self):
        half = self.__step // 2

        for x in range(half, self.__working_axis_length, self.__step):
            for y in range(half, self.__working_axis_length, self.__step):
                self.__do_diamond_step(x, y, half)

        pass

    def __do_diamond_step(self, x: int, y: int, length: int):

        value: float = 0

        value += self.__map[x - length][y - length]
        value += self.__map[x + length][y - length]
        value += self.__map[x - length][y + length]
        value += self.__map[x + length][y + length]

        value /= 4

        height = self.__generate_height_offset(value)

        self.__map[x][y] = height

    def __square_step(self):
        half = self.__step // 2

        for x in range(0, self.__working_axis_length, half):
            for y in range((x + half) % self.__step, self.__working_axis_length, self.__step):
                self.__do_square_step(x, y, half)

    def __do_square_step(self, x: int, y: int, length: int):
        value: float = 0
        count: int = 0

        if self.__is_valid_position(x - length, y):
            value += self.__map[x - length][y]
            count += 1

        if self.__is_valid_position(x + length, y):
            value += self.__map[x + length][y]
            count += 1

        if self.__is_valid_position(x, y - length):
            value += self.__map[x][y - length]
            count += 1

        if self.__is_valid_position(x, y + length):
            value += self.__map[x][y + length]
            count += 1

        value /= count

        height = self.__generate_height_offset(value)

        self.__map[x][y] = height

    def __generate_height_offset(self, height: float):

        new_height = height + (random.uniform(-1.0, 1.0) * self.__random_scale)

        return min(max(new_height, self.__min_height), self.__max_height)

    def __get_closest_size(self, size: int) -> int:
        """Finds the closest int x such that x = 2^n + 1 and x >= size"""

        # TODO: Need to find a more efficient method

        power = 0
        next_size = int(math.pow(2, power))

        while next_size < size:
            power += 1
            next_size = int(math.pow(2, power))

        return next_size + 1

    def __is_valid_position(self, x: int, y: int) -> bool:
        return x >= 0 and x < self.__working_axis_length and y >= 0 and y < self.__working_axis_length

    def __init_map(self):
        self.__map[0][0] = random.uniform(self.__min_height, self.__max_height)
        self.__map[0][self.__working_axis_length -
                      1] = random.uniform(self.__min_height, self.__max_height)
        self.__map[self.__working_axis_length -
                   1][0] = random.uniform(self.__min_height, self.__max_height)
        self.__map[self.__working_axis_length - 1][self.__working_axis_length -
                                                   1] = random.uniform(self.__min_height, self.__max_height)

    def __crop_map(self) -> list[list[float]]:
        """Crops the map to the desired size.

        :returns: A matrix of the desired size.
        :rtype: list[list[float]]
        """

        cropped_map: list[list[float]] = []

        for y in range(self.__y_axis_length):
            new_row: list[float] = []
            for x in range(self.__x_axis_length):
                new_row.append(self.__map[x][y])

            cropped_map.append(new_row)

        return cropped_map
