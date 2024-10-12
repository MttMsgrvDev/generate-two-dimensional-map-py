class ColorMapper:
    """Maps the heights in a height map to a color.

    Functions
    ---------

    map_colors:
        Maps the heights in a height map to colors.

    """

    def __init__(self, min_height: float, max_height: float):
        """Creates a new instance of ColorMapper

        :param min_height: The minimum allowed height for a height map.
        :type min_height: float

        :param max_height: The maximum allowed height for a height map.
        :type max_height: float
        """

        self.__min_height = min_height
        self.__max_height = max_height

    def map_colors(self, map: list[list[float]]) -> list[list[int]]:
        """Maps the heights of a height map to colors.

        :param map: The height map with the heights to be converted.
        :type map: list[list[float]]

        :returns: A matrix of color values.
        :rtype: list[list[int]]
        """

        colors: list[list[int]] = []

        for row in map:
            color_row = []
            for height in row:
                color_row.append(self.__convert_color(height))

            colors.append(color_row)

        return colors

    def __convert_color(self, height: float) -> int:
        """Converts a height to a color

        :param height: The height to be converted
        :type height: float

        :returns: The color value of the height.
        :rtype: int
        """
        old_range = self.__max_height - self.__min_height
        new_range = 255
        return int(((height - self.__min_height) * new_range) // old_range)
