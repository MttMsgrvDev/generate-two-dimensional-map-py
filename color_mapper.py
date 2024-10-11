class ColorMapper:

    def __init__(self, min_height: float, max_height: float):
        self.__min_height = min_height
        self.__max_height = max_height

    def map_colors(self, map: list[list[float]]) -> list[list[int]]:

        colors: list[list[int]] = []

        for row in map:
            color_row = []
            for height in row:
                color_row.append(self.__convert_color(height))

            colors.append(color_row)

        return colors

    def __convert_color(self, height: float) -> int:
        old_range = self.__max_height - self.__min_height
        new_range = 255
        return int(((height - self.__min_height) * new_range) // old_range)
