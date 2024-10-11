"""Contains functions needed to generate a height map image.

Functions
---------

generate_height_map_image:
    Generates an image file given a height map, the minimum height, the maximum height, and the path of the output file.

"""

from PIL import Image
from color_mapper import ColorMapper


def generate_height_map_image(map: list[list[float]], min_height: float, max_height: float, file_path: str):
    """Generates an image for a given height map.

    :param map: The height map to generate the image for.
    :type map: list[list[float]]

    :param min_height: The minimum height of the height map.
    :type min_height: float

    :param max_height: The maximum height of the height map.
    :type max_height: float

    :param file_path: The path to the image file to be generated.
    :type file_path: str
    """

    color_mapper = ColorMapper(min_height, max_height)

    height = len(map)
    width = len(map[0])

    img = Image.new('L', (width, height))

    colors = __flatten_map(color_mapper.map_colors(map))

    img.putdata(colors)
    img.save(file_path)


def __flatten_map(map: list[list[int]]) -> list[int]:
    flat_list: list[int] = []

    for row in map:
        for cell in row:
            flat_list.append(cell)

    return flat_list
